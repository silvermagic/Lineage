#ifndef TINTRANGE_H_INCLUDED
#define TINTRANGE_H_INCLUDED

#include <boost/format.hpp>
#include "utils/TRandom.h"

class TIntRange
{
public:
  TIntRange(int low, int high) : _low(low), _high(high) {}

  TIntRange(const TIntRange& range)
  {
    TIntRange(range._low, range._high);
  }

  static inline int ensure(int n, int low, int high)
  {
    int r = n;
    r = (low <= r) ? r : low;
    r = (r <= high) ? r : high;
    return r;
  }

  static inline  bool includes(int i, int low, int high)
  {
    return (low <= i) && (i <= high);
  }

  inline int ensure(int i)
  {
    int r = i;
    r = (_low <= r) ? r : _low;
    r = (r <= _high) ? r : _high;
    return r;
  }

  inline bool equals(const TIntRange& range)
  {
    return (_low == range._low) && (_high == range._high);
  }

  inline int getHigh()
  {
    return _high;
  }

  inline int getLow()
  {
    return _low;
  }

  inline int getWidth()
  {
    return _high - _low;
  }

  inline bool includes(int i)
  {
    return (_low <= i) && (i <= _high);
  }

  inline int randomValue()
  {
    return RANDOM.nextInt(getWidth() + 1) + _low;
  }

  std::string toString()
  {
    return (boost::format("low=%d, high=%d") % _low % _high).str();
  }

private:
  int _low, _high;
};

#endif // TINTRANGE_H_INCLUDED
