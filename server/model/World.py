# -*- coding: utf-8 -*-

import cmath
from Config import Config
from server.utils.Singleton import Singleton

MAX_MAP_ID = 8105

class World():
    __metaclass__ = Singleton
    def __init__(self):
        self._allPlayers = {}
        self._allObjects = {}
        self._visibleObjects= {}
        self._weather = 4
        self._allValues = []

    def storeObject(self, obj):
        '''
        保存游戏对象
        :param obj:游戏对象(Object)
        :return:None
        '''
        from server.model.Instance.PcInstance import PcInstance
        if not obj:
            raise Exception('None object')

        self._allObjects[obj._id] = obj
        if type(obj) == PcInstance:
            self._allPlayers[obj._name] = obj

    def removeObject(self, obj):
        '''
        移除游戏对象
        :param obj:游戏对象(Object)
        :return:None
        '''
        from server.model.Instance.PcInstance import PcInstance
        if not obj:
            raise Exception('None object')

        self._allObjects.pop(obj._id)
        if type(obj) == PcInstance:
            self._allPlayers.pop(obj._name)

    def findObject(self, id):
        '''
        根据对象ID寻找游戏对象
        :param id:游戏对象ID
        :return:游戏对象(Object)
        '''
        if self._allObjects.has_key(id):
            return self._allObjects[id]
        else:
            return None

    def addVisibleObject(self, obj):
        '''
        保存可见游戏对象
        :param obj:游戏对象
        :return:None
        '''
        mapId = obj._loc._map._mapId
        if mapId <= MAX_MAP_ID:
            if self._visibleObjects.has_key(mapId):
                self._visibleObjects[mapId][obj._id] = obj
            else:
                self._visibleObjects[mapId] = {obj._id: obj}

    def removeVisibleObject(self, obj):
        '''
        移除可见游戏对象
        :param obj:游戏对象
        :return:None
        '''
        mapId = obj._loc._map._mapId
        if mapId <= MAX_MAP_ID:
            if self._visibleObjects.has_key(mapId):
                if self._visibleObjects[mapId].has_key(obj._id):
                    self._visibleObjects[mapId].pop(obj._id)
                if len(self._visibleObjects[mapId]) == 0:
                    self._visibleObjects.pop(mapId)

    def moveVisibleObject(self, obj, newMapId):
        '''
        移动游戏对象到其他地图
        :param obj:游戏对象(Object)
        :param newMapId:新地图ID(int)
        :return:None
        '''
        mapId = obj._loc._map._mapId
        if mapId != newMapId:
            self.removeVisibleObject(obj)
            if newMapId <= MAX_MAP_ID:
                if self._visibleObjects.has_key(newMapId):
                    self._visibleObjects[newMapId][obj._id] = obj
                else:
                    self._visibleObjects[newMapId] = {obj._id: obj}

    # Bresenham画线算法
    def createLineMap(self, src, target):
        lineMap = {}
        x0 = src._loc._x
        y0 = src._loc._y
        x1 = target._loc._x
        y1 = target._loc._y
        sx = -1
        if x1 > x0:
            sx = 1
        dx = x0 - x1
        if x1 > x0:
            dx = x1 - x0
        sy = -1
        if y1 > y0:
            sy = 1
        dy = y0 - y1
        if y1 > y0:
            dy = y1 - y0

        x = x0
        y = y0
        if dx >= dy:
            E = -dx
            for i in range(dx + 1):
                key = (x << 16) + y
                lineMap[key] = key
                x += sx
                E += 2 * dy
                if E >= 0:
                    y += sy
                    E -= 2 * dx
        else:
            E = -dy
            for i in range(dy + 1):
                key = (x << 16) + y
                lineMap[key] = key
                y += sy
                E += 2 * dx
                if E >= 0:
                    x += sx
                    E -= 2 * dy

        return lineMap

    def getVisibleLineObjects(self, src, target):
        '''
        获取两个游戏对象间直线上的可见游戏对象
        :param src:起始游戏对象(Object)
        :param target:结束游戏对象(Object)
        :return:游戏对象集合(Object[])
        '''
        ret = []
        lineMap = self.createLineMap(src, target)

        mapId = target._loc._map._mapId
        if mapId <= MAX_MAP_ID:
            for item in self._visibleObjects[mapId].values():
                if item == src:
                    continue

                key = item._loc._x << 16 + item._loc._y
                if lineMap.has_key(key):
                    ret.append(item)

        return ret

    def getVisibleBoxObjects(self, obj, heading, width, height):
        '''
        获取对象正前方矩形范围的可见对象,以对象为中心,朝向为X正方向建立坐标系,将对象所在地图的游戏对象由
        当前坐标系转化到新坐标系中,然后判断是否在对应的矩形范围内
        :param obj:游戏对象(Object)
        :param heading:游戏对象朝向(int)
        :param width:宽度(int)
        :param height:高度(int)
        :return:游戏对象集合(Object[])
        '''
        ret = []
        headingRotate = [6, 7, 0, 1, 2, 3, 4, 5]
        cosSita = cmath.cos(headingRotate[heading] * cmath.pi / 4)
        sinSita = cmath.sin(headingRotate[heading] * cmath.pi / 4)

        mapId = obj._loc._map._mapId
        if mapId <= MAX_MAP_ID:
            for item in self._visibleObjects[mapId].values():
                if item == obj:
                    continue
                if mapId != item._loc._map._mapId:
                    continue
                if obj._loc == item._loc:
                    ret.append(item)
                    continue

                distance = obj._loc.getTileLineDistance(item._loc)
                if distance > height and distance > width:
                    continue

                xmin = 0
                xmax = height
                ymin = -width
                ymax = width
                diffx = item._loc._x - obj._loc._x
                diffy = item._loc._y - obj._loc._y
                rotX = round(diffx * cosSita + diffy * sinSita)
                rotY = round(-diffx * sinSita + diffy * cosSita)
                if rotX > xmin and distance <= xmax and rotY >= ymin and rotY <= ymax:
                    ret.append(item)

    def getVisibleObjects(self, obj, radius = -1):
        '''
        获取以游戏对象为中心的圆形范围内的游戏对象,这边实际上获取的是圆内切正方形范围内的游戏对象
        :param obj:游戏对象(Object)
        :param radius:半径(int)
        :return:游戏对象集合(Object[])
        '''
        ret = []
        mapId = obj._loc._map._mapId
        if mapId <= MAX_MAP_ID:
            for item in self._visibleObjects[mapId].values():
                if item == obj:
                    continue
                if mapId != item._loc._map._mapId:
                    continue

                if radius == -1:
                    if obj._loc.isInScreen(item._loc):
                        ret.append(item)
                elif radius == 0:
                    if obj._loc == item._loc:
                        ret.append(item)
                else:
                    if obj._loc.getTileLineDistance(item._loc) < radius:
                        ret.append(item)

        return ret

    def getVisiblePoint(self, loc, radius):
        '''
        获取地图某位置圆形范围内的游戏对象
        :param loc:游戏坐标(Location)
        :param radius:半径(int)
        :return:游戏对象集合(Object[])
        '''
        ret = []
        mapId = loc._mapId
        if mapId <= MAX_MAP_ID:
            for item in self._visibleObjects[mapId].values():
                if mapId != item._loc._mapId:
                    continue

                if loc.getTileLineDistance(item._loc) <= radius:
                    ret.append(item)

        return ret


    def getVisiblePlayer(self, obj, radius = -1):
        '''
        获取以游戏对象为中心的圆形范围内的游戏玩家,这边实际上获取的是圆内切正方形范围内的游戏对象
        :param obj:游戏对象(Object)
        :param radius:半径(int)
        :return:游戏玩家集合(Object[])
        '''
        ret = []
        mapId = obj._loc._map._mapId
        if mapId <= MAX_MAP_ID:
            for item in self._allPlayers[mapId].values():
                if obj == item:
                    continue

                if mapId != item._loc._mapId:
                    continue

                if radius == -1:
                    if obj._loc.isInScreen(item._loc):
                        ret.append(item)
                elif radius == 0:
                    if obj._loc == item._loc:
                        ret.append(item)
                else:
                    if obj._loc.getTileLineDistance(item._loc) < radius:
                        ret.append(item)

        return ret

    def getVisiblePlayerExceptTargetSight(self, obj, target):
        ret = []
        mapId = obj._loc._mapId

        for item in self._allPlayers.values():
            if item == obj:
                continue
            if mapId != item._loc._mapId:
                continue

            distance = Config.getint('server', 'PcRecognizeRange')
            if distance == -1:
                if obj._loc.isInScreen(item):
                    if target._loc.isInScreen(item):
                        ret.append(item)
            else:
                if obj._loc.getTileLineDistance(item) <= distance:
                    if target._loc.getTileLineDistance(item) > distance:
                        ret.append(item)

    def getRecognizePlayer(self, obj):
        return self.getVisiblePlayer(obj, Config.getint('server', 'PcRecognizeRange'))

    def getAllPlayers(self):
        return self._allPlayers.values()

    def getPlayer(self, name):
        if self._allPlayers.has_key(name):
            return self._allPlayers[name]

        for player in self._allPlayers:
            if name.lower() == player._name.lower():
                return player

        return None