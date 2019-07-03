//
// Created by 范炜东 on 2019/6/17.
//

#ifndef PROJECT_OBJECT_H
#define PROJECT_OBJECT_H

#include <memory>
class Object : public std::enable_shared_from_this<Object> {
public:
  Object(int);

  // 对象AOI处理: 对象obj进入/离开自身视野范围、自己被对象obj关注/取关了
  virtual void onNotify(std::shared_ptr<Object> obj, bool enter);
  virtual void onWatch(std::shared_ptr<Object> obj, bool enter);

  // 对象ID
  int id();

  // 对象类型
  virtual int type();

  // 对象是否已经离开游戏世界
  bool destroy();

  // 对象可见范围
  int range();

  // 对象字符串表示
  std::string toString();

protected:
  int id_; // 对象编号
  bool destroy_; // 对象是否已经离开游戏世界
  int range_; // 对象视野半径
};

class ObjectCompare
{
public:
  bool operator()(const std::shared_ptr<Object> &lhs, const std::shared_ptr<Object> &rhs) const
  {
    return lhs->id() < rhs->id();
  }
};

#endif //PROJECT_OBJECT_H
