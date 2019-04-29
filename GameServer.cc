//
// Created by 范炜东 on 2019/4/24.
//

#include "Config.h"
#include "Logger.h"
#include "Player.h"
#include "GameServer.h"

GameServer::GameServer() : io_context_(),
                           signals_(io_context_),
                           acceptor_(io_context_),
                           connection_manager_() {
  // 捕获信号量
  signals_.add(SIGINT);
  signals_.add(SIGTERM);
  do_await_stop();

  // 监听套接字
  boost::asio::ip::tcp::endpoint endpoint(boost::asio::ip::make_address_v4("0.0.0.0"), Config::SERVER_PORT);
  acceptor_.open(endpoint.protocol());
  acceptor_.set_option(boost::asio::ip::tcp::acceptor::reuse_address(true));
  acceptor_.bind(endpoint);
  acceptor_.listen();
  do_accept();
}

void GameServer::run() {
  LOG_INFO << "GameServer::run start";
  io_context_.run();
  LOG_INFO << "GameServer::run stop";
}

void GameServer::do_accept() {
  acceptor_.async_accept(
          [this](boost::system::error_code ec, boost::asio::ip::tcp::socket socket) {
            if (!acceptor_.is_open()) {
              return;
            }

            if (!ec) {
              connection_manager_.start(std::make_shared<Player>(std::move(socket), connection_manager_));
            }

            do_accept();
          });
}

void GameServer::do_await_stop() {
  signals_.async_wait(
          [this](boost::system::error_code /*ec*/, int /*signo*/) {
            LOG_INFO << "GameServer::do_await_stop Ctrl+C";
            acceptor_.close();
            connection_manager_.stop();
          });
}