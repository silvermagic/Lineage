//
// Created by 范炜东 on 2019/6/19.
//

#include <cmath>
#include "Config.h"
#include "Object.h"
#include "Tower.h"
#include "TowerAoi.h"

TowerAoi::TowerAoi(int id, int x, int y, int width, int height) : id_(id),
        area_(x, y, static_cast<int>(std::ceil(static_cast<float>(width) / (2 * Config::AOI_RECOGNIZE_RANGE + 1))), static_cast<int>(std::ceil(static_cast<float>(height) / (2 * Config::AOI_RECOGNIZE_RANGE + 1)))),
        towers_(static_cast<size_t>(area_.width() * area_.height())) {
}

TowerAoi::~TowerAoi() {
  towers_.clear();
}

void TowerAoi::initialize() {
  // 将游戏地图坐标映射为灯塔坐标
  for (int y = 0; y < area_.height(); ++y) {
    for (int x = 0; x < area_.width(); ++x) {
      towers_[static_cast<size_t>(x + y * area_.width())] = std::make_shared<Tower>(x, y);
    }
  }
}

bool TowerAoi::enter(std::shared_ptr<Object> obj, const Point &pt) {
  std::shared_ptr<Tower> pTower = find(pt);
  // 对象进入灯塔的监控范围
  pTower->enter(obj);

  // 如果对象有视野，则绑定到视野内的灯塔
  int range = obj->range();
  if (range > 0) {
    // 首先计算出对象视野范围内的灯塔
    auto area = vision(pt, range);
    for (int x = area.x(); x <= area.x() + area.width(); ++x) {
      for (int y = area.y(); y <= area.y() + area.height(); ++y) {
        // 绑定对象为灯塔的观察者
        towers_[static_cast<size_t>(x + y * area_.width())]->watch(obj, true);
      }
    }
  }

  return true;
}

bool TowerAoi::leave(std::shared_ptr<Object> obj, const Point &pt) {
  std::shared_ptr<Tower> pTower = find(pt);
  // 对象离开灯塔的监控范围
  pTower->leave(obj);

  // 如果对象有视野，则取消之前设置的观察者
  int range = obj->range();
  if (range > 0) {
    // 首先计算出对象视野范围内的灯塔
    auto area = vision(pt, range);
    for (int x = area.x(); x <= area.x() + area.width(); ++x) {
      for (int y = area.y(); y <= area.y() + area.height(); ++y) {
        // 取消观察者绑定
        towers_[static_cast<size_t>(x + y * area_.width())]->watch(obj, false);
      }
    }
  }

  return true;
}

bool TowerAoi::update(std::shared_ptr <Object> obj, const Point &old, const Point &cur) {
  std::shared_ptr <Tower> pOldTower = find(old);
  std::shared_ptr <Tower> pCurTower = find(cur);
  // 对象所属灯塔发生了变化
  if (*pOldTower != *pCurTower) {
    // 从旧灯塔移除
    pOldTower->leave(obj);
    // 添加到新灯塔
    pCurTower->enter(obj);
  }

  // 如果对象有视野，则还需要检测下视野内的灯塔是否发生变化
  int range = obj->range();
  if (range > 0) {
    auto old_area = vision(old, range);
    auto cur_area = vision(cur, range);
    // 视野内的灯塔发生了变化
    if (old_area != cur_area) {
      // 在旧的视野范围内但是不在新的视野范围的灯塔要取消观察者设置
      for (int x = old_area.x(); x <= old_area.x() + old_area.width(); ++x) {
        for (int y = old_area.y(); y <= old_area.y() + old_area.height(); ++y) {
          if (!cur_area.contains(x, y)) {
            // 取消观察者绑定
            towers_[static_cast<size_t>(x + y * area_.width())]->watch(obj, false);
          }
        }
      }

      // 在新的视野范围内但是不在旧的视野范围的灯塔要设置观察者
      for (int x = cur_area.x(); x <= cur_area.x() + cur_area.width(); x++) {
        for (int y = cur_area.y(); y <= cur_area.y() + cur_area.height(); y++) {
          if (!old_area.contains(x, y)) {
            // 绑定对象为灯塔的观察者
            towers_[static_cast<size_t>(x + y * area_.width())]->watch(obj, true);
          }
        }
      }
    }
  }

  return true;
}

std::shared_ptr<Tower> TowerAoi::find(int x, int y) {
  int diffX = x - area_.x();
  if (diffX < 0)
    diffX = 0;
  int diffY = y - area_.y();
  if (diffY < 0)
    diffY = 0;

  // 和初始化构造灯塔AOI一样，用灯塔边长来计算灯塔坐标
  int edge = 2 * Config::AOI_RECOGNIZE_RANGE + 1;
  int tx = static_cast<int>(std::floor(static_cast<float>(diffX) / edge));
  if (tx >= area_.width())
    tx = area_.width() - 1;

  int ty = static_cast<int>(std::floor(static_cast<float>(diffY) / edge));
  if (ty >= area_.height())
    ty = area_.height() - 1;

  return towers_[tx + ty * area_.width()];
}

std::shared_ptr<Tower> TowerAoi::find(const Point &pt) {
  return find(pt.x(), pt.y());
}

Rect TowerAoi::vision(int x, int y, int range) {
  auto pTower = find(x - range, y - range);
  Rect area(pTower->x(), pTower->y());
  pTower = find(x + range, y + range);
  area.width(pTower->x() - area.x());
  area.height(pTower->y() - area.y());
  return area;
}

Rect TowerAoi::vision(const Point &pt, int range) {
  return vision(pt.x(), pt.y(), range);
}
