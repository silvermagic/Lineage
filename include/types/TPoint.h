#ifndef TPOINT_H
#define TPOINT_H

#include <string>

class TPoint
{
public:
  TPoint();
  TPoint(int x, int y);
  TPoint(const TPoint& pt);
  virtual ~TPoint();

  /** Point朝着北、东北、东、东南、南、西南、西、西北(0-7)方向后退一格 */
  void backward(int heading);
  /** 判断两点是否处于同一位置 */
  bool equals(const TPoint& pt);
  /** Point朝着北、东北、东、东南、南、西南、西、西北(0-7)方向前进一格 */
  void forward(int heading);

  /** 计算两点之间的直线距离 */
  double getLineDistance(const TPoint& pt);
  /** 取得与另一个点间的X轴或Y轴距离较大值 */
  int getTileLineDistance(const TPoint& pt);
  /** 取得与另一个点间的X轴+Y轴的距离 */
  int getTileDistance(const TPoint& pt);
  /** 取得点的X轴值 */
  int getX();
  /** 取得点的Y轴值 */
  int getY();

  /** 获取对象的hash值 */
  int hashCode();

  /** 判断两点是否处于同一画面 */
  bool isInScreen(const TPoint& pt);
  /** 判断两点是否处于同一位置 */
  bool isSamePoint(const TPoint& pt);

  /** 设定点的X轴值 */
  void setX(int x);
  /** 设定点的Y轴值 */
  void setY(int y);
  void set(const TPoint& pt);
  void set(int x, int y);

  std::string toString();
protected:
  int _x, _y;
private:
  //Point朝着北、东北、东、东南、南、西南、西、西北(0-7)方向移动一格时x/y轴的变化
  static int HEADING_TABLE_X[8];
  static int HEADING_TABLE_Y[8];
};

#endif // TPOINT_H
