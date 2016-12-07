# -*- coding: utf-8 -*-

import threading,logging
from Datatables import Session,Characters
from server.storage.MySqlCharacterStorage import MySqlCharacterStorage
from server.utils.Singleton import Singleton

class CharacterTable():
    __metaclass__ = Singleton
    def __init__(self):
        self._charStorage = MySqlCharacterStorage()
        self._charNameList = {}
        self._lock = threading.Lock()

    def storeNewCharacter(self, pc):
        with self._lock:
            self._charStorage.createCharacter(pc)
            if not self._charNameList.has_key(pc._name):
                self._charNameList[pc._name] = pc._id

    def storeCharacter(self, pc):
        with self._lock:
            self._charStorage.storeCharacter(pc)

    def deleteCharacter(self, accountName, charName):
        with self._lock:
            self.deleteCharacter(accountName, charName)
            if self._charNameList.has_key(charName):
                self._charNameList.pop(charName)

    def loadCharacter(self, charName):
        return self._charStorage.loadCharacter(charName)

    def clearOnlineStatus(self):
        try:
            with Session() as session:
                session.query(Characters).update({Characters.OnlineStatus : 0})
        except Exception as e:
            logging.error(e)

    def updateOnlineStatus(self, pc):
        try:
            with Session() as session:
                session.query(Characters).filter(Characters.objid == pc._id).update({Characters.OnlineStatus : 0})
        except Exception as e:
            logging.error(e)

    def updatePartnerId(self, targetId, partnerId = 0):
        try:
            with Session() as session:
                session.query(Characters).filter(Characters.objid == targetId).update({Characters.PartnerID : partnerId})
        except Exception as e:
            logging.error(e)

    def saveCharStatus(self, pc):
        try:
            with Session() as session:
                session.query(Characters).filter(Characters.objid == pc._id).update({Characters.OriginalStr : pc._baseStr,
                                                                                     Characters.OriginalCon : pc._baseCon,
                                                                                     Characters.OriginalDex : pc._baseDex,
                                                                                     Characters.OriginalCha : pc._baseCha,
                                                                                     Characters.OriginalInt : pc._baseInt,
                                                                                     Characters.OriginalWis : pc._baseWis})
        except Exception as e:
            logging.error(e)

    def restoreInventory(self, pc):
        '''
        从数据库中加载用户仓库道具信息
        :param pc:玩家角色(PcInstance)
        :return:None
        '''
        pc._inventory.loadItems()
        pc._dwarf.loadItems()
        pc._dwarfForElf.loadItems()

    def doesCharNameExist(self, name):
        ret = None
        try:
            with Session() as session:
                ret = session.query(Characters).filter(Characters.char_name == name).one_or_none()
        except Exception as e:
            logging.error(e)
        return ret != None

    def loadAllCharName(self):
        try:
            with Session() as session:
                for item in session.query(Characters).all():
                    self._charNameList[item.char_name] = item.objid
        except Exception as e:
            logging.error(e)

