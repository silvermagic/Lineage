# -*- coding: utf-8 -*-

import logging
from Config import Config
from Datatables import Session,character_skills
from server import ActionCodes
from server.datatables.CharacterTable import CharacterTable
from server.datatables.GetBackRestartTable import GetBackRestartTable
from server.datatables.GetBackTable import GetBackTable
from server.model.World import World
from server.serverpackets.S_InitialAbilityGrowth import S_InitialAbilityGrowth
from server.serverpackets.S_LoginToGame import S_LoginToGame
from server.serverpackets.S_Unknown2 import S_Unknown2
from server.serverpackets.S_ActiveSpells import S_ActiveSpells
from server.serverpackets.S_Karma import S_Karma
from server.serverpackets.S_OwnCharStatus import S_OwnCharStatus
from server.serverpackets.S_MapID import S_MapID
from server.serverpackets.S_OwnCharPack import S_OwnCharPack
from server.serverpackets.S_SPMR import S_SPMR
from server.serverpackets.S_CharTitle import S_CharTitle
from server.serverpackets.S_InvList import S_InvList
from server.serverpackets.S_Weather import S_Weather
from server.serverpackets.S_CharacterConfig import S_CharacterConfig
from ClientBasePacket import ClientBasePacket

class C_LoginToServer(ClientBasePacket):
    def __init__(self, abyte, client):
        ClientBasePacket.__init__(self, abyte)

        login = client._account._name
        charName = self.readS()

        if client._activeChar:
            logging.info("角色ID重复登入(" + client._hostname + ")已强制中断连线 。")
            return

        pc = CharacterTable().loadCharacter(charName)
        if not pc or pc._accountName != login:
            logging.info("【无法进入】 角色名称：" + charName + " 玩家帐号：" + login + " 玩家IP：" + client._hostname)
            return

        if Config.getint('server', 'LevelDownRange') > 0:
            if (pc._highLevel - pc.getLevel()) >=  Config.getint('server', 'LevelDownRange'):
                logging.info("不允许的等级要求范围的角色: 角色名称=" + charName + " 玩家帐号=" + login + " 玩家IP=" + client._hostname)
                client.kick()
                return

        logging.info("【进入游戏】 角色名称：" + charName + " 玩家帐号：" + login + " 玩家IP：" + client._hostname)

        currentHpAtLoad = pc._currentHp
        currentMpAtLoad = pc._currentMp
        pc.skillList = []
        pc._onlineStatus = 1
        CharacterTable().updateOnlineStatus(pc)
        World().storeObject(pc)
        pc._netConnection = client
        client._activeChar = pc

        pc.sendPackets(S_InitialAbilityGrowth(pc))
        pc.sendPackets(S_LoginToGame())
        pc.sendPackets(S_Unknown2())

        # self.bookmarks(pc)
        for gbr in GetBackRestartTable()._getbackrestart.values():
            if pc._loc._map._mapId == gbr._mapId:
                pc._loc._x = gbr._locX
                pc._loc._y = gbr._locY
                pc.setMap(gbr._mapId)
        if Config.getboolean('altsettings', 'GetBack'):
            loc = GetBackTable().GetBack_Location(pc)
            pc._loc._x = loc[0]
            pc._loc._y = loc[1]
            pc.setMap(loc[2])

        # todo: 战争血盟复活地点设置
        World().addVisibleObject(pc)
        pc.sendPackets(S_ActiveSpells())
        pc.sendPackets(S_Karma(pc))

        # pc.beginGameTimeCarrier()

        pc.sendPackets(S_OwnCharStatus(pc))
        pc.sendPackets(S_MapID(pc._loc._map._mapId, pc._loc._map._isUnderwater))
        pc.sendPackets(S_OwnCharPack(pc))
        pc.sendPackets(S_SPMR(pc))

        pc.sendPackets(S_CharTitle(pc._id, pc._title))
        # pc.broadcastPacket(S_CharTitle(pc._id, pc._title))

        # todo: 中毒 水中等视觉
        pc.sendPackets(S_Weather(World()._weather))

        self.items(pc)
        # self.skills(pc)
        # self.buff(client, pc)
        # pc.turnOnOffLight()

        # todo: 祝福经验

        if pc._currentHp > 0:
            pc._isDead = False
            pc._status = 0
        else:
            pc._isDead = True
            pc._status = ActionCodes.ACTION_Die

        # todo: 在线奖励系统

        if Config.getboolean('server', 'CharacterConfigInServerSide'):
            # pc.sendPackets(S_CharacterConfig(pc._id))
            pass

        # todo: 召唤系统
        # todo: 攻城时间系统
        # todo: 玩家上线通知
        # todo: 血盟系统
        # todo: 结婚系统

        if currentHpAtLoad > pc._currentHp:
            pc._currentHp = currentHpAtLoad
        if currentMpAtLoad > pc._currentMp:
            pc._currentMp = currentMpAtLoad

        # todo: 回血 回魔 自动更新系统
        client._charRestart = False
        # todo: 经验系统
        # pc.save()
        pc.sendPackets(S_OwnCharStatus(pc))

        # 地狱惩罚系统
        if pc._hellTime > 0:
            pass

    def bookmarks(self, pc):
        pass

    def items(self, pc):
        CharacterTable().restoreInventory(pc)
        pc.sendPackets(S_InvList(pc._inventory._item_insts))

    def skills(self, pc):
        try:
            i = 0
            lv1 = 0
            lv2 = 0
            lv3 = 0
            lv4 = 0
            lv5 = 0
            lv6 = 0
            lv7 = 0
            lv8 = 0
            lv9 = 0
            lv10 = 0
            lv11 = 0
            lv12 = 0
            lv13 = 0
            lv14 = 0
            lv15 = 0
            lv16 = 0
            lv17 = 0
            lv18 = 0
            lv19 = 0
            lv20 = 0
            lv21 = 0
            lv22 = 0
            lv23 = 0
            lv24 = 0
            lv25 = 0
            lv26 = 0
            lv27 = 0
            lv28 = 0
            with Session() as session:
                for item in session.query(character_skills).all():
                    pass
        except Exception as e:
            logging.error(e)

    def buff(self, client, pc):
        pass
