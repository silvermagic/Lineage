//
// Created by 范炜东 on 2019/5/9.
//

#include "Account.h"

namespace db {
namespace def {

Account::Account(std::string &name, std::string &password) : name_(name), password_(password) {
}

std::string Account::name() {
  return name_;
}

std::string Account::password() {
  return password_;
}

}
}