# -*- coding: utf-8 -*-

import time,ctypes
from datetime import datetime
from server.utils.IntRange import IntRange

BASE_TIME_IN_MILLIS_REAL = 1057233600l

class GameTime():
    def __init__(self, time):
        '''
        保存UTC格式游戏时间
        :param time:
        '''
        self._time = time
        self._datetime = datetime.utcfromtimestamp(time)

    @classmethod
    def valueOf(cls, times):
        '''
        转化现实时间到游戏时间,游戏时间比现实时间快6倍,即游戏时间一天是4小时
        :param times:
        :return:
        '''
        t1 = times - BASE_TIME_IN_MILLIS_REAL
        if t1 < 0:
            raise Exception('时间参数异常')
        # 溢出变成有符号int
        t2 = ctypes.c_int32(int(t1 * 6)).value
        t3 = t2 % 3
        return cls(t2 - t3)

    @classmethod
    def fromSystemCurrentTime(cls):
        return cls.valueOf(time.time())

    def toTime(self):
        '''
        返回本地时间
        :return:时间(timestamp)
        '''
        return datetime.fromtimestamp(self._time).time()

    def isNight(self):
        '''
        游戏当前时间是否是晚上
        :return:True/False
        '''
        return IntRange.includes(self._datetime.hour, 6, 17)

    def toString(self):
        return self._datetime.strftime("%Y.%m.%d %a at %H.%M.%S %Z") + '(' + str(self._time) + ')'

if __name__ == '__main__':
    t = GameTime.fromSystemCurrentTime()
    print(t.toString())
