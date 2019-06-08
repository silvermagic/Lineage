//
// Created by 范炜东 on 2019/5/13.
//

#include <cassert>
#include "Account.h"
#include "Player.h"
#include "LoginController.h"

LoginController::LoginController() : accounts_() {
}

LoginController::~LoginController() {
  assert(accounts_.size() == 0);
}

bool LoginController::initialize() {
  return true;
}

bool LoginController::add(std::shared_ptr<Account> account) {
  if (account != nullptr) {
    std::shared_ptr<Player> player = nullptr;
    {
      std::lock_guard<std::mutex> guard(lock_);
      std::string name = account->name();
      auto iter = accounts_.find(name);
      if (iter != accounts_.end()) {
        // 踢掉已登入账户
        player = iter->second->player();
      } else {
        // 添加登入账户信息
        accounts_[name] = account;
        return true;
      }
    }
    player->stop();
  }
  return false;
}

void LoginController::remove(std::shared_ptr<Account> account) {
  if (account != nullptr) {
    // 移除登入账户信息
    std::lock_guard<std::mutex> guard(lock_);
    std::string name = account->name();
    accounts_.erase(name);
  }
}