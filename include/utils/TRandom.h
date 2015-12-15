#ifndef TRANDOM_H
#define TRANDOM_H

#include "Poco/Random.h"

class TRandom
{
public:
  TRandom() {}

  virtual ~TRandom() {}

  /** 随机布尔值*/
  inline bool nextBoolean() { return _rng.nextBool(); }

  /** 随机字节 */
  inline unsigned char nextByte() { return static_cast<unsigned char>(_rng.nextChar()); }

  /** 随机整数0~n */
  inline int nextInt(int n) { return _rng.next(n); }

  /** 随机整数offset~offset+n */
  int nextInt(int n, int offset) { return offset + _rng.next() % n; }

  /** 随机长整数 */
  long nextLong()
  {
    #ifdef _WIN64
      return (_rng.next() << 32) + _rng.next();
    #else
      return _rng.next();
    #endif
  }

protected:
  Poco::Random _rng;
};

TRandom RANDOM;

#endif // TRANDOM_H
