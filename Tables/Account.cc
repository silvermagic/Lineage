//
// Created by 范炜东 on 2019/4/30.
//

#include "Logger.h"
#include "ConnectionPoolManager.h"
#include "Templates/Account.h"
#include "Account.h"

namespace db {
namespace oper {

void Account::insert(std::shared_ptr<def::Account> account) {
  LOG_DEBUG << "Account::insert " << account->name();
  session sql(ConnectionPoolManager::instance());
  account->access_level = 0;
  account->banned = false;
  account->character_slot = 0;
  int banned = int(account->banned);
  sql << "insert into accounts (name, password, last_active, access_level, address, banned, character_slot) values "
         "(:name, :password, :last_active, :access_level, :address, :banned, :character_slot)",
          use(account->name()),
          use(account->password()),
          use(account->last_active),
          use(account->access_level),
          use(account->address),
          use(banned),
          use(account->character_slot);
}

std::shared_ptr<def::Account> Account::query(std::string &name) {
  LOG_DEBUG << "Account::query " << name;
  std::shared_ptr<def::Account> account = nullptr;
  row r;
  session sql(ConnectionPoolManager::instance());
  sql << "select name, password, last_active, access_level, address, banned, character_slot from accounts where name = :name", use(name), into(r);
  if (sql.got_data()) {
    std::string name, password;
    r >> name >> password;
    account = std::make_shared<def::Account>(name, password);
    int banned;
    r >> account->last_active >> account->access_level >> account->address >> banned >> account->character_slot;
    account->banned = banned != 0;
  }

  LOG_DEBUG << "Account::query " << name << (account != nullptr ? " success" : " failed");
  return account;
}

void Account::update(std::shared_ptr<def::Account> account) {
  LOG_DEBUG << "Account::update " << account->name();
  session sql(ConnectionPoolManager::instance());
  int banned = int(account->banned);
  sql << "update accounts "
         "set password = :password, last_active = :last_active, access_level = :access_level, address = :address, banned = :banned, character_slot = :character_slot "
         "where name = :name",
          use(account->password()),
          use(account->last_active),
          use(account->access_level),
          use(account->address),
          use(banned),
          use(account->character_slot),
          use(account->name());
}

}
}