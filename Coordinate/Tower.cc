//
// Created by 范炜东 on 2019/6/19.
//

#include "Object.h"
#include "Tower.h"

Tower::Tower(int x, int y): Point(x, y), objects_(), watchers_()
{
}

Tower::~Tower()
{
  objects_.clear();
  watchers_.clear();
}

void Tower::enter(std::shared_ptr<Object> obj)
{
  objects_.insert(obj);
  for (auto iter = watchers_.begin(); iter != watchers_.end(); )
  {
    if ((*iter)->destroy())
    {
      iter = watchers_.erase(iter);
      continue;
    }
    // 通知观察者iter更新可见对象列表
    (*iter)->onNotify(obj, true);
    ++iter;
  }
}

void Tower::leave(std::shared_ptr<Object> obj)
{
  objects_.erase(obj);
  for (auto iter = watchers_.begin(); iter != watchers_.end(); )
  {
    if ((*iter)->destroy())
    {
      iter = watchers_.erase(iter);
      continue;
    }
    // 通知观察者iter更新可见对象列表
    (*iter)->onNotify(obj, false);
    ++iter;
  }
}

void Tower::watch(std::shared_ptr<Object> obj, bool set = true)
{
  if (set) {
    watchers_.insert(obj);
    for (auto iter = objects_.begin(); iter != objects_.end(); )
    {
      if ((*iter)->destroy())
      {
        iter = objects_.erase(iter);
        continue;
      }
      if (obj->id() != (*iter)->id())
      {
        // 通知观察者obj更新可见对象列表
        obj->onNotify(*iter, true);
        // 提示对象iter被关注了
        (*iter)->onWatch(obj, true);
      }
      ++iter;
    }
  } else {
    watchers_.erase(obj);
    for (auto iter = objects_.begin(); iter != objects_.end(); )
    {
      if ((*iter)->destroy())
      {
        iter = objects_.erase(iter);
        continue;
      }
      if (obj->id() != (*iter)->id())
      {
        // 通知观察者obj更新可见对象列表
        obj->onNotify(*iter, false);
        // 提示对象iter被取关了
        (*iter)->onWatch(obj, false);
      }
      ++iter;
    }
  }
}