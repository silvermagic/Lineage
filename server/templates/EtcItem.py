# -*- coding: utf-8 -*-

from Item import Item

class EtcItem(Item):
    def __init__(self):
        Item.__init__(self)
        self._stackable = False
        self._locx = 0
        self._locy = 0
        self._mapid = 0
        self._delay_id = 0
        self._delay_time = 0
        self._delay_effect = 0
        self._maxChargeCount = 0
        self._isCanSeal = False

    def isStackable(self):
        return self._stackable

    def get_locx(self):
        return self._locx

    def get_locy(self):
        return self._locy

    def get_mapid(self):
        return self._mapid

    def get_delayid(self):
        return self._delay_id

    def get_delaytime(self):
        return self._delay_time

    def getMaxChargeCount(self):
        return self._delay_effect

    def isCanSeal(self):
        return self._isCanSeal