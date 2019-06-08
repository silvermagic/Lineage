//
// Created by 范炜东 on 2019/4/30.
//

#ifndef PROJECT_DB_DEF_ACCOUNT_H
#define PROJECT_DB_DEF_ACCOUNT_H

#include <memory>
#include <string>
#include <ctime>

namespace db {
namespace def {

class Account : public std::enable_shared_from_this<Account> {
public:
  Account(std::string&, std::string&);

  std::string name();
  std::string password();

public:
  std::tm last_active;
  int access_level;
  std::string address;
  bool banned;
  int character_slot;

protected:
  std::string name_;
  std::string password_;
};

}
}

#endif //PROJECT_DB_DEF_ACCOUNT_H
