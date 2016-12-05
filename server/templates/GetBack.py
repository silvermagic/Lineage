# -*- coding: utf-8 -*-

class GetBack():
    def __init__(self):
        self._areaX1 = 0
        self._areaY1 = 0
        self._areaX2 = 0
        self._areaY2 = 0
        self._areaMapId = 0
        self._getbackX1 = 0
        self._getbackY1 = 0
        self._getbackX2 = 0
        self._getbackY2 = 0
        self._getbackX3 = 0
        self._getbackY3 = 0
        self._getbackMapId = 0
        self._getbackTownId = 0
        self._getbackTownIdForElf = 0
        self._getbackTownIdForDarkelf = 0
        self._escapable = False

    def isSpecifyArea(self):
        return (self._areaX1 != 0 and self._areaY1 != 0 and self._areaX2 != 0 and self._areaY2 != 0)