# -*- coding: utf-8 -*-

class IntRange():
    @classmethod
    def includes(cls, i, low, high):
        return (low <= i) and (i <= high)

    @classmethod
    def ensure(cls, n, low, high):
        if n < low:
            return low
        if n > high:
            return high
        return n
