//
// Created by 范炜东 on 2019/6/19.
//

#ifndef PROJECT_LOCATION_H
#define PROJECT_LOCATION_H

#include "Point.h"

class Location : public Point {
public:
  Location(int);
  Location(int, int, int);

  // 等值运算符重载
  bool operator==(const Location& loc);

  // 基于当前位置得到一个可随机移动的位置
  Location randomMovement(int max, bool isRandomTeleport);
  Location randomMovement(int min, int max, bool isRandomTeleport);

  // 字符串表示
  std::string toString();

  int id() const;
  void id(int);
  std::shared_ptr<Map> map();

protected:
  int id_; // 地图编号
  std::shared_ptr<Map> map_;
};

#endif //PROJECT_LOCATION_H
