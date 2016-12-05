# -*- coding: utf-8 -*-

# 亚丁时间变化监视器

class GameTimeListener:
    def onMonthChanged(self, t):
        raise NotImplementedError

    def onDayChanged(self, t):
        raise NotImplementedError

    def onHourChanged(self, t):
        raise NotImplementedError

    def onMinuteChanged(self, t):
        raise NotImplementedError