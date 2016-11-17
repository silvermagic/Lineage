# -*- coding: utf-8 -*-

import logging
from Datatables import Session,Mapids
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
                for item in session.query(Mapids).all():
                    data = MapData()
                    mapId = item.mapid
                    data.startX = item.startX
                    data.endX = item.endX
                    data.startY = item.startY
                    data.endY = item.endY
                    data.monster_amount = item.monster_amount
                    data.dropRate = item.drop_rate
                    data.isUnderwater = item.underwater
                    data.isMarkable = item.markable
                    data.isTeleportable = item.teleportable
                    data.isEscapable = item.escapable
                    data.isUseResurrection = item.resurrection
                    data.isUsePainwand = item.painwand
                    data.isEnabledDeathPenalty = item.penalty
                    data.isTakePets = item.take_pets
                    data.isRecallPets = item.recall_pets
                    data.isUsableItem = item.usable_item
                    data.isUsableSkill = item.usable_skill

                    self._maps[mapId] = data
        except Exception as e:
            logging.error(e)
