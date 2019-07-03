//
// Created by 范炜东 on 2019/6/19.
//

#ifndef PROJECT_DB_OPER_MAP_H
#define PROJECT_DB_OPER_MAP_H

#include <vector>
#include <memory>

namespace db {
namespace def {
class Map;
}
namespace oper {

class Map {
public:
  static std::vector<std::shared_ptr<def::Map>> query();
};

}
}

#endif //PROJECT_DB_OPER_MAP_H
