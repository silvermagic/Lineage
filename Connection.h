//
// Created by 范炜东 on 2019/4/25.
//

#ifndef PROJECT_CONNECTION_H
#define PROJECT_CONNECTION_H

#include <mutex>
#include <queue>
#include <vector>
#include <memory>
#include <boost/asio.hpp>

class ClientPacket;
class ServerPacket;
class ConnectionManager;
class Connection : public std::enable_shared_from_this<Connection> {
public:
  Connection(const Connection&) = delete;
  Connection& operator=(const Connection&) = delete;
  Connection(boost::asio::ip::tcp::socket socket, ConnectionManager& manager);

  // 启动连接的首次异步操作
  void start();

  // 停止连接所有关联的异步操作
  virtual void stop();

  // 返回处理结果
  void write(ServerPacket &pkt);

  // 请求处理
  virtual void handle() = 0;

  // 获取连接的对端信息
  std::string address();

protected:
  // 执行异步读消息头
  void do_read_header();

  // 执行异步读消息体
  void do_read_body(std::size_t size);

  // 执行写操作
  void do_write();

  // 加密
  void encrypt(std::vector<char> &msg);

  // 解密
  void decrypt();

protected:
  // 连接相关
  std::string address_;
  boost::asio::ip::tcp::socket socket_; // 连接套接字
  ConnectionManager& connection_manager_; // 连接管理器
  // 读写相关（单读者多写者）
  std::mutex e_lock_; // 加密锁
  unsigned int encrypt_[2], decrypt_[2]; // 加密、解密秘钥
  std::vector<char> read_msg_; // 消息缓存
  std::mutex w_lock_; // 缓冲队列锁
  std::queue<std::vector<char>> write_msgs_; // 发送缓冲队列
};

#endif //PROJECT_CONNECTION_H
