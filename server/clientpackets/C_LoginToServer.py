# -*- coding: utf-8 -*-

import logging
from Config import Config
from Datatables import Session,character_skills
from server import ActionCodes
from server.datatables.CharacterTable import CharacterTable
from server.datatables.GetBackRestartTable import GetBackRestartTable
from server.datatables.GetBackTable import GetBackTable
from server.datatables.SkillsTable import SkillsTable
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
from server.serverpackets.S_AddSkill import S_AddSkill
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
        self.skills(pc)
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
            pc.setCurrentHp(currentHpAtLoad)
        if currentMpAtLoad > pc._currentMp:
            pc.setCurrentMp(currentMpAtLoad)

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
            Wizard = 0
            Wizard2 = 0
            Wizard3 = 0
            Wizard4 = 0
            Wizard5 = 0
            Wizard6 = 0
            Wizard7 = 0
            Wizard8 = 0
            Wizard9 = 0
            Wizard10 = 0
            Knight = 0
            Knight2 = 0
            Darkelf = 0
            Darkelf2 = 0
            Crown = 0
            unused = 0
            Elf = 0
            Elf2 = 0
            Elf3 = 0
            Elf4 = 0
            Elf5 = 0
            Elf6 = 0
            DragonKnight = 0
            DragonKnight2 = 0
            DragonKnight3 = 0
            Illusionist = 0
            Illusionist2 = 0
            Illusionist3 = 0
            with Session() as session:
                for rs in session.query(character_skills).filter(character_skills.char_obj_id == pc._id).all():
                    skills = SkillsTable()._skills[rs.skill_id]
                    if skills._skillLevel == 1:
                        Wizard |= skills._id
                    elif skills._skillLevel == 2:
                        Wizard2 |= skills._id
                    elif skills._skillLevel == 3:
                        Wizard3 |= skills._id
                    elif skills._skillLevel == 4:
                        Wizard4 |= skills._id
                    elif skills._skillLevel == 5:
                        Wizard5 |= skills._id
                    elif skills._skillLevel == 6:
                        Wizard6 |= skills._id
                    elif skills._skillLevel == 7:
                        Wizard7 |= skills._id
                    elif skills._skillLevel == 8:
                        Wizard8 |= skills._id
                    elif skills._skillLevel == 9:
                        Wizard9 |= skills._id
                    elif skills._skillLevel == 10:
                        Wizard10 |= skills._id
                    elif skills._skillLevel == 11:
                        Knight |= skills._id
                    elif skills._skillLevel == 12:
                        Knight2 |= skills._id
                    elif skills._skillLevel == 13:
                        Darkelf |= skills._id
                    elif skills._skillLevel == 14:
                        Darkelf2 |= skills._id
                    elif skills._skillLevel == 15:
                        Crown |= skills._id
                    elif skills._skillLevel == 16:
                        unused |= skills._id
                    elif skills._skillLevel == 17:
                        Elf |= skills._id
                    elif skills._skillLevel == 18:
                        Elf2 |= skills._id
                    elif skills._skillLevel == 19:
                        Elf3 |= skills._id
                    elif skills._skillLevel == 20:
                        Elf4 |= skills._id
                    elif skills._skillLevel == 21:
                        Elf5 |= skills._id
                    elif skills._skillLevel == 22:
                        Elf6 |= skills._id
                    elif skills._skillLevel == 23:
                        DragonKnight |= skills._id
                    elif skills._skillLevel == 24:
                        DragonKnight2 |= skills._id
                    elif skills._skillLevel == 25:
                        DragonKnight3 |= skills._id
                    elif skills._skillLevel == 26:
                        Illusionist |= skills._id
                    elif skills._skillLevel == 27:
                        Illusionist2 |= skills._id
                    elif skills._skillLevel == 28:
                        Illusionist3 |= skills._id
                    pc.setSkillMastery(rs.skill_id)

            i = Wizard + Wizard2 + Wizard3 + Wizard4 + Wizard5 + Wizard6 + Wizard7 + Wizard8 + Wizard9 + Wizard10 \
                + Knight + Knight2 + Darkelf + Darkelf2 + Crown + unused + Elf \
                + Elf2 + Elf3 + Elf4 + Elf5 + Elf6 + DragonKnight + DragonKnight2 + DragonKnight3 \
                + Illusionist + Illusionist2 + Illusionist3
            if i > 0:
                pc.sendPackets(S_AddSkill(Wizard, Wizard2, Wizard3, Wizard4, Wizard5, Wizard6, Wizard7, Wizard8, Wizard9, Wizard10,
                                          Knight, Knight2, Darkelf, Darkelf2, Crown, unused, Elf, Elf2, Elf3, Elf4, Elf5, Elf6,
                                          DragonKnight, DragonKnight2, DragonKnight3, Illusionist, Illusionist2, Illusionist3))
        except Exception as e:
            logging.error(e)

    def buff(self, client, pc):
        pass
