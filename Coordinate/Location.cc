//
// Created by 范炜东 on 2019/6/19.
//

#include <cmath>
#include <boost/format.hpp>
#include "Common.h"
#include "Map.h"
#include "WorldMap.h"
#include "Location.h"

Location::Location(int id): id_(id)
{
}

Location::Location(int id, int x, int y): Point(x, y), id_(id)
{
}

bool Location::operator==(const Location& loc)
{
  return (loc.id() == id_ && loc.x() == x_ && loc.y() == y_);
}

std::shared_ptr<Map> Location::map()
{
  return map_;
}

int Location::id() const
{
  return id_;
}

void Location::id(int value)
{
  id_ = value;
  map_ = WorldMap::instance()[id_];
}

Location Location::randomMovement(int max, bool isRandomTeleport)
{
  return randomMovement(0, max, isRandomTeleport);
}

Location Location::randomMovement(int min, int max, bool isRandomTeleport)
{
  if (min > max)
    throw std::invalid_argument("Location::random() min > max.");

  if (max <= 0)
    return std::move(Location(x_, y_, id_));

  // 设置新坐标所属地图
  Location loc(id_);

  // 计算X轴和Y轴随机范围
  int x_range[] = {x_ - max, x_ + max};
  int y_range[] = {y_ - max, y_ + max};
  int x_map_range[] = {map_->x(), map_->x() + map_->width()};
  int y_map_range[] = {map_->y(), map_->y() + map_->height()};
  if (x_range[0] < x_map_range[0])
    x_range[0] = x_map_range[0];
  if (x_range[1] > x_map_range[1])
    x_range[1] = x_map_range[1];
  if (y_range[0] < y_map_range[0])
    y_range[0] = y_map_range[0];
  if (y_range[1] > y_map_range[1])
    y_range[1] = y_map_range[1];
  int diffX = x_range[1] - x_range[0];
  int diffY = y_range[1] - y_range[0];

  // 限制随机尝试次数
  int trial = 0;
  int trial_max = std::pow(1 + (max * 2), 2);
  int trial_min = (min == 0) ? 0 : std::pow(1 + ((min - 1) * 2), 2);
  int limit = 40 * trial_min / (trial_max - trial_min);
  while (true)
  {
    if (trial >= limit)
    {
      loc.x(x_);
      loc.y(y_);
      break;
    }
    trial++;

    int x = x_range[0] + random(diffX + 1);
    int y = y_range[0] + random(diffY + 1);
    loc.x(x);
    loc.y(y);

    if (getTileLineDistance(loc) < min)
      continue;

    if (isRandomTeleport)
    {
      // TODO: 随机传送场合
    }

    if (map_->isInMap(x, y) && map_->isPassable(x, y))
      break;
  }

  return std::move(loc);
}


std::string Location::toString()
{
  return std::move((boost::format("(%1, %2) on %3") % x_ % y_ % id_).str());
}