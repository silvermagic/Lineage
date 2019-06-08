//
// Created by 范炜东 on 2019/4/30.
//

#ifndef PROJECT_DB_OPER_ACCOUNT_H
#define PROJECT_DB_OPER_ACCOUNT_H

namespace db {
namespace def {
class Account;
}
namespace oper {

class Account {
public:
  static void insert(std::shared_ptr<def::Account>);

  static std::shared_ptr<def::Account> query(std::string&);

  static void update(std::shared_ptr<def::Account>);
};

}
}

#endif //PROJECT_DB_OPER_ACCOUNT_H
