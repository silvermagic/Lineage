//
// Created by 范炜东 on 2019/5/13.
//

#ifndef PROJECT_LOGINCONTROLLER_H
#define PROJECT_LOGINCONTROLLER_H

#include <map>
#include "Singleton.h"

class Account;
class LoginController : public Singleton<LoginController> {
public:
  LoginController();
  ~LoginController();

  // 初始化
  bool initialize();

  // 添加登入账户
  bool add(std::shared_ptr<Account>);

  // 移除登入账户
  void remove(std::shared_ptr<Account>);

protected:
  std::mutex lock_;
  std::map<std::string, std::shared_ptr<Account>> accounts_;
};

#endif //PROJECT_LOGINCONTROLLER_H
