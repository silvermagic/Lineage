# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from Datatables import Session,characters,character_buddys,character_buff,character_config,character_items,character_quests,character_skills,character_teleport
from server.utils.TimeUtil import TimeUtil
from CharacterStorage import CharacterStorage

class MySqlCharacterStorage(CharacterStorage):
    def loadCharacter(self, charName):
        from server.model.Instance.PcInstance import PcInstance
        pc = None
        try:
            with Session() as session:
                item = session.query(characters).filter(characters.char_name == charName).one_or_none()
                pc = PcInstance()
                pc._accountName = item.account_name
                pc._id = item.objid
                pc._name = item.char_name
                pc._birthday = TimeUtil.dt2ts(item.birthday)
                pc._highLevel = item.HighLevel
                pc.setExp(item.Exp)
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
                pc.setMap(item.MapID)
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

    def createCharacter(self, pc):
        try:
            with Session() as session:
                item = characters()
                item.account_name = pc._accountName
                item.objid = pc._id
                item.char_name = pc._name
                item.birthday = TimeUtil.ts2dt(pc.getSimpleBirthday())
                item.level = pc._level
                item.HighLevel = pc._highLevel
                item.Exp = pc.getExp()
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

    def deleteCharacter(self, accountName, charName):
        try:
            with Session() as session:
                units = session.query(characters).filter(characters.account_name == accountName,
                                                         characters.char_name == charName).all()
                session.query(character_buddys).filter(character_buddys.char_id.in_(units)).delete()
                session.query(character_buff).filter(character_buff.char_obj_id.in_(units)).delete()
                session.query(character_config).filter(character_config.object_id.in_(units)).delete()
                session.query(character_items).filter(character_items.char_id.in_(units)).delete()
                session.query(character_quests).filter(character_quests.char_id.in_(units)).delete()
                session.query(character_skills).filter(character_skills.char_obj_id.in_(units)).delete()
                session.query(character_teleport).filter(character_teleport.char_id.in_(units)).delete()
                session.query(characters).filter(characters.char_name == charName).delete()
        except Exception as e:
            logging.error(e)

    def storeCharacter(self, pc):
        hp = pc._currentHp
        if hp < 1:
            hp = 1
        try:
            with Session() as session:
                session.query(characters).filter(characters.objid == pc._id).update({characters.level: pc._level,
                                                                                     characters.HighLevel: pc._highLevel,
                                                                                     characters.Exp: pc.getExp(),
                                                                                     characters.MaxHp: pc._baseMaxHp,
                                                                                     characters.CurHp: hp,
                                                                                     characters.MaxMp: pc._baseMaxMp,
                                                                                     characters.CurMp: pc._currentMp,
                                                                                     characters.Ac: pc._ac,
                                                                                     characters.Str: pc._baseStr,
                                                                                     characters.Con: pc._baseCon,
                                                                                     characters.Dex: pc._baseDex,
                                                                                     characters.Cha: pc._baseCha,
                                                                                     characters.Intel: pc._baseInt,
                                                                                     characters.Wis: pc._baseWis,
                                                                                     characters.Status: pc._currentWeapon,
                                                                                     characters.Class: pc._classId,
                                                                                     characters.Sex: pc._sex,
                                                                                     characters.Type: pc._type,
                                                                                     characters.Heading: pc._heading,
                                                                                     characters.LocX: pc._loc._x,
                                                                                     characters.LocY: pc._loc._y,
                                                                                     characters.MapID: pc._loc._map._mapId,
                                                                                     characters.Food: pc._food,
                                                                                     characters.Lawful: pc._lawful,
                                                                                     characters.Title: pc._title,
                                                                                     characters.ClanID: pc._clanid,
                                                                                     characters.Clanname: pc._clanname,
                                                                                     characters.ClanRank: pc._clanRank,
                                                                                     characters.BonusStatus: pc._bonusStats,
                                                                                     characters.ElixirStatus: pc._elixirStats,
                                                                                     characters.ElfAttr: pc._elfAttr,
                                                                                     characters.PKcount: pc._PKcount,
                                                                                     characters.PkCountForElf: pc._PkCountForElf,
                                                                                     characters.ExpRes: pc._expRes,
                                                                                     characters.PartnerID: pc._partnerId,
                                                                                     characters.AccessLevel: pc._accessLevel,
                                                                                     characters.OnlineStatus: pc._onlineStatus,
                                                                                     characters.HomeTownID: pc._homeTownId,
                                                                                     characters.Contribution: pc._contribution,
                                                                                     characters.HellTime: pc._hellTime,
                                                                                     characters.Banned: pc._banned,
                                                                                     characters.Karma: pc._karma._karma,
                                                                                     characters.LastPk: TimeUtil.ts2dt(
                                                                                         pc._lastPk),
                                                                                     characters.LastPkForElf: TimeUtil.ts2dt(
                                                                                         pc._lastPkForElf),
                                                                                     characters.DeleteTime: TimeUtil.ts2dt(
                                                                                         pc._deleteTime),
                                                                                     characters.LastActive: datetime.now(),
                                                                                     characters.AinZone: pc._ainZone,
                                                                                     characters.AinPoint: pc._ainPoint})
        except Exception as e:
            logging.error(e)