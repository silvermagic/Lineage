#ifndef TPERFORMANCETIMER_H
#define TPERFORMANCETIMER_H

#include "Poco/Timestamp.h"

using Poco::Timestamp;

class TPerformanceTimer
{
public:
	TPerformanceTimer() {}
	virtual ~TPerformanceTimer() {}

	//运行时间:微秒
	long elapsedTimeMicros()
	{
		return _begin.elapsed();
	}

	//运行时间:毫秒
	long elapsedTimeMillis()
	{
		return _begin.elapsed() / 1000;
	}

	//运行时间:纳秒
	long elapsedTimeNanos()
	{
		return _begin.elapsed() * 1000;
	}

	//重置运行时间
	void reset()
	{
		_begin.update();
	}

protected:
	Timestamp _begin;
};

#endif // TPERFORMANCETIMER_H
