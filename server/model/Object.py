# -*- coding: utf-8 -*-

from Location import Location

class Object():
    def __init__(self):
        self._id = 0
        self._loc = Location()

    def getLineDistance(self, obj):
        return self._loc.getLineDistance(obj._loc)

    def getTileLineDistance(self, obj):
        return self._loc.getTileLineDistance(obj._loc)


    def getTileDistance(self, obj):
        return self._loc.getTileDistance(obj._loc)

    def onPerceive(self, perceivedFrom):
        return

    def onAction(self, actionFrom):
        return

    def onTalkAction(self, talkFrom):
        return
