# -*- coding: utf-8 -*-

import logging,time,math
from datetime import datetime
from Config import Config
from server.model.Character import Character
from server.model.Karma import Karma
from server.model.PcInventory import PcInventory
from server.model.DwarfInventory import DwarfInventory
from server.model.DwarfForElfInventory import DwarfForElfInventory
from server.model.EquipmentSlot import EquipmentSlot
from server.serverpackets.S_HPUpdate import S_HPUpdate
from server.serverpackets.S_MPUpdate import S_MPUpdate
from server.utils.IntRange import IntRange
from server.utils.CalcStat import CalcStat

CLASSID_KNIGHT_MALE = 61
CLASSID_KNIGHT_FEMALE = 48
CLASSID_ELF_MALE = 138
CLASSID_ELF_FEMALE = 37
CLASSID_WIZARD_MALE = 734
CLASSID_WIZARD_FEMALE = 1186
CLASSID_DARK_ELF_MALE = 2786
CLASSID_DARK_ELF_FEMALE = 2796
CLASSID_PRINCE = 0
CLASSID_PRINCESS = 1
CLASSID_DRAGON_KNIGHT_MALE = 6658
CLASSID_DRAGON_KNIGHT_FEMALE = 6661
CLASSID_ILLUSIONIST_MALE = 6671
CLASSID_ILLUSIONIST_FEMALE = 6650

INTERVAL_AUTO_UPDATE = 300
INTERVAL_EXP_MONITOR = 500

class PcInstance(Character):
    def __init__(self):
        # 成员变量含义参见变量引用函数的说明
        Character.__init__(self)
        # 角色属性计算
        self._elixirStats = 0 # 万能药水使用数目
        self._baseStr = 0
        self._originalStr = 0 # 角色最初创建时的力量值
        self._baseDex = 0
        self._originalDex = 0
        self._baseCha = 0
        self._originalCha = 0
        self._baseInt = 0
        self._originalInt = 0
        self._baseWis = 0
        self._originalWis = 0
        self._baseCon = 0
        self._originalCon = 0
        # 近战/远程伤害加成 近战/远程命中加成 魔法伤害加成 魔法命中加成 魔法暴击加成计算
        self._baseDmgup = 0
        self._originalDmgup = 0
        self._dmgModifierByArmor = 0
        self._baseBowDmgup = 0
        self._originalBowDmgup = 0
        self._bowDmgModifierByArmor = 0
        self._baseHitup = 0
        self._originalHitup = 0
        self._hitModifierByArmor = 0
        self._baseBowHitup = 0
        self._originalBowHitup = 0
        self._bowHitModifierByArmor = 0
        self._originalMagicHit = 0
        self._originalMagicDamage = 0
        self._originalMagicCritical = 0
        # 防御计算
        self._baseAc = 0
        self._originalAc = 0
        # 血量魔量计算
        self._baseMaxHp = 0
        self._originalHpup = 0
        self._advenHp = 0
        self._baseMaxMp = 0
        self._originalMpup = 0
        self._advenMp = 0
        # 体力和魔力回复量计算
        self._hpr = 0
        self._trueHpr = 0
        self._originalHpr = 0
        self._mpr = 0
        self._trueMpr = 0
        self._originalMpr = 0
        # 魔法防御和魔法攻击计算
        self._baseMr = 0
        self._originalMr = 0
        self._baseSp = 0
        self._originalSp = 0
        # 闪避计算
        self._baseEr = 0
        self._originalEr = 0
        # 重量减免 伤害减免 魔法消耗减免
        self._weightReduction = 0
        self._originalStrWeightReduction = 0
        self._originalConWeightReduction = 0
        self._damageReductionByArmor = 0
        self._originalMagicConsumeReduction = 0
        # 角色当前使用武器
        self._weapon = None
        self._weaponType = 0 # 武器类型,返回给客户端用于决定角色装备武器时的样子(弓 单手剑 双手剑 匕首)
        # 其他属性
        self._netConnection = None
        self._accountName = ''
        self._skillList = []
        self._birthday = time.time()
        self._highLevel = 0
        self._classId = 0
        self._sex = 0
        self._type = 0
        self._food = 40
        self._clanid = 0
        self._clanname = ''
        self._clanRank = 0
        self._bonusStats = 0
        self._elfAttr = 0
        self._PKcount = 0
        self._PkCountForElf = 0
        self._expRes = 0
        self._partnerId = 0
        self._accessLevel = 0
        self._gm = False
        self._monitor = False
        self._onlineStatus = 0
        self._homeTownId = 0
        self._contribution = 0
        self._hellTime = 0
        self._banned = 0
        self._karma = Karma()
        self._lastPk = None
        self._lastPkForElf = None
        self._deleteTime = None
        self._lastActive = time.time()
        self._ainZone = 0
        self._ainPoint = 0
        self._moveSpeed = 0
        self._braveSpeed = 0
        self._gmInvis = False
        self._tempCharGfxAtDead = 0
        self._ghost = False # 幽灵之家游戏
        self._isInCharReset = False
        self._gc = None
        self._inventory = PcInventory(self)
        self._dwarf = DwarfInventory(self)
        self._dwarfForElf = DwarfForElfInventory(self)
        self._equipSlot = EquipmentSlot(self)
        self._party = None
        self._isTeleport = False # 是否在瞬间移动
        self._hasteItemEquipped = 0

    # ============================================================角色力量、敏捷、体质、智力、精神、魅力属性计算============================================================
    def addBaseStr(self, i):
        '''
        角色基础力量属性值,_baseStr对应characters的str字段,在人物创建 人物初始化或使用万能药水以及50级后属性奖励时会调用此函数更新_baseStr,即_baseStr = _originalStr + 力量万能药水 + 50级升级奖励力量属性
        :param i:增加的力量属性值(int)
        :return:None
        '''
        i += self._baseStr
        i = IntRange.ensure(i, 1, 127)
        self.addStr(i - self._baseStr)
        self._baseStr = i

    def addBaseCon(self, i):
        i += self._baseCon
        i = IntRange.ensure(i, 1, 127)
        self.addCon(i - self._baseCon)
        self._baseCon = i

    def addBaseDex(self, i):
        i += self._baseDex
        i = IntRange.ensure(i, 1, 127)
        self.addDex(i - self._baseDex)
        self._baseDex = i

    def addBaseCha(self, i):
        i += self._baseCha
        i = IntRange.ensure(i, 1, 127)
        self.addCha(i - self._baseCha)
        self._baseCha = i

    def addBaseInt(self, i):
        i += self._baseInt
        i = IntRange.ensure(i, 1, 127)
        self.addInt(i - self._baseInt)
        self._baseInt = i

    def addBaseWis(self, i):
        i += self._baseWis
        i = IntRange.ensure(i, 1, 127)
        self.addWis(i - self._baseWis)
        self._baseWis = i

    # ====================================================近战/远程伤害加成 近战/远程命中加成 魔法伤害加成 魔法命中加成 魔法暴击加成计算====================================================
    def resetBaseDmgup(self):
        '''
        计算因等级变化而产生的伤害加成变化,仅和自身等级有关
        :return:None
        '''
        newBaseDmgup = 0
        newBaseBowDmgup = 0
        if self.isKnight() or self.isDarkelf() or self.isDragonKnight():
            newBaseDmgup = int(self.getLevel() / 10)
            newBaseBowDmgup = 0
        elif self.isElf():
            newBaseDmgup = 0
            newBaseBowDmgup = int(self.getLevel() / 10)

        self.addDmgup(newBaseDmgup - self._baseDmgup)
        self.addBowDmgup(newBaseBowDmgup - self._baseBowDmgup)
        self._baseDmgup = newBaseDmgup
        self._baseBowDmgup = newBaseBowDmgup

    def resetOriginalDmgup(self):
        '''
        计算人物创建时的力量属性带来的近战伤害加成,仅和人物创建时的初始力量值有关
        :return:None
        '''
        originalStr = self._originalStr
        if self.isCrown():
            if originalStr >= 15 and originalStr <= 17:
                self._originalDmgup = 1
            elif originalStr >= 18:
                self._originalDmgup = 2
            else:
                self._originalDmgup = 0
        elif self.isKnight():
            if originalStr == 18 or originalStr == 19:
                self._originalDmgup = 2
            elif originalStr == 20:
                self._originalDmgup = 4
            else:
                self._originalDmgup = 0
        elif self.isElf():
            if originalStr == 12 or originalStr == 13:
                self._originalDmgup = 1
            elif originalStr >= 14:
                self._originalDmgup = 2
            else:
                self._originalDmgup = 0
        elif self.isDarkelf():
            if originalStr >= 14 and originalStr <= 17:
                self._originalDmgup = 1
            elif originalStr == 18:
                self._originalDmgup = 2
            else:
                self._originalDmgup = 0
        elif self.isWizard():
            if originalStr == 10 or originalStr == 11:
                self._originalDmgup = 1
            elif originalStr >= 12:
                self._originalDmgup = 2
            else:
                self._originalDmgup = 0
        elif self.isDragonKnight():
            if originalStr >= 15 and originalStr <= 17:
                self._originalDmgup = 1
            elif originalStr >= 18:
                self._originalDmgup = 3
            else:
                self._originalDmgup = 0
        elif self.isIllusionist():
            if originalStr == 13 or originalStr == 14:
                self._originalDmgup = 1
            elif originalStr >= 15:
                self._originalDmgup = 2
            else:
                self._originalDmgup = 0

    def resetOriginalBowDmgup(self):
        '''
        计算人物创建时的敏捷属性带来的远程伤害加成,仅和人物创建时的初始敏捷值有关
        :return:None
        '''
        originalDex = self._originalDex
        if self.isCrown():
            if originalDex >= 13:
                self._originalBowDmgup = 1
            else:
                self._originalBowDmgup = 0
        elif self.isKnight():
            self._originalBowDmgup = 0
        elif self.isElf():
            if originalDex >= 14 and originalDex <= 16:
                self._originalBowDmgup = 2
            elif originalDex >= 17:
                self._originalBowDmgup = 3
            else:
                self._originalBowDmgup = 0
        elif self.isDarkelf():
            if originalDex == 18:
                self._originalBowDmgup = 2
            else:
                self._originalBowDmgup = 0
        elif self.isWizard():
            self._originalBowDmgup = 0
        elif self.isDragonKnight():
            self._originalBowDmgup = 0
        elif self.isIllusionist():
            self._originalBowDmgup = 0

    def resetBaseHitup(self):
        '''
        计算因等级变化而产生的命中加成变化,仅和自身等级有关
        :return:None
        '''
        newBaseHitup = 0
        newBaseBowHitup = 0
        if self.isCrown():
            newBaseHitup = int(self.getLevel() / 5)
            newBaseBowHitup = int(self.getLevel() / 5)
        elif self.isKnight():
            newBaseHitup = int(self.getLevel() / 3)
            newBaseBowHitup = int(self.getLevel() / 3)
        elif self.isElf():
            newBaseHitup = int(self.getLevel() / 5)
            newBaseBowHitup = int(self.getLevel() / 5)
        elif self.isDarkelf():
            newBaseHitup = int(self.getLevel() / 3)
            newBaseBowHitup = int(self.getLevel() / 3)
        elif self.isDragonKnight():
            newBaseHitup = int(self.getLevel() / 3)
            newBaseBowHitup = int(self.getLevel() / 3)
        elif self.isIllusionist():
            newBaseHitup = int(self.getLevel() / 5)
            newBaseBowHitup = int(self.getLevel() / 5)

        self.addHitup(newBaseHitup - self._baseHitup)
        self.addBowHitup(newBaseBowHitup - self._baseBowHitup)
        self._baseHitup = newBaseHitup
        self._baseBowHitup = newBaseBowHitup

    def resetOriginalHitup(self):
        '''
        计算人物创建时的力量属性带来的近战命中加成,仅和人物创建时的初始力量值有关
        :return:None
        '''
        originalStr = self._originalStr
        if self.isCrown():
            if originalStr >= 16 and originalStr <= 18:
                self._originalHitup = 1
            elif originalStr >= 19:
                self._originalHitup = 2
            else:
                self._originalHitup = 0
        elif self.isKnight():
            if originalStr == 17 or originalStr == 18:
                self._originalHitup = 2
            elif originalStr >= 19:
                self._originalHitup = 4
            else:
                self._originalHitup = 0
        elif self.isElf():
            if originalStr == 13 and originalStr == 14:
                self._originalHitup = 1
            elif originalStr >= 15:
                self._originalHitup = 2
            else:
                self._originalHitup = 0
        elif self.isDarkelf():
            if originalStr >= 15 and originalStr <= 17:
                self._originalHitup = 1
            elif originalStr == 18:
                self._originalHitup = 2
            else:
                self._originalHitup = 0
        elif self.isWizard():
            if originalStr == 11 or originalStr == 12:
                self._originalHitup = 1
            elif originalStr >= 13:
                self._originalHitup = 2
            else:
                self._originalHitup = 0
        elif self.isDragonKnight():
            if originalStr >= 14 and originalStr <= 16:
                self._originalHitup = 1
            elif originalStr >= 17:
                self._originalHitup = 3
            else:
                self._originalHitup = 0
        elif self.isIllusionist():
            if originalStr == 12 or originalStr == 13:
                self._originalHitup = 1
            elif originalStr == 14 or originalStr == 15:
                self._originalHitup = 2
            elif originalStr == 16:
                self._originalHitup = 3
            elif originalStr >= 17:
                self._originalHitup = 4
            else:
                self._originalHitup = 0

    def resetOriginalBowHitup(self):
        '''
        计算人物创建时的敏捷属性带来的远程命中加成,仅和人物创建时的初始敏捷值有关
        :return:None
        '''
        originalDex = self._originalDex
        if self.isCrown():
            self._originalBowHitup = 0
        elif self.isKnight():
            self._originalBowHitup = 0
        elif self.isElf():
            if originalDex >= 13 and originalDex <= 15:
                self._originalBowHitup = 2
            elif originalDex >= 16:
                self._originalBowHitup = 3
            else:
                self._originalBowHitup = 0
        elif self.isDarkelf():
            if originalDex == 17:
                self._originalBowHitup = 1
            elif originalDex == 18:
                self._originalBowHitup = 2
            else:
                self._originalBowHitup = 0
        elif self.isWizard():
            self._originalBowHitup = 0
        elif self.isDragonKnight():
            self._originalBowHitup = 0
        elif self.isIllusionist():
            self._originalBowHitup = 0

    def resetOriginalMagicHit(self):
        '''
        计算人物创建时的智力属性带来的魔法命中加成,仅和人物创建时的初始智力值有关
        :return:None
        '''
        originalInt = self._originalInt
        if self.isCrown():
            if originalInt == 12 or originalInt == 13:
                self._originalMagicHit = 1
            elif originalInt >= 14:
                self._originalMagicHit = 2
            else:
                self._originalMagicHit = 0
        elif self.isKnight():
            if originalInt == 10 or originalInt == 11:
                self._originalMagicHit = 1
            elif originalInt == 12:
                self._originalMagicHit = 2
            else:
                self._originalMagicHit = 0
        elif self.isElf():
            if originalInt == 13 or originalInt == 14:
                self._originalMagicHit = 1
            elif originalInt >= 15:
                self._originalMagicHit = 2
            else:
                self._originalMagicHit = 0
        elif self.isDarkelf():
            if originalInt == 12 or originalInt == 13:
                self._originalMagicHit = 1
            elif originalInt >= 14:
                self._originalMagicHit = 2
            else:
                self._originalMagicHit = 0
        elif self.isWizard():
            if originalInt >= 14:
                self._originalMagicHit = 1
            else:
                self._originalMagicHit = 0
        elif self.isDragonKnight():
            if originalInt == 12 or originalInt == 13:
                self._originalMagicHit = 2
            elif originalInt == 14 or originalInt == 15:
                self._originalMagicHit = 3
            elif originalInt >= 16:
                self._originalMagicHit = 4
            else:
                self._originalMagicHit = 0
        elif self.isIllusionist():
            if originalInt >= 13:
                self._originalMagicHit = 1
            else:
                self._originalMagicHit = 0

    def resetOriginalMagicDamage(self):
        '''
        计算人物创建时的智力属性带来的魔法伤害加成,仅和人物创建时的初始智力值有关
        :return:None
        '''
        originalInt = self._originalInt
        if self.isCrown():
            self._originalMagicDamage = 0
        elif self.isKnight():
            self._originalMagicDamage = 0
        elif self.isElf():
            self._originalMagicDamage = 0
        elif self.isDarkelf():
            self._originalMagicDamage = 0
        elif self.isWizard():
            if originalInt >= 13:
                self._originalMagicDamage = 1
            else:
                self._originalMagicDamage = 0
        elif self.isDragonKnight():
            if originalInt == 13 or originalInt == 14:
                self._originalMagicDamage = 1
            elif originalInt == 15 or originalInt == 16:
                self._originalMagicDamage = 2
            elif originalInt == 17:
                self._originalMagicDamage = 3
            else:
                self._originalMagicDamage = 0
        elif self.isIllusionist():
            if originalInt == 16:
                self._originalMagicDamage = 1
            elif originalInt == 17:
                self._originalMagicDamage = 2
            else:
                self._originalMagicDamage = 0

    def resetOriginalMagicCritical(self):
        '''
        计算人物创建时的智力属性带来的魔法暴击加成,仅和人物创建时的初始智力值有关
        :return:None
        '''
        originalInt = self._originalInt
        if self.isCrown():
            self._originalMagicCritical = 0
        elif self.isKnight():
            self._originalMagicCritical = 0
        elif self.isElf():
            if originalInt == 14 or originalInt == 15:
                self._originalMagicCritical = 2
            elif originalInt >= 16:
                self._originalMagicCritical = 4
            else:
                self._originalMagicCritical = 0
        elif self.isDarkelf():
            self._originalMagicCritical = 0
        elif self.isWizard():
            if originalInt == 15:
                self._originalMagicCritical = 2
            elif originalInt == 16:
                self._originalMagicCritical = 4
            elif originalInt == 17:
                self._originalMagicCritical = 6
            elif originalInt == 18:
                self._originalMagicCritical = 8
            else:
                self._originalMagicCritical = 0
        elif self.isDragonKnight():
            self._originalMagicCritical = 0
        elif self.isIllusionist():
            self._originalMagicCritical = 0

    # ====================================================================防御计算===================================================================
    def resetBaseAc(self):
        '''
        计算因等级变化而产生的防御值变化,仅和自身敏捷值有关,而装备和魔法加成的敏捷值无关
        :return:None
        '''
        newAc = CalcStat.calcAc(self.getLevel(), self._baseDex)
        self.addAc(newAc - self._baseAc)
        self._baseAc = newAc

    def resetOriginalAc(self):
        '''
        计算人物创建时的敏捷属性带来的防御加成,仅和人物创建时的初始敏捷值有关
        :return:None
        '''
        originalDex = self._originalDex
        if self.isCrown():
            if originalDex >= 12 and originalDex <=14:
                self._originalAc = 1
            elif originalDex == 15 or originalDex == 16:
                self._originalAc = 2
            elif originalDex >= 17:
                self._originalAc = 3
            else:
                self._originalAc = 0
        elif self.isKnight():
            if originalDex == 13 or originalDex == 14:
                self._originalAc = 1
            elif originalDex >= 15:
                self._originalAc = 3
            else:
                self._originalAc = 0
        elif self.isElf():
            if originalDex >= 15 and originalDex <= 17:
                self._originalAc = 1
            elif originalDex == 18:
                self._originalAc = 2
            else:
                self._originalAc = 0
        elif self.isDarkelf():
            if originalDex >= 17:
                self._originalAc = 1
            else:
                self._originalAc = 0
        elif self.isWizard():
            if originalDex == 8 or originalDex == 9:
                self._originalAc = 1
            elif originalDex >= 10:
                self._originalAc = 2
            else:
                self._originalAc = 0
        elif self.isDragonKnight():
            if originalDex == 12 or originalDex == 13:
                self._originalAc = 1
            elif originalDex >= 14:
                self._originalAc = 2
            else:
                self._originalAc = 0
        elif self.isIllusionist():
            if originalDex == 11 or originalDex == 12:
                self._originalAc = 1
            elif originalDex >= 13:
                self._originalAc = 2
            else:
                self._originalAc = 0

        self.addAc(0- self._originalAc)

    # ============================================================角色血量和魔量计算============================================================
    def setCurrentHp(self, i):
        '''
        设置角色当前血量,并返回血量更新消息到客户端
        :param i:血量值(int)
        :return:None
        '''
        if self._currentHp == i:
            return

        Character.setCurrentHp(self, i)
        self.sendPackets(S_HPUpdate(self))

    def addBaseMaxHp(self, i):
        '''
        角色基础血量上限计算,_baseMaxHp对应characters的MaxHp字段,在人物创建或重置初始化时以及角色升级/降级时会调用此函数更新_baseMaxHp,即_baseMaxHp = random(_originalHpup) + 等级产生的血量
        :param i:血量上限增加值(int)
        :return:None
        '''
        i += self._baseMaxHp
        i = IntRange.ensure(i, 1, 32767)
        self.addMaxHp(i - self._baseMaxHp)
        self._baseMaxHp = i

    def resetOriginalHpup(self):
        '''
        计算人物创建时的体质属性带来的血量加成,仅和人物创建时的初始体质值有关
        :return:None
        '''
        originalCon = self._originalCon
        if self.isCrown():
            if originalCon == 12 or originalCon == 13:
                self._originalHpup = 1
            elif originalCon == 14 or originalCon == 15:
                self._originalHpup = 2
            elif originalCon >= 16:
                self._originalHpup = 3
            else:
                self._originalHpup = 0
        elif self.isKnight():
            if originalCon == 15 or originalCon == 16:
                self._originalHpup = 1
            elif originalCon >= 17:
                self._originalHpup = 3
            else:
                self._originalHpup = 0
        elif self.isElf():
            if originalCon >= 13 and originalCon <= 17:
                self._originalHpup = 1
            elif originalCon == 18:
                self._originalHpup = 2
            else:
                self._originalHpup = 0
        elif self.isDarkelf():
            if originalCon == 10 or originalCon == 11:
                self._originalHpup = 1
            elif originalCon >= 12:
                self._originalHpup = 2
            else:
                self._originalHpup = 0
        elif self.isWizard():
            if originalCon == 14 or originalCon == 15:
                self._originalHpup = 1
            elif originalCon >= 16:
                self._originalHpup = 2
            else:
                self._originalHpup = 0
        elif self.isDragonKnight():
            if originalCon == 15 or originalCon == 16:
                self._originalHpup = 1
            elif originalCon >= 17:
                self._originalHpup = 3
            else:
                self._originalHpup = 0
        elif self.isIllusionist():
            if originalCon == 13 or originalCon == 14:
                self._originalHpup = 1
            elif originalCon >= 15:
                self._originalHpup = 2
            else:
                self._originalHpup = 0

    def setCurrentMp(self, i):
        '''
        设置角色当前魔量,并返回魔量更新消息到客户端
        :param i:魔量值(int)
        :return:None
        '''
        if self._currentMp == i:
            return

        Character.setCurrentMp(self, i)
        self.sendPackets(S_MPUpdate(self))

    def addBaseMaxMp(self, i):
        '''
        角色基础魔量上限计算,_baseMaxMp对应characters的MaxMp字段,在人物创建或重置初始化时以及角色升级/降级时会调用此函数更新_baseMaxMp,即_baseMaxMp = random(_originalMpup) + 等级产生的魔量
        :param i:魔量上限增加值(int)
        :return:None
        '''
        i += self._baseMaxMp
        i = IntRange.ensure(i, 1, 32767)
        self.addMaxMp(i - self._baseMaxMp)
        self._baseMaxMp = i

    def resetOriginalMpup(self):
        '''
        计算人物创建时的精神属性带来的魔量加成,仅和人物创建时的初始精神值有关
        :return:None
        '''
        originalWis = self._originalWis
        if self.isCrown():
            if originalWis >= 16:
                self._originalMpup = 1
            else:
                self._originalMpup = 0
        elif self.isKnight():
            self._originalMpup = 0
        elif self.isElf():
            if originalWis >= 14 and originalWis <= 16:
                self._originalMpup = 1
            elif originalWis >= 17:
                self._originalMpup = 2
            else:
                self._originalMpup = 0
        elif self.isDarkelf():
            if originalWis >= 12:
                self._originalMpup = 1
            else:
                self._originalMpup = 0
        elif self.isWizard():
            if originalWis >= 13 and originalWis <= 16:
                self._originalMpup = 1
            elif originalWis >= 17:
                self._originalHpup = 2
            else:
                self._originalMpup = 0
        elif self.isDragonKnight():
            if originalWis >= 13 and originalWis <= 15:
                self._originalMpup = 1
            elif originalWis >= 16:
                self._originalMpup = 2
            else:
                self._originalMpup = 0
        elif self.isIllusionist():
            if originalWis >= 13 and originalWis <= 15:
                self._originalMpup = 1
            elif originalWis >= 16:
                self._originalMpup = 2
            else:
                self._originalMpup = 0

    # ============================================================角色体力回复量和魔力回复量计算============================================================
    def addHpr(self, i):
        '''
        角色体力回复量计算,_trueHpr对应角色当前最大体力回复值,在装备/脱下套装时会调用此函数更新_trueHpr,即_trueHpr = 套装的体力回复量,不包含_originalHpr,因为套装产生的回血量不受饱食度影响(_hpr就是_trueHpr的有效值)
        :param i:套装增加/减少的体力回复量
        :return:None
        '''
        self._trueHpr += i
        self._hpr = max(0, self._trueHpr)

    def resetOriginalHpr(self):
        '''
        计算人物创建时的体质属性带来的体力回复量加成,仅和人物创建时的初始体质值有关
        :return:None
        '''
        originalCon = self._originalCon
        if self.isCrown():
            if originalCon == 13 or originalCon == 14:
                self._originalHpr = 1
            elif originalCon == 15 or originalCon == 16:
                self._originalHpr = 2
            elif originalCon == 17:
                self._originalHpr = 3
            elif originalCon == 18:
                self._originalHpr = 4
            else:
                self._originalHpr = 0
        elif self.isKnight():
            if originalCon == 16 or originalCon == 17:
                self._originalHpr = 2
            elif originalCon == 18:
                self._originalHpr = 4
            else:
                self._originalHpr = 0
        elif self.isElf():
            if originalCon == 14 or originalCon == 15:
                self._originalHpr = 1
            elif originalCon == 16:
                self._originalHpr = 2
            elif originalCon >= 17:
                self._originalHpr = 3
            else:
                self._originalHpr = 0
        elif self.isDarkelf():
            if originalCon == 11 or originalCon == 12:
                self._originalHpr = 1
            elif originalCon >= 13:
                self._originalHpr = 2
            else:
                self._originalHpr = 0
        elif self.isWizard():
            if originalCon == 17:
                self._originalHpr = 1
            elif originalCon == 18:
                self._originalHpr = 2
            else:
                self._originalHpr = 0
        elif self.isDragonKnight():
            if originalCon == 16 or originalCon == 17:
                self._originalHpr = 1
            elif originalCon == 18:
                self._originalHpr = 3
            else:
                self._originalHpr = 0
        elif self.isIllusionist():
            if originalCon == 14 or originalCon == 15:
                self._originalHpr = 1
            elif originalCon >= 16:
                self._originalHpr = 2
            else:
                self._originalHpr = 0

    def addMpr(self, i):
        '''
        角色魔力回复量计算,_trueMpr对应角色当前最大魔力回复值,在装备/脱下套装时会调用此函数更新_trueMpr,即_trueMpr = 套装的魔力回复量,不包含_originalMpr,因为套装产生的回魔量不受饱食度影响(_mpr就是_trueMpr的有效值)
        :param i:套装增加/减少的魔力回复量
        :return:None
        '''
        self._trueMpr += i
        self._mpr = max(0, self._trueMpr)

    def resetOriginalMpr(self):
        '''
        计算人物创建时的精神属性带来的魔力回复量加成,仅和人物创建时的初始精神值有关
        :return:None
        '''
        originalWis = self._originalWis
        if self.isCrown():
            if originalWis == 13 or originalWis == 14:
                self._originalMpr = 1
            elif originalWis >= 15:
                self._originalMpr = 2
            else:
                self._originalMpr = 0
        elif self.isKnight():
            if originalWis == 11 or originalWis == 12:
                self._originalMpr = 1
            elif originalWis == 13:
                self._originalMpr = 2
            else:
                self._originalMpr = 0
        elif self.isElf():
            if originalWis >= 15 or originalWis <= 17:
                self._originalMpr = 1
            elif originalWis == 18:
                self._originalMpr = 2
            else:
                self._originalMpr = 0
        elif self.isDarkelf():
            if originalWis >= 13:
                self._originalMpr = 1
            else:
                self._originalMpr = 0
        elif self.isWizard():
            if originalWis == 14 or originalWis == 15:
                self._originalMpr = 1
            elif originalWis == 16 or originalWis == 17:
                self._originalMpr = 2
            elif originalWis == 18:
                self._originalMpr = 3
            else:
                self._originalMpr = 0
        elif self.isDragonKnight():
            if originalWis == 15 or originalWis == 16:
                self._originalMpr = 1
            elif originalWis >= 17:
                self._originalMpr = 2
            else:
                self._originalMpr = 0
        elif self.isIllusionist():
            if originalWis >= 14 and originalWis <= 16:
                self._originalMpr = 1
            elif originalWis >= 17:
                self._originalMpr = 2
            else:
                self._originalMpr = 0

    # ================================================================魔法防御和魔法攻击计算================================================================
    def resetBaseMr(self):
        '''
        计算因等级变化而产生的魔法防御值变化,受自身精神值以及装备和魔法加成的精神值影响
        :return:None
        '''
        newMr = 0
        if self.isCrown():
            newMr = 10
        elif self.isElf():
            newMr = 25
        elif self.isWizard():
            newMr = 15
        elif self.isDarkelf():
            newMr = 10
        elif self.isDragonKnight():
            newMr = 18
        elif self.isIllusionist():
            newMr = 20

        newMr += CalcStat.calcStatMr(self._wis)
        newMr += int(self.getLevel() / 2)
        self.addMr(newMr - self._baseMr)
        self._baseMr = newMr

    def resetOriginalMr(self):
        '''
        计算人物创建时的精神属性带来的魔力回复量加成,仅和人物创建时的初始精神值有关
        :return:None
        '''
        originalWis = self._originalWis
        if self.isCrown():
            if originalWis == 12 or originalWis == 13:
                self._originalMr = 1
            elif originalWis >= 14:
                self._originalMr = 2
            else:
                self._originalMr = 0
        elif self.isKnight():
            if originalWis == 10 or originalWis == 11:
                self._originalMr = 1
            elif originalWis >= 12:
                self._originalMr = 2
            else:
                self._originalMr = 0
        elif self.isElf():
            if originalWis >= 13 and originalWis <= 15:
                self._originalMr = 1
            elif originalWis >= 16:
                self._originalMr = 2
            else:
                self._originalMr = 0
        elif self.isDarkelf():
            if originalWis >= 11 and originalWis <= 13:
                self._originalMr = 1
            elif originalWis == 14:
                self._originalMr = 2
            elif originalWis == 15:
                self._originalMr = 3
            elif originalWis >= 16:
                self._originalMr = 4
            else:
                self._originalMr = 0
        elif self.isWizard():
            if originalWis >= 15:
                self._originalMr = 1
            else:
                self._originalMr = 0
        elif self.isDragonKnight():
            if originalWis >= 14:
                self._originalMr = 2
            else:
                self._originalMr = 0
        elif self.isIllusionist():
            if originalWis >= 15 and originalWis <= 17:
                self._originalMr = 2
            elif originalWis == 18:
                self._originalMr = 4
            else:
                self._originalMr = 0

        self.addMr(self._originalMr)

    def resetBaseSp(self):
        '''
        计算因等级变化而产生的魔法攻击值变化,受自身智力值以及装备和魔法加成的智力值影响
        :return:None
        '''
        newSp = 0
        newSp += CalcStat.calcStatSp(self._int)
        newSp += int(self.getLevel() / 4)
        self.addSp(newSp - self._baseSp)
        self._baseSp = newSp

    # ====================================================================闪避计算====================================================================
    def resetBaseEr(self):
        '''
        计算因等级变化而产生的闪避值变化,仅和自身敏捷值有关,而装备和魔法加成的敏捷值无关
        :return:None
        '''
        newEr = 0
        if self.isKnight():
            newEr = int(self.getLevel() / 4)
        elif self.isCrown() or self.isElf():
            newEr = int(self.getLevel() / 8)
        elif self.isDarkelf():
            newEr = int(self.getLevel() / 6)
        elif self.isWizard():
            newEr = int(self.getLevel() / 10)
        elif self.isDragonKnight():
            newEr = int(self.getLevel() / 7)
        elif self.isIllusionist():
            newEr = int(self.getLevel() / 9)
        newEr += int((self._dex - 8) / 2)
        self.addEr(newEr - self._baseEr)
        self._baseEr = newEr

    def resetOriginalEr(self):
        '''
        计算人物创建时的敏捷属性带来的闪避加成,仅和人物创建时的初始敏捷值有关
        :return:None
        '''
        originalDex = self._originalDex
        if self.isCrown():
            if originalDex == 14 or originalDex == 15:
                self._originalEr = 1
            elif originalDex == 16 or originalDex == 17:
                self._originalEr = 2
            elif originalDex == 18:
                self._originalEr = 3
            else:
                self._originalEr = 0
        elif self.isKnight():
            if originalDex == 14 or originalDex == 15:
                self._originalEr = 1
            elif originalDex == 16:
                self._originalEr = 3
            else:
                self._originalEr = 0
        elif self.isElf():
            self._originalEr = 0
        elif self.isDarkelf():
            if originalDex >= 16:
                self._originalEr = 2
            else:
                self._originalEr = 0
        elif self.isWizard():
            if originalDex == 9 or originalDex == 10:
                self._originalEr = 1
            elif originalDex == 11:
                self._originalEr = 2
            else:
                self._originalEr = 0
        elif self.isDragonKnight():
            if originalDex == 13 or originalDex == 14:
                self._originalEr = 1
            elif originalDex >= 15:
                self._originalEr = 2
            else:
                self._originalEr = 0
        elif self.isIllusionist():
            if originalDex == 12 or originalDex == 13:
                self._originalEr = 1
            elif originalDex >= 14:
                self._originalEr = 2
            else:
                self._originalEr = 0

        self.addEr(self._originalEr)

    # ============================================================负重减免 伤害减免 魔法消耗减免============================================================
    def resetOriginalStrWeightReduction(self):
        '''
        计算人物创建时的力量属性带来的负重减免,仅和人物创建时的初始力量值有关
        :return:None
        '''
        originalStr = self._originalStr
        if self.isCrown():
            if originalStr >= 14 and originalStr <= 16:
                self._originalStrWeightReduction = 1
            elif originalStr >= 17 and originalStr <= 19:
                self._originalStrWeightReduction = 2
            elif originalStr == 20:
                self._originalStrWeightReduction = 3
            else:
                self._originalStrWeightReduction = 0
        elif self.isKnight():
            self._originalStrWeightReduction = 0
        elif self.isElf():
            if originalStr >= 16:
                self._originalStrWeightReduction = 2
            else:
                self._originalStrWeightReduction = 0
        elif self.isDarkelf():
            if originalStr >= 13 and originalStr <= 15:
                self._originalStrWeightReduction = 2
            elif originalStr >= 16:
                self._originalStrWeightReduction = 3
            else:
                self._originalStrWeightReduction = 0
        elif self.isWizard():
            if originalStr >= 9:
                self._originalStrWeightReduction = 1
            else:
                self._originalStrWeightReduction = 0
        elif self.isDragonKnight():
            if originalStr >= 16:
                self._originalStrWeightReduction = 1
            else:
                self._originalStrWeightReduction = 0
        elif self.isIllusionist():
            if originalStr == 18:
                self._originalStrWeightReduction = 1
            else:
                self._originalStrWeightReduction = 0

    def resetOriginalConWeightReduction(self):
        '''
        计算人物创建时的体质属性带来的负重减免,仅和人物创建时的初始体质值有关
        :return:None
        '''
        originalCon = self._originalCon
        if self.isCrown():
            if originalCon >= 11:
                self._originalConWeightReduction = 1
            else:
                self._originalConWeightReduction = 0
        elif self.isKnight():
            if originalCon >= 15:
                self._originalConWeightReduction = 1
            else:
                self._originalConWeightReduction = 0
        elif self.isElf():
            if originalCon >= 15:
                self._originalConWeightReduction = 2
            else:
                self._originalConWeightReduction = 0
        elif self.isDarkelf():
            if originalCon >= 9:
                self._originalConWeightReduction = 1
            else:
                self._originalConWeightReduction = 0
        elif self.isWizard():
            if originalCon == 13 or originalCon == 14:
                self._originalConWeightReduction = 1
            elif originalCon >= 15:
                self._originalConWeightReduction = 2
            else:
                self._originalConWeightReduction = 0
        elif self.isDragonKnight():
            self._originalConWeightReduction = 0
        elif self.isIllusionist():
            if originalCon == 17:
                self._originalConWeightReduction = 1
            elif originalCon == 18:
                self._originalConWeightReduction = 2
            else:
                self._originalConWeightReduction = 0

    def resetOriginalMagicConsumeReduction(self):
        '''
        计算人物创建时的智力属性带来的魔力消耗减免,仅和人物创建时的初始智力值有关
        :return:None
        '''
        originalInt = self._originalInt
        if self.isCrown():
            if originalInt == 11 or originalInt == 12:
                self._originalMagicConsumeReduction = 1
            elif originalInt >= 13:
                self._originalMagicConsumeReduction = 2
            else:
                self._originalMagicConsumeReduction = 0
        elif self.isKnight():
            if originalInt == 9 or originalInt == 10:
                self._originalMagicConsumeReduction = 1
            elif originalInt >= 11:
                self._originalMagicConsumeReduction = 2
            else:
                self._originalMagicConsumeReduction = 0
        elif self.isElf():
            self._originalMagicConsumeReduction = 0
        elif self.isDarkelf():
            if originalInt == 13 or originalInt == 14:
                self._originalMagicConsumeReduction = 1
            elif originalInt >= 15:
                self._originalMagicConsumeReduction = 2
            else:
                self._originalMagicConsumeReduction = 0
        elif self.isWizard():
            self._originalMagicConsumeReduction = 0
        elif self.isDragonKnight():
            self._originalMagicConsumeReduction = 0
        elif self.isIllusionist():
            if originalInt == 14:
                self._originalMagicConsumeReduction = 1
            elif originalInt >= 15:
                self._originalMagicConsumeReduction = 2
            else:
                self._originalMagicConsumeReduction = 0

    # ======================================================================其他属性=====================================================================
    def refresh(self):
        self.resetLevel()
        # 命中、伤害
        self.resetBaseDmgup()
        self.resetOriginalDmgup()
        self.resetOriginalBowDmgup()
        self.resetBaseHitup()
        self.resetOriginalHitup()
        self.resetOriginalBowHitup()
        self.resetOriginalMagicHit()
        self.resetOriginalMagicDamage()
        self.resetOriginalMagicCritical()
        # 防御
        self.resetBaseAc()
        self.resetOriginalAc()
        # 血量、魔量
        self.resetOriginalHpup()
        self.resetOriginalMpup()
        # 体力回复量、魔力回复量
        self.resetOriginalHpr()
        self.resetOriginalMpr()
        # 魔法防御、魔法攻击
        self.resetBaseMr()
        self.resetOriginalMr()
        self.resetBaseSp()
        # 闪避
        self.resetBaseEr()
        self.resetOriginalEr()
        # 重量减免、伤害减免、魔法消耗减免
        self.resetOriginalStrWeightReduction()
        self.resetOriginalConWeightReduction()
        self.resetOriginalMagicConsumeReduction()

    def setSkillMastery(self, skillid):
        if skillid not in self._skillList:
            self._skillList.append(skillid)

    def removeSkillMastery(self, skillid):
        if skillid in self._skillList:
            self._skillList.remove(skillid)

    def isSkillMastery(self, skillid):
        return (skillid in self._skillList)

    def clearSkillMastery(self):
        self._skillList = []

    def getSimpleBirthday(self):
        dt = datetime.fromtimestamp(self._birthday).date().timetuple()
        return int(time.mktime(dt))

    def logout(self):
        pass

    def getMaxWeight(self):
        '''
        获取玩家最大负重量
        :return:负重量(double)
        '''
        str = self._str
        con = self._con
        maxWeight = 150 * math.floor(0.6 * str + 0.4 * con + 1)
        weightReductionByArmor = self._weightReduction / 100
        # todo: 娃娃系统
        weightReductionByDoll = 0
        # todo: 魔法系统
        weightReductionByMagic = 0
        # 角色初始力量和体制提供的负重倍率
        originalWeightReduction = 0
        originalWeightReduction += 0.04 * (self._originalStrWeightReduction + self._originalConWeightReduction)
        weightReduction = 1 + weightReductionByArmor + weightReductionByDoll + originalWeightReduction

        maxWeight *= weightReduction
        maxWeight += weightReductionByMagic
        maxWeight *= Config.getint('rates', 'RateWeightLimit')

        return maxWeight

    def turnOnOffLight(self):
        # todo: 照明
        return

    def resetLevel(self):
        # todo: 等级计算
        return

    def isCrown(self):
        return (self._classId == CLASSID_PRINCE or self._classId == CLASSID_PRINCESS)

    def isKnight(self):
        return (self._classId == CLASSID_KNIGHT_MALE or self._classId == CLASSID_KNIGHT_FEMALE)

    def isElf(self):
        return (self._classId == CLASSID_ELF_MALE or self._classId == CLASSID_ELF_FEMALE)

    def isWizard(self):
        return (self._classId == CLASSID_WIZARD_MALE or self._classId == CLASSID_WIZARD_FEMALE)

    def isDarkelf(self):
        return (self._classId == CLASSID_DARK_ELF_MALE or self._classId == CLASSID_DARK_ELF_FEMALE)

    def isDragonKnight(self):
        return (self._classId == CLASSID_DRAGON_KNIGHT_MALE or self._classId == CLASSID_DRAGON_KNIGHT_FEMALE)

    def isIllusionist(self):
        return (self._classId == CLASSID_ILLUSIONIST_MALE or self._classId == CLASSID_ILLUSIONIST_FEMALE)

    def save(self):
        return

    def delInvis(self):
        return

    def sendPackets(self, serverbasepacket):
        if not self._netConnection:
            return
        try:
            self._netConnection.sendPacket(serverbasepacket)
        except Exception as e:
            logging.error(e)

    def getExp(self):
        with self._lock:
            return self._exp

    def setExp(self, exp):
        with self._lock:
            self._exp = exp

    '''
    def beginGameTimeCarrier(self):
        if not self._gc:
            self._gc = GameTimeCarrier(self)
            self._gc.start()

    def save(self):
        from server.datatables.CharacterTable import CharacterTable
        if self._ghost:
            return

        if self._isInCharReset:
            return

        CharacterTable().storeCharacter(self)
    '''