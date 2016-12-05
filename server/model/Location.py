# -*- coding: utf-8 -*-

import math,random
from server.types.Point import Point

class Location(Point):
    def __init__(self, pt = None, map = None):
        if not pt:
            Point.__init__(self)
        else:
            Point.__init__(self, pt._x, pt._y)

        if not map:
            self._map = map

    def __eq__(self, other):
        return other._map.getId() == self._map.getId() and other._x == self._x \
               and other._y == self._y

    def hashCode(self):
        return 7 * self._map.getId() + Point.hashCode(self)

    '''
    @classmethod
    def randomLocation(cls, baseLocation, min, max, isRandomTeleport):
        if min > max:
            raise Exception('min > max')
        if max <= 0:
            raise Exception(str(baseLocation.__dict__))

        newLocation = Location()
        newLocation._map = baseLocation._map

        llocX = baseLocation._x - max
        rlocX = baseLocation._x + max
        dlocY = baseLocation._y - max
        ulocY = baseLocation._y + max

        lmapX = baseLocation._map._worldTopLeftX
        rmapX = lmapX + baseLocation._map.getWidth()
        dmapY = baseLocation._map._worldTopLeftY
        umapY = dmapY + baseLocation._map.getHeight()

        if llocX < lmapX:
            llocX = lmapX
        if rlocX > rmapX:
            rlocX = rmapX

        if dlocY < dmapY:
            dlocY = dmapY
        if ulocY > umapY:
            ulocY = umapY

        diffX = rlocX - llocX
        diffY = ulocY - dlocY

        amax = math.pow(1 + max * 2, 2)
        amin = 0
        if min != 0:
            amin = math.pow(1 + (min - 1) * 2, 2)
        trialLimit = int(40 * amax / (amax - amin))

        trial = 0
        while True:
            if trial >= trialLimit:
                newLocation._x = baseLocation._x
                newLocation._y = baseLocation._y
                break

            trial += 1
            newX = llocX + random.randrange(diffX + 1)
            newY = dlocY + random.randrange(diffY + 1)

            newLocation._x = newX
            newLocation._y = newY

            if baseLocation.getTileLineDistance(newLocation) < min:
                continue

            if isRandomTeleport:
                # todo
                pass

            if baseLocation._map.isInMap(Point(newX, newY)) and baseLocation._map.isPassable(Point(newX, newY)):
                break

        return newLocation
    '''