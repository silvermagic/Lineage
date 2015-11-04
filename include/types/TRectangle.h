#ifndef TRECTANGLE_H
#define TRECTANGLE_H

class TPoint;

class TRectangle
{
public:
  TRectangle(TRectangle& rect);
  TRectangle(int left, int top, int right, int bottom);
  TRectangle();
  virtual ~TRectangle();

  //设置/获取成员变量
  void set(TRectangle& rect);
  void set(int left, int top, int right, int bottom);
  int getLeft();
  int getTop();
  int getRight();
  int getBottom();
  int getWidth();
  int getHeight();
  
  //判断点是否被包含在矩形中
  bool contains(int x, int y);
  bool contains(TPoint& pt);
private:
  int m_left, m_top;
  int m_right, m_bottom;
};

#endif // TRECTANGLE_H
