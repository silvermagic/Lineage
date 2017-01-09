# -*- coding: utf-8 -*-

from server.datatables.ArmorSetTable import ArmorSetTable
from server.model.skill import SkillId
from server.model.PolyMorph import PolyMorph
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.utils.Singleton import Singleton

class ArmorSet:
    __metaclass__ = Singleton
    def __init__(self):
        self._allSet = []
        self.loadArmorSet()

    def loadArmorSet(self):
        for armorSet in ArmorSetTable()._armorSetList:
            item = ArmorSetEffect()
            item._id = armorSet._id
            item._ids = map(int, armorSet._sets.split(','))
            item._polyId = armorSet._polyId
            item._ac = armorSet._ac
            item._addHp = armorSet._hp
            item._addMp = armorSet._mp
            item._regenHp = armorSet._hpr
            item._regenMp = armorSet._mpr
            item._addMr = armorSet._mr
            item._str = armorSet._str
            item._dex = armorSet._dex
            item._con = armorSet._con
            item._wis = armorSet._wis
            item._cha = armorSet._cha
            item._int = armorSet._int
            item._defenseWater = armorSet._defenseWater
            item._defenseWind = armorSet._defenseWind
            item._defenseFire = armorSet._defenseFire
            item._defenseEarth = armorSet._defenseEarth
            self._allSet.append(item)

class ArmorSetEffect:
    def __init__(self):
        self._id = 0
        self._ids = []
        # 套装变身
        self._polyId = 0
        # 防御和血魔加成
        self._ac = 0
        self._addHp = 0
        self._addMp = 0
        self._regenHp = 0
        self._regenMp = 0
        self._addMr = 0
        # 属性值加成
        self._str = 0
        self._dex = 0
        self._con = 0
        self._wis = 0
        self._cha = 0
        self._int = 0
        # 属性防御加成
        self._defenseWater = 0
        self._defenseWind = 0
        self._defenseFire = 0
        self._defenseEarth = 0

    def isValid(self, pc):
        return pc._inventory.checkEquipped(self._ids)

    def isPartOfSet(self, id):
        '''
        判断道具是否属于套装配件
        :param id:道具模板标识(int)
        :return:True/False
        '''
        return (id in self._ids)

    def isEquippedRingOfArmorSet(self, pc, ring):
        '''
        判断套装是否需要装备特定戒子,如果套装包含戒子,那么必须装备一对戒子才能使套装生效
        :param pc:玩家角色(PcInstance)
        :param ring:套装戒子(ItemInstance)
        :return:True/False
        '''
        itemId = ring._item._itemId
        if pc._inventory.getTypeEquipped(2, 9) == 2: # 装备了两个戒子
            rings = pc._inventory.getRingEquipped()
            if rings[0]._item._itemId == itemId and rings[1]._item._itemId == itemId:
                return True

        return False

    def isRemainderOfCharge(self, pc):
        if pc._inventory.checkItem(20383, 1):
            item = pc._inventory.findItemId(20383)
            if item:
                if item._chargeCount != 0:
                    return True
        return False

    def giveEffect(self, pc):
        # 防御和血魔加成
        pc.addAc(self._ac)
        pc.addMaxHp(self._addHp)
        pc.addMaxMp(self._addMp)
        pc.addHpr(self._regenHp)
        pc.addMpr(self._regenMp)
        pc.addMr(self._addMr)
        # 属性值加成
        pc.addStr(self._str)
        pc.addDex(self._dex)
        pc.addCon(self._con)
        pc.addWis(self._wis)
        pc.addCha(self._cha)
        pc.addInt(self._int)
        # 属性防御加成
        pc.addWater(self._defenseWater)
        pc.addWind(self._defenseWind)
        pc.addFire(self._defenseFire)
        pc.addEarth(self._defenseEarth)
        # 套装变身
        awakeSkillId = pc._awakeSkillId
        if awakeSkillId in (SkillId.AWAKEN_ANTHARAS, SkillId.AWAKEN_FAFURION, SkillId.AWAKEN_VALAKAS):
            pc.sendPackets(S_ServerMessage(1384)) # 现在处于觉醒状态
            return
        if self._polyId == 6080 or self._polyId == 6094:
            if pc._sex == 0:
                self._polyId = 6094
            else:
                self._polyId = 6080
            if not self.isRemainderOfCharge(pc):
                return
        PolyMorph.doPoly(pc, self._polyId, 0, PolyMorph.MORPH_BY_ITEMMAGIC)

    def cancelEffect(self, pc):
        # 防御和血魔加成
        pc.addAc(-self._ac)
        pc.addMaxHp(-self._addHp)
        pc.addMaxMp(-self._addMp)
        pc.addHpr(-self._regenHp)
        pc.addMpr(-self._regenMp)
        pc.addMr(-self._addMr)
        # 属性值加成
        pc.addStr(-self._str)
        pc.addDex(-self._dex)
        pc.addCon(-self._con)
        pc.addWis(-self._wis)
        pc.addCha(-self._cha)
        pc.addInt(-self._int)
        # 属性防御加成
        pc.addWater(-self._defenseWater)
        pc.addWind(-self._defenseWind)
        pc.addFire(-self._defenseFire)
        pc.addEarth(-self._defenseEarth)
        # 套装变身
        awakeSkillId = pc._awakeSkillId
        if awakeSkillId in (SkillId.AWAKEN_ANTHARAS, SkillId.AWAKEN_FAFURION, SkillId.AWAKEN_VALAKAS):
            pc.sendPackets(S_ServerMessage(1384))  # 现在处于觉醒状态
            return
        if self._polyId == 6080:
            if pc._sex == 0:
                self._polyId = 6094
        if pc._tempCharGfx != self._polyId:
            return
        PolyMorph.undoPoly(pc)

    def __eq__(self, other):
        return self._id == other._id