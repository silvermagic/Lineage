#ifndef TRANDOM_H
#define TRANDOM_H

#include <ctime>
#include <boost/random/mersenne_twister.hpp>

class TRandom
{
public:
  TRandom() { _rng.seed(std::time(0)); }
  
  virtual ~TRandom() {}

  /** 随机布尔值*/
  inline bool nextBoolean() { return _rng() % 2 ? true : false; }

  /** 随机字节 */
  inline unsigned char nextByte() { return static_cast<unsigned char>(nextInt(256)); }

  /** 随机整数0~n */
  inline int nextInt(int n) { return _rng() % n; }

  /** 随机整数offset~offset+n */
  int nextInt(int n, int offset) { return offset + _rng() % n; }

  /** 随机长整数 */
  long nextLong()
  {
    #ifdef _WIN64
      return (_rng() << 32) + _rng();
    #else
      return _rng();
    #endif
  }

protected:
  boost::random::mt19937 _rng;
};

TRandom RANDOM;

#endif // TRANDOM_H
