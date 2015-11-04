#include <algorithm>
#include <cmath>
#include <boost/format.hpp>
#include "types/TPoint.h"

int TPoint::HEADING_TABLE_X[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int TPoint::HEADING_TABLE_Y[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };

TPoint::TPoint()
{
}

TPoint::TPoint(int x, int y)
{
  _x = x;
  _y = y;
}

TPoint::TPoint(const TPoint& pt)
{
  _x = pt._x;
  _y = pt._y;
}

TPoint::~TPoint()
{
}

void TPoint::backward(int heading)
{
  _x -= HEADING_TABLE_X[heading];
  _y -= HEADING_TABLE_Y[heading];
}

bool TPoint::equals(const TPoint& pt)
{
  return ((pt._x == _x) && (pt._y == _y));
}

void TPoint::forward(int heading)
{
  _x += HEADING_TABLE_X[heading];
  _y += HEADING_TABLE_Y[heading];
}

double TPoint::getLineDistance(const TPoint& pt)
{
  long diffX = pt._x - _x;
  long diffY = pt._y - _y;
  return sqrt((diffX * diffX) + (diffY * diffY));
}

int TPoint::getTileLineDistance(const TPoint& pt)
{
  return std::max(std::abs(pt._x - _x), std::abs(pt._y - _y));
}

int TPoint::getTileDistance(const TPoint& pt)
{
  return std::abs(pt._x - _x) + std::abs(pt._y - _y);
}

int TPoint::getX()
{
  return _x;
}

int TPoint::getY()
{
  return _y;
}

int TPoint::hashCode()
{
  return 7 * _x + _y;
}

bool TPoint::isInScreen(const TPoint& pt)
{
  int dist = getTileDistance(pt);

  if(dist > 19) {
    return false;
  } else if(dist <= 18) {
    return true;
  } else {
    int dist2 = std::abs(pt._x - (_x - 18)) + std::abs(pt._y - (_y - 18));
    if((19 <= dist2) && (dist2 <= 52)) {
      return true;
    }
    return false;
  }
}

bool TPoint::isSamePoint(const TPoint& pt)
{
  return ((pt._x == _x) && (pt._y == _y));
}

void TPoint::setX(int x)
{
  _x = x;
}

void TPoint::setY(int y)
{
  _y = y;
}

void TPoint::set(const TPoint& pt)
{
  _x = pt._x;
  _y = pt._y;
}

void TPoint::set(int x, int y)
{
  _x = x;
  _y = y;
}

std::string TPoint::toString()
{
  return (boost::format("(%d, %d)") % _x % _y).str();
}
