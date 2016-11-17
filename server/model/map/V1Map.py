# -*- coding: utf-8 -*-
from ...types.Point import Point
from Map import Map

BITFLAG_IS_IMPASSABLE = 128

class V1Map(Map):
    def __init__(self, mapId, map, worldTopLeftX, worldTopLeftY,
                 underwater, markable, teleportable, escapable,
                 useResurrection, usePainwand, enabledDeathPenalty,
                 takePets, recallPets, usableItem, usableSkill):
        Map.__init__(self)
        self._mapId = mapId
        self._map = map
        self._worldTopLeftX = worldTopLeftX
        self._worldTopLeftY = worldTopLeftY
        self._worldBottomRightX = worldTopLeftX + len(map) - 1
        self._worldBottomRightY = worldTopLeftY + len(map[0]) - 1
        self._isUnderwater = underwater
        self._isMarkable = markable
        self._isTeleportable = teleportable
        self._isEscapable = escapable
        self._isUseResurrection = useResurrection
        self._isUsePainwand = usePainwand
        self._isEnabledDeathPenalty = enabledDeathPenalty
        self._isTakePets = takePets
        self._isRecallPets = recallPets
        self._isUsableItem = usableItem
        self._isUsableSkill = usableSkill

    def accessTile(self, pt):
        if self.isInMap(pt):
            return 0

        return self._map[pt._x - self._worldTopLeftX][pt._y - self._worldTopLeftY]

    def accessOriginalTile(self, pt):
        return self.accessTile(pt) & (~BITFLAG_IS_IMPASSABLE)

    def setTile(self, pt, tile):
        if self.isInMap(pt):
            return
        self._map[pt._x - self._worldTopLeftX][pt._y - self._worldTopLeftY] = tile

    def getWidth(self):
        return self._worldBottomRightX - self._worldTopLeftX + 1

    def getHeight(self):
        return self._worldBottomRightY - self._worldTopLeftY + 1

    def getTile(self, pt):
        tile = self._map[pt._x - self._worldTopLeftX][pt._y - self._worldTopLeftY]
        if 0 != (tile & BITFLAG_IS_IMPASSABLE):
            return 300

        return self.accessOriginalTile(pt)

    def getOriginalTile(self, pt):
        return self.accessOriginalTile(pt)

    def isInMap(self, pt):
        if self._mapId == 4 and (pt._x < 32520 or pt._y < 32070 or (pt._y < 32190 and pt._x < 33950)):
            return False

        return (self._worldTopLeftX <= pt._x and pt._x <= self._worldBottomRightX
                and self._worldTopLeftY <= pt._y and pt._y <= self._worldBottomRightY)

    def isPassable(self, pt, heading = None):
        if not heading:
            return self._isPassable(Point(pt._x, pt._y - 1), 4) \
                   or self._isPassable(Point(pt._x + 1, pt._y), 6) \
                   or self._isPassable(Point(pt._x, pt._y + 1), 0) \
                   or self._isPassable(Point(pt._x - 1, pt._y), 2)
        else:
            self._isPassable(pt, heading)

    def _isPassable(self, pt, heading):
        tile1 = self.accessTile(pt)

        if (heading == 0):
            tile2 = self.accessTile(Point(pt._x, pt._y - 1))
        elif (heading == 1):
            tile2 = self.accessTile(Point(pt._x + 1, pt._y - 1))
        elif (heading == 2):
            tile2 = self.accessTile(Point(pt._x + 1, pt._y))
        elif (heading == 3):
            tile2 = self.accessTile(Point(pt._x + 1, pt._y + 1))
        elif (heading == 4):
            tile2 = self.accessTile(Point(pt._x, pt._y + 1))
        elif (heading == 5):
            tile2 = self.accessTile(Point(pt._x - 1, pt._y + 1))
        elif (heading == 6):
            tile2 = self.accessTile(Point(pt._x - 1, pt._y))
        elif (heading == 76):
            tile2 = self.accessTile(Point(pt._x - 1, pt._y - 1))
        else:
            return False

        if (tile2 & BITFLAG_IS_IMPASSABLE) == BITFLAG_IS_IMPASSABLE:
            return False

        if heading == 0:
            return (tile1 & 0x02) == 0x02
        elif heading == 1:
            tile3 = self.accessTile(Point(pt._x, pt._y - 1))
            tile4 = self.accessTile(Point(pt._x + 1, pt._y))
            return (tile3 & 0x01) == 0x01 or (tile4 & 0x02) == 0x02
        elif heading == 2:
            return (tile1 & 0x01) == 0x01
        elif heading == 3:
            tile3 = self.accessTile(Point(pt._x, pt._y + 1))
            return (tile3 & 0x01) == 0x01
        elif heading == 4:
            return (tile2 & 0x02) == 0x02
        elif heading == 5:
            return (tile2 & 0x01) == 0x01 or (tile2 & 0x02) == 0x02
        elif heading == 6:
            return (tile2 & 0x01) == 0x01
        elif heading == 7:
            tile3 = self.accessTile(Point(pt._x - 1, pt._y))
            return (tile3 & 0x02) == 0x02

        return False

    def setPassable(self, pt, isPassable):
        if isPassable:
            self.setTile(pt, self.accessTile(pt) & (~BITFLAG_IS_IMPASSABLE))
        else:
            self.setTile(pt, self.accessTile(pt) | BITFLAG_IS_IMPASSABLE)

    def isSafetyZone(self, pt):
        tile = self.accessOriginalTile(pt)
        return (tile & 0x30) == 0x10

    def isCombatZone(self, pt):
        tile = self.accessOriginalTile(pt)
        return (tile & 0x30) == 0x20

    def isNormalZone(self, pt):
        tile = self.accessOriginalTile(pt)
        return (tile & 0x30) == 0x00

    def isArrowPassable(self, pt, heading = None):
        if not heading:
            return (self.accessOriginalTile(pt) & 0x0e) != 0
        else:
            tile1 = self.accessTile(pt)
            newX, newY = 0,0
            if heading == 0:
                newX = pt._x
                newY = pt._y - 1
                tile2 = self.accessTile(Point(newX, newY))
            elif heading == 1:
                newX = pt._x + 1
                newY = pt._y - 1
                tile2 = self.accessTile(Point(newX, newY))
            elif heading == 2:
                newX = pt._x + 1
                newY = pt._y
                tile2 = self.accessTile(Point(newX, newY))
            elif heading == 3:
                newX = pt._x + 1
                newY = pt._y + 1
                tile2 = self.accessTile(Point(newX, newY))
            elif heading == 4:
                newX = pt._x
                newY = pt._y + 1
                tile2 = self.accessTile(Point(newX, newY))
            elif heading == 5:
                newX = pt._x - 1
                newY = pt._y + 1
                tile2 = self.accessTile(Point(newX, newY))
            elif heading == 6:
                newX = pt._x - 1
                newY = pt._y
                tile2 = self.accessTile(Point(newX, newY))
            elif heading == 7:
                newX = pt._x - 1
                newY = pt._y - 1
                tile2 = self.accessTile(Point(newX, newY))
            else:
                return False

            if self.isExistDoor(Point(newX, newY)):
                return False

            if heading == 0:
                return (tile1 & 0x08) == 0x08
            elif heading == 1:
                tile3 = self.accessTile(Point(pt._x, pt._y - 1))
                tile4 = self.accessTile(Point(pt._x + 1, pt._y))
                return (tile3 & 0x04) == 0x04 or (tile4 & 0x08) == 0x08
            elif heading == 2:
                return (tile1 & 0x04) == 0x04
            elif heading == 3:
                tile3 = self.accessTile(Point(pt._x, pt._y + 1))
                return (tile3 & 0x04) == 0x04
            elif heading == 4:
                return (tile2 & 0x08) == 0x08
            elif heading == 5:
                return (tile2 & 0x04) == 0x04 or (tile2 & 0x08) == 0x08
            elif heading == 6:
                return (tile2 & 0x04) == 0x04
            elif heading == 7:
                tile3 = self.accessTile(Point(pt._x - 1, pt._y))
                return (tile3 & 0x08) == 0x08
            else:
                return False

    def isFishingZone(self, pt):
        return self.accessOriginalTile(pt) == 16

    def isExistDoor(self, pt):
        return False