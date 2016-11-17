# -*- coding: utf-8 -*-

import math

HEADING_TABLE_X = (0, 1, 1, 1, 0, -1, -1, -1)
HEADING_TABLE_Y = (-1, -1, 0, 1, 1, 1, 0, -1)

class Point():

    def __init__(self, x = None, y = None):
        self._x = 0
        self._y = 0

        if x:
            self._x = x

        if y:
            self._y = y

    def set(self, x, y):
        self._x = x
        self._y = y

    def forward(self, heading):
        self._x += HEADING_TABLE_X[heading]
        self._y += HEADING_TABLE_Y[heading]

    def backward(self, heading):
        self._x -= HEADING_TABLE_X[heading]
        self._y -= HEADING_TABLE_Y[heading]

    def getLineDistance(self, pt):
        diffX = pt._x - self._x
        diffY = pt._y - self._y
        return math.sqrt(diffX * diffX + diffY * diffY)

    def getTileLineDistance(self, pt):
        return max(math.fabs(pt._x - self._x), math.fabs(pt._y - self._y))

    def getTileDistance(self, pt):
        return math.fabs(pt._x - self._x) + math.fabs(pt._y - self._y)

    def isInScreen(self, pt):
        dist = self.getTileDistance(pt)

        if dist > 17:
            return False
        elif dist <= 13:
            return True
        else:
            dist = math.fabs(pt._x - (self._x - 15)) + math.fabs(pt._y - (self._y - 15))
            if 17 <= dist and dist <= 43:
                return True
            return False

    def __eq__(self, other):
        return other._x == self._x and other._y == self._y

    def hashCode(self):
        return 7 * self._x + self._y