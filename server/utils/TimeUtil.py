# -*- coding: utf-8 -*-

import time
from datetime import datetime

class TimeUtil():
    @classmethod
    def dt2ts(cls, dt):
        '''
        转化datetime格式为timestamp格式
        :param dt:日期(datetime)
        :return:日期(timestamp)
        '''
        if not dt:
            dt = datetime.now()
        return time.mktime(dt.timetuple())

    @classmethod
    def ts2dt(cls, ts):
        '''
        转化timestamp格式为datetime格式
        :param ts:日期(timestamp)
        :return:日期(datetime)
        '''
        if ts < 0:
            ts = 0
        return datetime.fromtimestamp(ts)