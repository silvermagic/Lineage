//
// Created by 范炜东 on 2019/6/24.
//

#ifndef PROJECT_RECT_H
#define PROJECT_RECT_H

#include "Point.h"

class Rect {
public:
  Rect(int x, int y, int width = 0, int height = 0);
  Rect(const Point &pt, int width = 0, int height = 0);

  // 判断点是否位于矩形内
  bool contains(int x, int y);
  bool contains(const Point &pt);

  // 等值运算符重载
  bool operator==(const Rect& r);
  bool operator!=(const Rect& r);

  // 返回坐标的字符串表示
  virtual std::string toString();

  // 返回矩形的左下角X轴坐标
  int x() const;
  void x(int value);

  // 返回矩形的左下角X轴坐标
  int y() const;
  void y(int value);

  // 返回矩形的宽
  int width() const;
  void width(int value);

  // 返回矩形的高
  int height() const;
  void height(int value);

protected:
  int x_, y_, width_, height_;
};

#endif //PROJECT_RECT_H
