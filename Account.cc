//
// Created by 范炜东 on 2019/5/9.
//

#include "Config.h"
#include "Logger.h"
#include "Player.h"
#include "Tables/Account.h"
#include "Account.h"

std::string Account::encrypt(std::string v) {
  return v;
}

Account::Account(std::string &name, std::string &password, std::shared_ptr<Player> player) : db::def::Account(name, password), player_(player) {
  address = player_->address();
  std::time_t t = std::time(nullptr);
  last_active = *std::localtime(&t);
}

Account::~Account() {
}

bool Account::load() {
  LOG_DEBUG << "Account::load " << name_;
  auto iter = db::oper::Account::query(name_);
  if (iter == nullptr) {
    if (Config::AUTO_CREATE_ACCOUNTS) {
      db::oper::Account::insert(shared_from_this());
    } else {
      return false;
    }
  } else {
    password_ = iter->password();
    access_level = iter->access_level;
    banned = iter->banned;
    character_slot = iter->character_slot;
  }

  return true;
}

bool Account::validate(std::string &v) {
  LOG_DEBUG << "Account::validate " << name_;
  return password_ == v;
}

std::shared_ptr<Player> Account::player() {
  return player_;
}