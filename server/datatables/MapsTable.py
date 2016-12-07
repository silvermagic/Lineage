# -*- coding: utf-8 -*-

import logging
from Datatables import Session,mapids
from server.utils.Singleton import Singleton

class MapData():
    def __init__(self):
        self.startX = 0
        self.endX = 0
        self.startY = 0
        self.endY = 0
        self.monster_amount = 1
        self.dropRate = 1
        self.isUnderwater = False
        self.isMarkable = False
        self.isTeleportable = False
        self.isEscapable = False
        self.isUseResurrection = False
        self.isUsePainwand = False
        self.isEnabledDeathPenalty = False
        self.isTakePets = False
        self.isRecallPets = False
        self.isUsableItem = False
        self.isUsableSkill = False

class MapsTable():
    __metaclass__ = Singleton
    def __init__(self):
        self._maps = {}
        logging.debug('loading maps from db...')
        try:
            with Session() as session:
                for rs in session.query(mapids).all():
                    item = MapData()
                    mapId = rs.mapid
                    item.startX = rs.startX
                    item.endX = rs.endX
                    item.startY = rs.startY
                    item.endY = rs.endY
                    item.monster_amount = rs.monster_amount
                    item.dropRate = rs.drop_rate
                    item.isUnderwater = rs.underwater
                    item.isMarkable = rs.markable
                    item.isTeleportable = rs.teleportable
                    item.isEscapable = rs.escapable
                    item.isUseResurrection = rs.resurrection
                    item.isUsePainwand = rs.painwand
                    item.isEnabledDeathPenalty = rs.penalty
                    item.isTakePets = rs.take_pets
                    item.isRecallPets = rs.recall_pets
                    item.isUsableItem = rs.usable_item
                    item.isUsableSkill = rs.usable_skill

                    self._maps[mapId] = item
        except Exception as e:
            logging.error(e)
