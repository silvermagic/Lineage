# -*- coding: utf-8 -*-

import logging,random
from Datatables import Session,Getback
from server.model.TownLocation import TownLocation
from server.templates.GetBack import GetBack
from server.utils.Singleton import Singleton

class GetBackTable():
    __metaclass__ = Singleton
    def __init__(self):
        self._getback = {}
        self.loadGetBack()

    def loadGetBack(self):
        try:
            with Session() as session:
                for rs in session.query(Getback).order_by(Getback.area_mapid.desc(), Getback.area_x1.desc()).all():
                    item = GetBack()
                    item._areaX1 = rs.area_x1
                    item._areaY1 = rs.area_y1
                    item._areaX2 = rs.area_x2
                    item._areaY2 = rs.area_y2
                    item._areaMapId = rs.area_mapid
                    item._getbackX1 = rs.getback_x1
                    item._getbackY1 = rs.getback_y1
                    item._getbackX2 = rs.getback_x2
                    item._getbackY2 = rs.getback_y2
                    item._getbackX3 = rs.getback_x3
                    item._getbackX3 = rs.getback_y3
                    item._getbackMapId = rs.getback_mapid
                    item._getbackTownId = rs.getback_townid
                    item._getbackTownIdForElf = rs.getback_townid_elf
                    item._getbackTownIdForDarkelf = rs.getback_townid_darkelf
                    item._escapable = rs.scrollescape

                    if self._getback.has_key(item._areaMapId):
                        self._getback[item._areaMapId].append(item)
                    else:
                        self._getback[item._areaMapId] = [item]
        except Exception as e:
            logging.error(e)

    def GetBack_Location(self, pc, bScroll_Escape = True):
        '''
        获取玩家当前的回城点
        :param pc:
        :param bScroll_Escape:
        :return:回城点坐标
        '''
        loc = [0, 0, 0]
        nPosition = random.randrange(3)

        pcLocX = pc._loc._x
        pcLocY = pc._loc._x
        pcMapId = pc._loc._map._mapId
        getbackList = None
        if self._getback.has_key(pcMapId):
            getbackList = self._getback[pcMapId]

        if getbackList:
            getback = None
            for gb in getbackList:
                if gb.isSpecifyArea():
                    if gb._areaX1 <= pcLocX \
                            and pcLocX <= gb._areaX2 \
                            and gb._areaY1 <= pcLocY \
                            and pcLocY <= gb._areaY2:
                        getback = gb
                        break
                else:
                    getback = gb
                    break

            loc = self.ReadGetbackInfo(getback, nPosition)

            if pc.isElf() and getback._getbackTownIdForElf > 0:
                loc = TownLocation.getGetBackLoc(getback._getbackTownIdForElf)
            elif pc.isDarkelf() and getback._getbackTownIdForDarkelf > 0:
                loc = TownLocation.getGetBackLoc(getback._getbackTownIdForDarkelf)
            elif getback._getbackTownId > 0:
                loc = TownLocation.getGetBackLoc(getback._getbackTownId)
        else:
            loc = [33089, 33397, 4]

        return loc

    def ReadGetbackInfo(self, getback, nPosition):
        '''
        获取回城点的三个游戏坐标的其中一个
        :param getback:回城点
        :param nPosition:索引
        :return:游戏坐标
        '''
        loc = [0, 0, 0]
        if nPosition == 0:
            loc[0] = getback._getbackX1
            loc[1] = getback._getbackY1
        elif nPosition == 1:
            loc[0] = getback._getbackX2
            loc[1] = getback._getbackY2
        elif nPosition == 2:
            loc[0] = getback._getbackX3
            loc[1] = getback._getbackY3
        loc[2] = getback._getbackMapId

        return loc