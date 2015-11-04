#ifndef TDICE_H
#define TDICE_H

#include "utils/TRandom.h"

//掷骰子
class TDice
{
public:
  TDice(int faces):_faces(faces) {}
  virtual ~TDice() {}

  /** 取回基础值 */
  inline int getFaces() { return _faces; }
  /** 单次随机值 */
  inline int roll() { return RANDOM.nextInt(_faces) + 1; }
  /** 多次随机值总和 */
  inline int roll(int counts)
  {
    int n = 0;
    for (int i = 0; i < counts; i++)
      n += roll();
    return n;
  }
private:
  int _faces; //基础值
};

#endif // TDICE_H
