//
// Created by 范炜东 on 2019/4/24.
//

#ifndef PROJECT_GAMESERVER_H
#define PROJECT_GAMESERVER_H

#include "ConnectionManager.h"
#include <boost/asio.hpp>

class GameServer {
public:
  GameServer(const GameServer&) = delete;
  GameServer& operator=(const GameServer&) = delete;
  GameServer();

  // 启动游戏服务(加载数据库信息->加载地图->游戏初始化->开始监听连接)
  void run();

protected:
  // 执行异步监听操作
  void do_accept();

  // 处理CTRL+C
  void do_await_stop();

protected:
  boost::asio::io_context io_context_; // 异步操作执行上下文
  boost::asio::signal_set signals_; // 退出信号处理
  boost::asio::ip::tcp::acceptor acceptor_; // 连接接收器
  ConnectionManager connection_manager_; // 连接管理
};

#endif //PROJECT_GAMESERVER_H
