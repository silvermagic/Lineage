# -*- coding: utf-8 -*-

from ..utils.IntRange import IntRange

KARMA_POINT = [10000, 20000, 100000, 500000, 1500000, 3000000, 5000000, 10000000, 15500000]

class Karma():
    def __init__(self):
        self._karma = 0

    def set(self, i):
        self._karma = IntRange.ensure(i, -15500000, 15500000)

    def add(self, i):
        self._karma = IntRange.ensure(self._karma + i, -15500000, 15500000)

    def getLevel(self):
        isMinus = False
        karmaLevel = 0

        karma = self._karma
        if karma < 0:
            isMinus = True
            karma *= -1

        for point in KARMA_POINT:
            if karma >= point:
                karmaLevel += 1
                if karmaLevel >= 8:
                    break
            else:
                break

        if isMinus:
            karmaLevel *= -1

        return karmaLevel

    def getPercent(self):
        karma = self._karma
        karmaLevel = self.getLevel()
        if karmaLevel == 0:
            return 0

        if karma < 0:
            karma *= -1
            karmaLevel *= -1

        return int(100 * (karma - KARMA_POINT[karmaLevel - 1]) / (KARMA_POINT[karmaLevel] - KARMA_POINT[karmaLevel - 1]))
