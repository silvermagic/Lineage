# -*- coding: utf-8 -*-

class Map():
    def __init__(self):
        self._mapId = 0
        self._worldTopLeftX = 0
        self._worldTopLeftY = 0
        self._worldBottomRightX = 0
        self._worldBottomRightY = 0
        self._map = None
        self._isUnderwater = False
        self._isMarkable = False
        self._isTeleportable = False
        self._isEscapable = False
        self._isUseResurrection = False
        self._isUsePainwand = False
        self._isEnabledDeathPenalty = False
        self._isTakePets = False
        self._isRecallPets = False
        self._isUsableItem = False
        self._isUsableSkill = False

    def getTile(self, pt):
        return 0

    def getOriginalTile(self, pt):
        return 0

    def isInMap(self, pt):
        return False

    def isPassable(self, pt, heading = None):
        return False

    def setPassable(self, pt, isPassable):
        return False

    def isSafetyZone(self, pt):
        return False

    def isCombatZone(self, pt):
        return False

    def isNormalZone(self, pt):
        return False

    def isArrowPassable(self, pt, heading = None):
        return False

    def isFishingZone(self, pt):
        return False

    def isExistDoor(self, pt):
        return False

    def isNull(self):
        return True