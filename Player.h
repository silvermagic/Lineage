//
// Created by 范炜东 on 2019/4/25.
//

#ifndef PROJECT_PLAYER_H
#define PROJECT_PLAYER_H

#include "Connection.h"

class Player : public Connection {
public:
  Player(boost::asio::ip::tcp::socket socket, ConnectionManager& manager);
  ~Player();

  // 请求处理
  void handle() override;
};

#endif //PROJECT_PLAYER_H
