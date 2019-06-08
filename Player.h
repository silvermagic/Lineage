//
// Created by 范炜东 on 2019/4/25.
//

#ifndef PROJECT_PLAYER_H
#define PROJECT_PLAYER_H

#include "Connection.h"

class Account;
class Player : public Connection {
public:
  Player(boost::asio::ip::tcp::socket socket, ConnectionManager& manager);
  ~Player();

  void stop() override;

  // 请求处理
  void handle() override;

  // 属性存取
  std::shared_ptr<Account> account();
  void account(std::shared_ptr<Account>);

protected:
  std::shared_ptr<Account> account_;
};

#endif //PROJECT_PLAYER_H
