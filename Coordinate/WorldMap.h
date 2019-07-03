//
// Created by 范炜东 on 2019/6/19.
//

#ifndef PROJECT_WORLDMAP_H
#define PROJECT_WORLDMAP_H

#include <boost/asio.hpp>
#include "Singleton.h"

class Map;
class WorldMap : public Singleton<WorldMap>, public boost::asio::io_context {
public:
  // 初始化
  bool initialize();

  // 获取对应地图
  std::shared_ptr<Map> operator[](int id);

protected:
  std::map<int, std::shared_ptr<Map>> maps_;
};

#endif //PROJECT_WORLDMAP_H
