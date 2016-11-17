# -*- coding: utf-8 -*-

import threading,logging
from datetime import datetime
from Datatables import Session,Characters,Character_Buddys,Character_Buff,Character_Config,Character_Items,Character_Quests,Character_Skills,Character_Teleport
from server.model.Instance.PcInstance import PcInstance
from server.model.map.WorldMap import WorldMap
from server.utils.Singleton import Singleton
from server.utils.TimeUtil import TimeUtil

class CharacterTable():
    __metaclass__ = Singleton
    def __init__(self):
        self._charNameList = {}
        self._lock = threading.Lock()

    def storeNewCharacter(self, pc):
        with self._lock:
            self._createCharacter(pc)
            if not self._charNameList.has_key(pc._name):
                self._charNameList[pc._name] = pc._id

    def storeCharacter(self, pc):
        with self._lock:
            self._storeCharacter(pc)

    def deleteCharacter(self, accountName, charName):
        with self._lock:
            self.deleteCharacter(accountName, charName)
            if self._charNameList.has_key(charName):
                self._charNameList.pop(charName)

    def loadCharacter(self, charName):
        return self._loadCharacter(charName)

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
        pass

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

    def _loadCharacter(self, charName):
        pc = None
        try:
            with Session() as session:
                item = session.query(Characters).filter(Characters._name == charName).one_or_none()
                pc = PcInstance()
                pc._accountName = item.account_name
                pc._id = item.objid
                pc._name = item.char_name
                pc._birthday = TimeUtil.dt2ts(item.birthday)
                pc._highLevel = item.HighLevel
                pc._exp = item.Exp
                pc.addBaseMaxHp(item.MaxMp)
                pc._currentHp = item.CurHp
                if pc._currentHp < 1:
                    pc._currentHp = 1
                pc.addMaxMp(item.MaxMp)
                pc._currentMp = item.CurMp
                pc.addBaseStr(item.Str)
                pc.addBaseCon(item.Con)
                pc.addBaseDex(item.Dex)
                pc.addBaseCha(item.Cha)
                pc.addBaseInt(item.Intel)
                pc.addBaseWis(item.Wis)
                pc._currentWeapon = item.Status
                pc._classId = item.Class
                pc._tempCharGfx = item.Class
                pc._gfxid = item.Class
                pc._sex = item.Sex
                pc._type = item.Type
                pc._heading = item.Heading
                if pc._heading > 7:
                    pc._heading = 0
                pc._loc._x = item.LocX
                pc._loc._y = item.LocY
                pc._loc._map = WorldMap()._maps[item.MapID]
                pc._food = item.Food
                pc._lawful = item.Lawful
                pc._title = item.Title
                pc._clanid = item.ClanID
                pc._clanname = item.Clanname
                pc._clanRank = item.ClanRank
                pc._bonusStats = item.BonusStatus
                pc._elixirStats = item.ElixirStatus
                pc._elfAttr = item.ElfAttr
                pc._PKcount = item.PKcount
                pc._PkCountForElf = item.PkCountForElf
                pc._expRes = item.ExpRes
                pc._partnerId = item.PartnerID
                pc._accessLevel = item.AccessLevel
                if pc._accessLevel == 200:
                    pc._gm = True
                    pc._monitor = False
                elif pc._accessLevel == 100:
                    pc._gm = False
                    pc._monitor = True
                else:
                    pc._gm = False
                    pc._monitor = False
                pc._onlineStatus = item.OnlineStatus
                pc._homeTownId = item.HomeTownID
                pc._contribution = item.Contribution
                pc._hellTime = item.HellTime
                pc._banned = item.Banned
                pc._karma.set(item.Karma)
                pc._lastPk = TimeUtil.dt2ts(item.LastPk)
                pc._lastPkForElf = TimeUtil.dt2ts(item.LastPkForElf)
                pc._deleteTime = TimeUtil.dt2ts(item.DeleteTime)
                pc._originalStr = item.OriginalStr
                pc._originalCon = item.OriginalCon
                pc._originalDex = item.OriginalDex
                pc._originalCha = item.OriginalCha
                pc._originalInt = item.OriginalInt
                pc._originalWis = item.OriginalWis
                pc._lastActive = TimeUtil.dt2ts(item.LastActive)
                pc._ainZone = item.AinZone
                pc._ainPoint = item.AinPoint
        except Exception as e:
            logging.error(e)

        return pc

    def _createCharacter(self, pc):
        try:
            with Session() as session:
                item = Characters()
                item.account_name = pc._accountName
                item.objid = pc._id
                item.char_name = pc._name
                item.birthday = TimeUtil.ts2dt(pc.getSimpleBirthday())
                item.level = pc._level
                item.HighLevel = pc._highLevel
                item.Exp = pc._exp
                item.MaxHp = pc._baseMaxHp
                item.CurHp = pc._currentHp
                if item.CurHp < 1:
                    item.CurHp = 1
                item.MaxMp = pc._baseMaxMp
                item.CurMp = pc._currentMp
                item.Ac = pc._ac
                item.Str = pc._str
                item.Con = pc._con
                item.Dex = pc._dex
                item.Cha = pc._cha
                item.Intel = pc._int
                item.Wis = pc._wis
                item.Status = pc._currentWeapon
                item.Class = pc._classId
                item.Sex = pc._sex
                item.Type = pc._type
                item.Heading = pc._heading
                item.LocX = pc._loc._x
                item.LocY = pc._loc._y
                item.MapID = pc._loc._map._mapId
                item.Food = pc._food
                item.Lawful = pc._lawful
                item.Title = pc._title
                item.ClanID = pc._clanid
                item.Clanname = pc._clanname
                item.ClanRank = pc._clanRank
                item.BonusStatus = pc._bonusStats
                item.ElixirStatus = pc._elixirStats
                item.ElfAttr = pc._elfAttr
                item.PKcount = pc._PKcount
                item.PkCountForElf = pc._PkCountForElf
                item.ExpRes = pc._expRes
                item.PartnerID = pc._partnerId
                item.AccessLevel = pc._accessLevel
                item.OnlineStatus = pc._onlineStatus
                item.HomeTownID = pc._homeTownId
                item.Contribution = pc._contribution
                item.Pay = 0
                item.HellTime = pc._hellTime
                item.Banned = pc._banned
                item.Karma = pc._karma._karma
                item.LastPk = TimeUtil.ts2dt(pc._lastPk)
                item.LastPkForElf = TimeUtil.ts2dt(pc._lastPkForElf)
                item.DeleteTime = TimeUtil.ts2dt(pc._deleteTime)
                session.add(item)
        except Exception as e:
            logging.error(e)

    def _deleteCharacter(self, accountName, charName):
        try:
            with Session() as session:
                units = session.query(Characters).filter(Characters.account_name ==  accountName, Characters.char_name == charName).all()
                session.query(Character_Buddys).filter(Character_Buddys.char_id.in_(units)).delete()
                session.query(Character_Buff).filter(Character_Buff.char_obj_id.in_(units)).delete()
                session.query(Character_Config).filter(Character_Config.object_id.in_(units)).delete()
                session.query(Character_Items).filter(Character_Items.char_id.in_(units)).delete()
                session.query(Character_Quests).filter(Character_Quests.char_id.in_(units)).delete()
                session.query(Character_Skills).filter(Character_Skills.char_obj_id.in_(units)).delete()
                session.query(Character_Teleport).filter(Character_Teleport.char_id.in_(units)).delete()
                session.query(Characters).filter(Characters.char_name == charName).delete()
        except Exception as e:
            logging.error(e)

    def _storeCharacter(self, pc):
        hp = pc._currentHp
        if hp < 1:
            hp = 1
        try:
            with Session() as session:
                session.query(Characters).filter(Characters.objid == pc._id).update({Characters.level : pc._level,
                                                           Characters.HighLevel : pc._highLevel,
                                                           Characters.Exp : pc._exp,
                                                           Characters.MaxHp : pc._baseMaxHp,
                                                           Characters.CurHp : hp,
                                                           Characters.MaxMp : pc._baseMaxMp,
                                                           Characters.CurMp : pc._currentMp,
                                                           Characters.Ac : pc._ac,
                                                           Characters.Str : pc._baseStr,
                                                           Characters.Con : pc._baseCon,
                                                           Characters.Dex : pc._baseDex,
                                                           Characters.Cha : pc._baseCha,
                                                           Characters.Intel : pc._baseInt,
                                                           Characters.Wis : pc._baseWis,
                                                           Characters.Status : pc._currentWeapon,
                                                           Characters.Class : pc._classId,
                                                           Characters.Sex : pc._sex,
                                                           Characters.Type : pc._type,
                                                           Characters.Heading : pc._heading,
                                                           Characters.LocX : pc._loc._x,
                                                           Characters.LocY : pc._loc._y,
                                                           Characters.MapID : pc._loc._map._mapId,
                                                           Characters.Food : pc._food,
                                                           Characters.Lawful : pc._lawful,
                                                           Characters.Title : pc._title,
                                                           Characters.ClanID : pc._clanid,
                                                           Characters.Clanname : pc._clanname,
                                                           Characters.ClanRank : pc._clanRank,
                                                           Characters.BonusStatus : pc._bonusStats,
                                                           Characters.ElixirStatus : pc._elixirStats,
                                                           Characters.ElfAttr : pc._elfAttr,
                                                           Characters.PKcount : pc._PKcount,
                                                           Characters.PkCountForElf : pc._PkCountForElf,
                                                           Characters.ExpRes : pc._expRes,
                                                           Characters.PartnerID : pc._partnerId,
                                                           Characters.AccessLevel : pc._accessLevel,
                                                           Characters.OnlineStatus : pc._onlineStatus,
                                                           Characters.HomeTownID : pc._homeTownId,
                                                           Characters.Contribution : pc._contribution,
                                                           Characters.HellTime : pc._hellTime,
                                                           Characters.Banned : pc._banned,
                                                           Characters.Karma : pc._karma._karma,
                                                           Characters.LastPk : TimeUtil.ts2dt(pc._lastPk),
                                                           Characters.LastPkForElf : TimeUtil.ts2dt(pc._lastPkForElf),
                                                           Characters.DeleteTime : TimeUtil.ts2dt(pc._deleteTime),
                                                           Characters.LastActive : datetime.now(),
                                                           Characters.AinZone : pc._ainZone,
                                                           Characters.AinPoint : pc._ainPoint})
        except Exception as e:
            logging.error(e)

