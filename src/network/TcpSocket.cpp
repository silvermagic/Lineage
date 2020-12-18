//
// Created by kyle on 2020/12/22.
//

#include "network/TcpSocket.h"

namespace kge {

TcpSocket::TcpSocket(boost::asio::ip::tcp::socket s) : socket_(std::move(s)) {}

void TcpSocket::do_read() {
  auto self(shared_from_this());
  socket_.async_read_some(boost::asio::buffer(buffer_->data(), buffer_->size() - buffer_->transfered()),
                          [this, self](const boost::system::error_code &ec, std::size_t length) {
                            buffer_->transfered(length);
                            do_handle();
                            // 然后开始新一轮数据包接收
                            do_read();
                          });
}

bool TcpSocket::do_send() {
  if (write_queue_.empty())
    return false;

  std::shared_ptr<Packet> pkt = write_queue_.front();
  boost::system::error_code error;
  std::size_t transferred = socket_.write_some(
    boost::asio::buffer(pkt->data() + pkt->transfered(), pkt->size() - pkt->transfered()), error);
  if (error) {
    if (error == boost::asio::error::would_block || error == boost::asio::error::try_again)
      return Send();

    write_queue_.pop();
    if (closing_ && write_queue_.empty())
      Close();
    return false;
  } else if (transferred == 0) {
    write_queue_.pop();
    if (closing_ && write_queue_.empty())
      Close();
    return false;
  } else if (transferred < (pkt->size() - pkt->transfered())) {
    pkt->transfered(transferred);
    return Send();
  }

  write_queue_.pop();
  if (closing_ && write_queue_.empty())
    Close();
  return !write_queue_.empty();
}

void TcpSocket::do_close() {
  boost::system::error_code error;
  socket_.shutdown(boost::asio::socket_base::shutdown_send, error);
}

}
