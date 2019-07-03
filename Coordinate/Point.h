//
// Created by 范炜东 on 2019/5/15.
//

#ifndef PROJECT_POINT_H
#define PROJECT_POINT_H

#include <string>

class Point {
public:
  Point();
  Point(int, int);

  // 向后移动
  void backward(int t);

  // 向前移动
  void forward(int t);

  // 计算到目标的直线距离
  double getLineDistance(const Point& pt);

  // 计算到目标投影到X轴和Y轴后的距离
  int getTileDistance(const Point& pt);

  // 计算到目标的最大平行距离, 即到目标的X轴和Y轴投影距离中的较大者
  int getTileLineDistance(const Point& pt);

  // 如果返回指定坐标在屏幕中是否可见。玩家坐标为(0, 0)，则可见范围的坐标为左上(-2, 15)右上(15, -2)左下(-15, 2)右下(2, -15)，被聊天文本框遮挡的不可见的部分也包含在屏幕中
  bool isInScreen(const Point& pt);

  // 等值运算符重载
  bool operator==(const Point& pt);
  bool operator!=(const Point& pt);

  // 返回坐标的字符串表示
  virtual std::string toString();

  // 获取/设置坐标的X轴坐标
  int x() const;
  virtual void x(int x);

  // 获取/设置坐标的Y轴坐标
  int y() const;
  virtual void y(int y);

protected:
  int x_, y_;
};

#endif //PROJECT_POINT_H
