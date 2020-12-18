//
// Created by kyle on 2020/12/22.
//

#ifndef KGE_TCPSOCKET_H
#define KGE_TCPSOCKET_H

#include <boost/asio.hpp>
#include "Connect.h"

namespace kge {

class TcpSocket : public Connect {
public:
  TcpSocket(boost::asio::ip::tcp::socket s) : socket_(std::move(s)) {}

protected:
  void do_read() override;
  bool do_send() override;
  void do_close() override;

protected:
  boost::asio::ip::tcp::socket socket_;
};

}

#endif //KGE_TCPSOCKET_H
