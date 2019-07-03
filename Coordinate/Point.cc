//
// Created by 范炜东 on 2019/5/15.
//

#include <boost/format.hpp>
#include "Point.h"

static const int MOVE_TABLE_X[] = { 0, 1, 1, 1, 0, -1, -1, -1 };
static const int MOVE_TABLE_Y[] = { -1, -1, 0, 1, 1, 1, 0, -1 };

Point::Point(): x_(0), y_(0)
{
}

Point::Point(int x, int y): x_(x), y_(y)
{
}

void Point::backward(int t)
{
  x_ -= MOVE_TABLE_X[t];
  y_ -= MOVE_TABLE_Y[t];
}

void Point::forward(int t)
{
  x_ += MOVE_TABLE_X[t];
  y_ += MOVE_TABLE_Y[t];
}

double Point::getLineDistance(const Point& pt)
{
  int diffX = pt.x() - x_;
  int diffY = pt.y() - y_;
  return std::sqrt(diffX * diffX + diffY * diffY);
}

int Point::getTileDistance(const Point& pt)
{
  int diffX = pt.x() - x_;
  int diffY = pt.y() - y_;
  return std::max(std::abs(diffX), std::abs(diffY));
}

int Point::getTileLineDistance(const Point& pt)
{
  int diffX = pt.x() - x_;
  int diffY = pt.y() - y_;
  return std::abs(diffX) + std::abs(diffY);
}

bool Point::isInScreen(const Point& pt)
{
  int dist = getTileDistance(std::forward<const Point>(pt));
  // 首先使用平行距离进行判断，过滤掉那些太远影响近似计算的点
  if (dist > 17)
  {
    return false;
  }
  else if (dist <= 13) // 简化判断
  {
    return true;
  }
  else
  {
    // 判断两点间的直线距离是否在范围内的近似算法，首先以当前坐标为原点建立坐标系，
    // 然后计算沿着X轴和Y轴移动到目标的距离
    int diffX = pt.x() - (x_ - 15);
    int diffY = pt.y() - (y_ - 15);
    int dist = std::abs(diffX) + std::abs(diffY);
    if (17 <= dist && dist <= 43)
      return true;
  }

  return false;
}

bool Point::operator==(const Point& pt)
{
  return (pt.x() == x_ && pt.y() == y_);
}

bool Point::operator!=(const Point& pt)
{
  return (pt.x() != x_ || pt.y() != y_);
}

std::string Point::toString()
{
  return std::move((boost::format("(%1, %2)") % x_ % y_).str());
}

int Point::x() const
{
  return x_;
}

void Point::x(int x)
{
  x_ = x;
}

int Point::y() const
{
  return y_;
}

void Point::y(int y)
{
  y_ = y;
}

