//
// Created by 范炜东 on 2019/5/13.
//

#ifndef PROJECT_CHARACTER_H
#define PROJECT_CHARACTER_H

#include <vector>

namespace db {
namespace def {
class Character;
}
namespace oper {

class Character {
public:
  static void insert(std::shared_ptr<def::Character>);

  static std::shared_ptr<def::Character> query(std::string&);

  static std::vector<std::shared_ptr<def::Character>> query_by_account(std::string&);

  static void update(std::shared_ptr<def::Character>);

  static std::vector<std::string> delete_expired(std::string&);
};

}
}

#endif //PROJECT_CHARACTER_H
