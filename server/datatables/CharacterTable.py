# -*- coding: utf-8 -*-

import threading,logging
from Datatables import Session,characters
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
                session.query(characters).update({characters.OnlineStatus : 0})
        except Exception as e:
            logging.error(e)

    def updateOnlineStatus(self, pc):
        try:
            with Session() as session:
                session.query(characters).filter(characters.objid == pc._id).update({characters.OnlineStatus : 0})
        except Exception as e:
            logging.error(e)

    def updatePartnerId(self, targetId, partnerId = 0):
        try:
            with Session() as session:
                session.query(characters).filter(characters.objid == targetId).update({characters.PartnerID : partnerId})
        except Exception as e:
            logging.error(e)

    def saveCharStatus(self, pc):
        try:
            with Session() as session:
                session.query(characters).filter(characters.objid == pc._id).update({characters.OriginalStr : pc._baseStr,
                                                                                     characters.OriginalCon : pc._baseCon,
                                                                                     characters.OriginalDex : pc._baseDex,
                                                                                     characters.OriginalCha : pc._baseCha,
                                                                                     characters.OriginalInt : pc._baseInt,
                                                                                     characters.OriginalWis : pc._baseWis})
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
                ret = session.query(characters).filter(characters.char_name == name).one_or_none()
        except Exception as e:
            logging.error(e)
        return ret != None

    def loadAllCharName(self):
        try:
            with Session() as session:
                for item in session.query(characters).all():
                    self._charNameList[item.char_name] = item.objid
        except Exception as e:
            logging.error(e)

