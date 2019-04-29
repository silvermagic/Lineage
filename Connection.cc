//
// Created by 范炜东 on 2019/4/25.
//

#include <algorithm>
#include "Logger.h"
#include "Common.h"
#include "Opcodes.h"
#include "ServerPackets/ServerPacket.h"
#include "ClientPackets/ClientPacket.h"
#include "ConnectionManager.h"
#include "Connection.h"

// 将乱数数值混淆用的混淆密码
static const unsigned int C1 = 0x9c30d539L;
// 初始的解码数值
static const unsigned int C2 = 0x930fd7e2L;
// 将乱数数值混淆用的混淆密码
static const unsigned int C3 = 0x7c72e993L;
// 将封包数值混淆用的混淆密码
static const unsigned int C4 = 0x287effc3L;
// 初始数据包
static const unsigned char FIRST_PACKET[] = {0xF4, 0x0a, 0x8d, 0x23, 0x6f, 0x7f, 0x04, 0x00, 0x05, 0x08, 0x00};

// 计算数据体长度
static std::size_t bytes2uint(std::vector<char> &msg) {
  std::size_t i = (unsigned int)msg[0] & 0xFF;
  i |= msg[1] << 8 & 0xFF00L;
  return i;
}

// 计算密钥掩码
static unsigned int bytes2uint(char *pbuf) {
  unsigned int i = (unsigned int)pbuf[0] & 0xFFL;
  i |= pbuf[1] << 8 & 0xFF00L;
  i |= pbuf[2] << 16 & 0xFF0000L;
  i |= pbuf[3] << 24 & 0xFF000000L;
  return i;
}

Connection::Connection(boost::asio::ip::tcp::socket socket, ConnectionManager &manager) : socket_(std::move(socket)),
                                                                                          connection_manager_(manager),
                                                                                          e_lock_(), encrypt_(),
                                                                                          decrypt_(), read_msg_(),
                                                                                          w_lock_(), write_msgs_() {
  address_ = socket_.remote_endpoint().address().to_string();
}

void Connection::start() {
  // 密钥初始化
  unsigned int key = 2147483647 ^ C1;
  key = key >> 13 | key << 19;
  encrypt_[0] = decrypt_[0] = key;
  encrypt_[1] = decrypt_[1] = C2 ^ key ^ C3;
  // 初始包发送（初始包发送不需要加锁）
  ServerPacket pkt;
  pkt.writeC(Opcodes::S_OPCODE_INITPACKET);
  pkt.writeD(2147483647);
  pkt.writeBytes((char *)FIRST_PACKET, sizeof(FIRST_PACKET));
  std::vector<char> msg(pkt.size() + HEADER_LENGTH);
  msg[0] = msg.size() & 0xFF;
  msg[1] = msg.size() >> 8 & 0xFF;
  std::copy(pkt.data(), pkt.data() + pkt.size(), msg.begin() + HEADER_LENGTH);
  write_msgs_.push(msg);
  auto self(shared_from_this());
  boost::asio::async_write(socket_, boost::asio::buffer(write_msgs_.front().data(), write_msgs_.front().size()),
                           [this, self](boost::system::error_code ec, std::size_t /*length*/) {
                             if (!ec) {
                               write_msgs_.pop();
                               LOG_INFO << "Connection::start handshake success";
                               do_read_header();
                             } else {
                               LOG_ERROR << "Connection::start handshake failed";
                               connection_manager_.stop(shared_from_this());
                             }
                           });
}

void Connection::stop() {
  socket_.close();
}

void Connection::write(ServerPacket &pkt) {
  // 拷贝数据包
  std::size_t size = 4 * (pkt.size() / 4 + 1);
  std::vector<char> raw(size, '\0');
  std::copy(pkt.data(), pkt.data() + pkt.size(), raw.begin());

  // 数据包加密处理
  LOG_DEBUG << "[Send Before] " << bytes_to_str(raw.data(), raw.size());
  encrypt(raw);
  std::vector<char> msg(raw.size() + HEADER_LENGTH);
  msg[0] = msg.size() & 0xFF;
  msg[1] = msg.size() >> 8 & 0xFF;
  std::copy(raw.data(), raw.data() + raw.size(), msg.begin() + HEADER_LENGTH);
  LOG_DEBUG << "[Send After] " << bytes_to_str(msg.data(), msg.size());

  // 放入发送缓冲队列
  std::lock_guard<std::mutex> guard(w_lock_);
  bool write_in_progress = !write_msgs_.empty();
  write_msgs_.push(msg);
  if (!write_in_progress) {
    do_write();
  }
}

std::string Connection::address() {
  return address_;
}

void Connection::do_read_header() {
  auto self(shared_from_this());
  read_msg_.resize(HEADER_LENGTH);
  boost::asio::async_read(socket_,
                          boost::asio::buffer(read_msg_.data(), read_msg_.size()),
                          [this, self](boost::system::error_code ec, std::size_t /*length*/) {
                            if (!ec) {
                              std::size_t size = bytes2uint(read_msg_);
                              if (size > MAX_BODY_LENGTH) {
                                connection_manager_.stop(shared_from_this());
                              } else {
                                do_read_body(size - HEADER_LENGTH);
                              }
                            } else {
                              LOG_ERROR << "Connection::do_read_header failed [" << address_ << "]";
                              connection_manager_.stop(shared_from_this());
                            }
                          });
}

void Connection::do_read_body(std::size_t size) {
  auto self(shared_from_this());
  read_msg_.resize(size);
  boost::asio::async_read(socket_,
                          boost::asio::buffer(read_msg_.data(), read_msg_.size()),
                          [this, self, size](boost::system::error_code ec, std::size_t /*length*/) {
                            if (!ec) {
                              // 数据包解码
                              decrypt();
                              LOG_DEBUG << "[Recv] " << bytes_to_str(read_msg_.data(), read_msg_.size());
                              // 处理读取到的数据包
                              handle();
                              // 获取下个数据包首部
                              do_read_header();
                            } else {
                              LOG_ERROR << "Connection::do_read_body failed [" << address_ << "]";
                              connection_manager_.stop(shared_from_this());
                            }
                          });
}

void Connection::do_write() {
  auto self(shared_from_this());
  boost::asio::async_write(socket_, boost::asio::buffer(write_msgs_.front().data(), write_msgs_.front().size()),
                           [this, self](boost::system::error_code ec, std::size_t /*length*/) {
                             if (!ec) {
                               std::lock_guard<std::mutex> guard(w_lock_);
                               write_msgs_.pop();
                               if (!write_msgs_.empty()) {
                                 do_write();
                               }
                             } else {
                               LOG_ERROR << "Connection::do_write failed [" << address_ << "]";
                               connection_manager_.stop(shared_from_this());
                             }
                           });
}

void Connection::encrypt(std::vector<char> &msg) {
  std::lock_guard <std::mutex> guard(e_lock_);
  char *key = reinterpret_cast<char*>(&encrypt_);
  char *pbuf = msg.data();
  unsigned int mask = bytes2uint(pbuf);
  pbuf[0] ^= key[0];
  for (std::size_t i = 1; i < msg.size(); i++) {
    pbuf[i] ^= pbuf[i - 1] ^ key[i & 7];
  }
  pbuf[3] ^= key[2];
  pbuf[2] ^= pbuf[3] ^ key[3];
  pbuf[1] ^= pbuf[2] ^ key[4];
  pbuf[0] ^= pbuf[1] ^ key[5];
  encrypt_[0] ^= mask;
  encrypt_[1] = (unsigned int)((encrypt_[1] + C4) & 0xFFFFFFFFL);
}

void Connection::decrypt() {
  char *key = reinterpret_cast<char*>(&decrypt_);
  char *pbuf = read_msg_.data();
  char k = pbuf[0] ^ pbuf[1] ^ key[5];
  pbuf[0] = k ^ key[0];
  pbuf[1] ^= pbuf[2] ^ key[4];
  pbuf[2] ^= pbuf[3] ^ key[3];
  pbuf[3] ^= key[2];
  for (std::size_t i = 1; i < read_msg_.size(); i++) {
    char t = pbuf[i];
    pbuf[i] ^= key[i & 7] ^ k;
    k = t;
  }
  unsigned int mask = bytes2uint(pbuf);
  decrypt_[0] ^= mask;
  decrypt_[1] = (unsigned int)((decrypt_[1] + C4) & 0xFFFFFFFFL);
}