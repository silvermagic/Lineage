# -*- coding: utf-8 -*-

import time
from datetime import datetime

class TimeUtil():
    @classmethod
    def dt2ts(cls, dt):
        return time.mktime(dt.timetuple())

    @classmethod
    def ts2dt(cls, ts):
        return datetime.fromtimestamp(ts)