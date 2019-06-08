//
// Created by 范炜东 on 2019/5/9.
//

#ifndef PROJECT_ACCOUNT_H
#define PROJECT_ACCOUNT_H

#include "Templates/Account.h"

class Player;
class Account : public db::def::Account {
public:
  static std::string encrypt(std::string);

public:
  Account(std::string&, std::string&, std::shared_ptr<Player>);
  ~Account();

  // 从数据库加载账户
  bool load();

  // 验证密码是否有效
  bool validate(std::string&);

  // 获取账户对应客户端对象
  std::shared_ptr<Player> player();

protected:
  std::shared_ptr<Player> player_;
};

#endif //PROJECT_ACCOUNT_H
