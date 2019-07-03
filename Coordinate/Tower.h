//
// Created by 范炜东 on 2019/6/19.
//

#ifndef PROJECT_TOWER_H
#define PROJECT_TOWER_H

#include <set>
#include <map>

#include "Point.h"

class Object;
class Tower : public Point
{
public:
  Tower(int x, int y);
  virtual ~Tower();

  // 对象进入灯塔监控范围
  void enter(std::shared_ptr<Object> obj);

  // 对象离开灯塔监控范围
  void leave(std::shared_ptr<Object> obj);

  // 设置/取消对象为灯塔的观察者
  void watch(std::shared_ptr<Object> obj, bool set);

protected:
  std::set<std::shared_ptr<Object>, ObjectCompare> objects_; // 灯塔监控范围内的对象
  std::set<std::shared_ptr<Object>, ObjectCompare> watchers_; // 灯塔绑定的观察者对象
};

#endif //PROJECT_TOWER_H
