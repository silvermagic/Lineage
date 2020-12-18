//
// Created by kyle on 2020/12/22.
//

#ifndef KGE_SSLSOCKET_H
#define KGE_SSLSOCKET_H

#include <boost/asio.hpp>
#include "Connect.h"

namespace kge {

class SslSocket : public Connect {
public:
  SslSocket(boost::asio::ssl::stream<boost::asio::ip::tcp::socket>);

protected:
  void do_handshake() override;
  void do_read() override;
  bool do_send() override;
  void do_close() overide;

protected:
  boost::asio::ssl::stream<boost::asio::ip::tcp::socket> socket_;
};

}

#endif //KGE_SSLSOCKET_H