//
// Created by 范炜东 on 2019/6/19.
//

#ifndef PROJECT_TOWERAOI_H
#define PROJECT_TOWERAOI_H

#pragma once

#include <memory>
#include <mutex>
#include <vector>
#include "Rect.h"

class Tower;
class Object;
class TowerAoi
{
public:
  TowerAoi(int id, int x, int y, int width, int height);
  virtual ~TowerAoi();

  // 将游戏坐标系按灯塔视野分割并构建灯塔AOI游戏坐标系
  void initialize();

  // 对象进入灯塔系统(输入坐标为游戏坐标)
  bool enter(std::shared_ptr<Object> obj, const Point &pt);

  // 对象离开灯塔系统(输入坐标为游戏坐标)
  bool leave(std::shared_ptr<Object> obj, const Point &pt);

  // 更新灯塔系统中的对象(输入坐标为游戏坐标)
  bool update(std::shared_ptr<Object> obj, const Point &old, const Point &cur);

  // 根据游戏坐标计算所属灯塔
  std::shared_ptr<Tower> find(int x, int y);
  std::shared_ptr<Tower> find(const Point &pt);

protected:
  // 获取坐标AOI所涉及的灯塔区域
  Rect vision(int x, int y, int range);
  Rect vision(const Point &pt, int range);

protected:
  int id_; // AOI编号
  Rect area_; // 灯塔坐标系区域
  std::vector<std::shared_ptr<Tower>> towers_; // 灯塔AOI坐标系统
};

#endif //PROJECT_TOWERAOI_H
