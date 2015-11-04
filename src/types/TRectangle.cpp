#include "types/TPoint.h"
#include "types/TRectangle.h"

TRectangle::TRectangle(TRectangle& rect)
{
  set(rect);
}

TRectangle::TRectangle(int left, int top, int right, int bottom)
{
  set(left, top, right, bottom);
}

TRectangle::TRectangle()
{
  TRectangle(0, 0, 0, 0);
}

TRectangle::~TRectangle()
{
}

void TRectangle::set(TRectangle& rect)
{
  set(rect.getLeft(), rect.getTop(), rect.getRight(), rect.getBottom());
}

void TRectangle::set(int left, int top, int right, int bottom)
{
  m_left = left;
  m_top = top;
  m_right = right;
  m_bottom = bottom;
}

int TRectangle::getLeft()
{
  return m_left;
}

int TRectangle::getTop()
{
  return m_top;
}

int TRectangle::getRight()
{
  return m_right;
}

int TRectangle::getBottom()
{
  return m_bottom;
}

int TRectangle::getWidth()
{
  return m_right - m_left;
}

int TRectangle::getHeight()
{
  return m_bottom - m_top;
}

bool TRectangle::contains(int x, int y)
{
  return (m_left <= x && x <= m_right) && (m_top <= y && y <= m_bottom);
}

bool TRectangle::contains(TPoint& pt)
{
  return contains(pt.getX(), pt.getY());
}
