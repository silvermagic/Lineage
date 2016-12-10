# -*- coding: utf-8 -*-

from server.datatables.SkillsTable import SkillsTable
from server.model.PcInventory import PcInventory
from server.serverpackets.S_Invis import S_Invis
from server.serverpackets.S_RemoveObject import S_RemoveObject
from server.serverpackets.S_Ability import S_Ability
from server.serverpackets.S_SPMR import S_SPMR
from server.serverpackets.S_SkillHaste import S_SkillHaste
from server.serverpackets.S_AddSkill import S_AddSkill
from server.serverpackets.S_DelSkill import S_DelSkill
from server.serverpackets.S_SkillBrave import S_SkillBrave
from skill import SkillId

class EquipmentSlot():
    def __init__(self, pc):
        self._owner = pc
        self._currentArmorSet = []
        self._armors = []

    def setWeapon(self, weapon):
        self._owner._weapon = weapon
        self._owner._weaponType = weapon._item._weaponType
        weapon.startEquipmentTimer(self._owner)

    def setArmor(self, armor):
        item = armor._item
        item_id = armor._itemId

        if item._clsType == 2 and item._type >=8 and item._type <= 12:
            self._owner.addAc(item.get_ac() - armor._acByMagic)
        else:
            self._owner.addAc(item.get_ac() - armor._enchantLevel - armor._acByMagic)

        self._owner._damageReductionByArmor += item.getDamageReduction()
        self._owner._weightReduction += item.getWeightReduction()
        self._owner._hitModifierByArmor += item.getHitModifierByArmor()
        self._owner._dmgModifierByArmor += item.getDmgModifierByArmor()
        self._owner._bowHitModifierByArmor += item.getBowHitModifierByArmor()
        self._owner._bowDmgModifierByArmor += item.getBowDmgModifierByArmor()
        self._owner.addEarth(item.get_defense_earth())
        self._owner.addWind(item.get_defense_wind())
        self._owner.addWater(item.get_defense_water())
        self._owner.addFire(item.get_defense_fire())
        self._owner.addRegistStun(item.get_regist_stun())
        self._owner.addRegistStone(item.get_regist_stone())
        self._owner.addRegistSleep(item.get_regist_sleep())
        self._owner.addRegistFreeze(item.get_regist_freeze())
        self._owner.addRegistSustain(item.get_regist_sustain())
        self._owner.addRegistBlind(item.get_regist_blind())
        self._owner.addEarth(item.get_defense_earth() + armor._EarthMr)
        self._owner.addWind(item.get_defense_wind() + armor._WindMr)
        self._owner.addWater(item.get_defense_water() + armor._WaterMr)
        self._owner.addFire(item.get_defense_fire() + armor._FireMr)
        self._armors.append(armor)

        # todo: 套装

        if item_id in (20077, # 炎魔的血光斗篷
                       20062, # 隐身斗篷
                       120077): # 受祝福的隐身斗篷
            if not self._owner.hasSkillEffect(SkillId.INVISIBILITY):
                self._owner.killSkillEffectTimer(SkillId.BLIND_HIDING)
                self._owner.setSkillEffect(SkillId.INVISIBILITY, 0)
                self._owner.sendPackets(S_Invis(self._owner._id, 1))
                self._owner.broadcastPacketForFindInvis(S_RemoveObject(self._owner), False)
        elif item_id == 20288:
            self._owner.sendPackets(S_Ability(1, True))
        elif item_id == 20383:
            if armor._chargeCount != 0:
                armor._chargeCount -= 1
                self._owner._inventory.updateItem(armor, PcInventory.COL_CHARGE_COUNT)

        armor.startEquipmentTimer(self._owner)

    def removeWeapon(self, weapon):
        self._owner._weapon = None
        self._owner._weaponType = 0
        weapon.stopEquipmentTimer(self._owner)
        if self._owner.hasSkillEffect(SkillId.COUNTER_BARRIER):
            self._owner.removeSkillEffect(SkillId.COUNTER_BARRIER)

    def removeArmor(self, armor):
        item = armor._item
        item_id = armor._itemId

        if item._clsType == 2 and item._type >= 8 and item._type <= 12:
            self._owner.addAc(-(item.get_ac() - armor._acByMagic))
        else:
            self._owner.addAc(-(item.get_ac() - armor._enchantLevel - armor._acByMagic))

        self._owner._damageReductionByArmor -= item.getDamageReduction()
        self._owner._weightReduction -= item.getWeightReduction()
        self._owner._hitModifierByArmor -= item.getHitModifierByArmor()
        self._owner._dmgModifierByArmor -= item.getDmgModifierByArmor()
        self._owner._bowHitModifierByArmor -= item.getBowHitModifierByArmor()
        self._owner._bowDmgModifierByArmor -= item.getBowDmgModifierByArmor()
        self._owner.addEarth(-item.get_defense_earth())
        self._owner.addWind(-item.get_defense_wind())
        self._owner.addWater(-item.get_defense_water())
        self._owner.addFire(-item.get_defense_fire())
        self._owner.addRegistStun(-item.get_regist_stun())
        self._owner.addRegistStone(-item.get_regist_stone())
        self._owner.addRegistSleep(-item.get_regist_sleep())
        self._owner.addRegistFreeze(-item.get_regist_freeze())
        self._owner.addRegistSustain(-item.get_regist_sustain())
        self._owner.addRegistBlind(-item.get_regist_blind())
        self._owner.addEarth(-item.get_defense_earth() - armor._EarthMr)
        self._owner.addWind(-item.get_defense_wind() - armor._WindMr)
        self._owner.addWater(-item.get_defense_water() - armor._WaterMr)
        self._owner.addFire(-item.get_defense_fire() - armor._FireMr)
        self._armors.remove(armor)

        # todo: 套装

        if item_id in (20077,  # 炎魔的血光斗篷
                       20062,  # 隐身斗篷
                       120077):  # 受祝福的隐身斗篷
            self._owner.delInvis()
        elif item_id == 20288:
            self._owner.sendPackets(S_Ability(1, False))

        armor.stopEquipmentTimer(self._owner)

    def set(self, equipment):
        item = equipment._item
        if item._clsType == 0:
            return

        if item._addhp != 0:
            self._owner.addMaxHp(item._addhp)
        if item._addmp != 0:
            self._owner.addMaxMp(item._addmp)
        if equipment._addHp != 0:
            self._owner.addMaxHp(equipment._addHp)
        if equipment._addMp != 0:
            self._owner.addMaxMp(equipment._addMp)

        self._owner.addStr(item._addstr)
        self._owner.addCon(item._addcon)
        self._owner.addDex(item._adddex)
        self._owner.addInt(item._addint)
        self._owner.addWis(item._addwis)
        if item._addwis != 0:
            self._owner.resetBaseMr()
        self._owner.addCha(item._addcha)

        addMr = 0
        addMr += equipment.getMr()
        if item._itemId == 20236 and self._owner.isElf():
            addMr += 5
        if addMr != 0:
            self._owner.addMr(addMr)
        if item._addsp != 0:
            self._owner.addSp(item._addsp)
        self._owner.sendPackets(S_SPMR(self._owner))

        if item._isHasteItem:
            self._owner._hasteItemEquipped += 1
            self._owner.removeHasteSkillEffect()
            if self._owner._moveSpeed != 1:
                self._owner._moveSpeed = 1
                self._owner.sendPackets(S_SkillHaste(self._owner._id, 1, -1))
                self._owner.broadcastPacket(S_SkillHaste(self._owner._id, 1, 0))

        if item._itemId == 20383:
            if self._owner.hasSkillEffect(SkillId.STATUS_BRAVE):
                self._owner.killSkillEffectTimer(SkillId.STATUS_BRAVE)
                self._owner.sendPackets(S_SkillBrave(self._owner._id, 0, 0))
                self._owner.broadcastPacket(S_SkillBrave(self._owner._id, 0, 0))
                self._owner._braveSpeed = 0

        self._owner._equipSlot.setMagicHelm(equipment)
        if item._clsType == 1:
            self.setWeapon(equipment)
        elif item._clsType == 2:
            self.setArmor(equipment)
            self._owner.sendPackets(S_SPMR(self._owner))

    def remove(self, equipment):
        item = equipment._item
        if item._clsType == 0:
            return

        if item._addhp != 0:
            self._owner.addMaxHp(-item._addhp)
        if item._addmp != 0:
            self._owner.addMaxMp(-item._addmp)
        if equipment._addHp != 0:
            self._owner.addMaxHp(-equipment._addHp)
        if equipment._addMp != 0:
            self._owner.addMaxMp(-equipment._addMp)

        self._owner.addStr(-item._addstr)
        self._owner.addCon(-item._addcon)
        self._owner.addDex(-item._adddex)
        self._owner.addInt(-item._addint)
        self._owner.addWis(-item._addwis)
        if item._addwis != 0:
            self._owner.resetBaseMr()
        self._owner.addCha(-item._addcha)

        addMr = 0
        addMr -= equipment.getMr()
        if item._itemId == 20236 and self._owner.isElf():
            addMr -= 5
        if addMr != 0:
            self._owner.addMr(addMr)
        if item._addsp != 0:
            self._owner.addSp(-item._addsp)
        self._owner.sendPackets(S_SPMR(self._owner))

        if item._isHasteItem:
            self._owner._hasteItemEquipped -= 1
            if self._owner._hasteItemEquipped == 0:
                self._owner._moveSpeed = 0
                self._owner.sendPackets(S_SkillHaste(self._owner._id, 0, 0))
                self._owner.broadcastPacket(S_SkillHaste(self._owner._id, 0, 0))

        self._owner._equipSlot.removeMagicHelm(self._owner._id, equipment)
        if item._clsType == 1:
            self.removeWeapon(equipment)
        elif item._clsType == 2:
            self.removeArmor(equipment)

    def setMagicHelm(self, item_inst):
        item_id = item_inst._itemId

        if item_id == 20013:
            self._owner.setSkillMastery(SkillId.PHYSICAL_ENCHANT_DEX)
            self._owner.setSkillMastery(SkillId.HASTE)
            self._owner.sendPackets(S_AddSkill(0, 0, 0, 2, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20014:
            self._owner.setSkillMastery(SkillId.HEAL)
            self._owner.setSkillMastery(SkillId.EXTRA_HEAL)
            self._owner.sendPackets(S_AddSkill(1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20015:
            self._owner.setSkillMastery(SkillId.ENCHANT_WEAPON)
            self._owner.setSkillMastery(SkillId.DETECTION)
            self._owner.setSkillMastery(SkillId.PHYSICAL_ENCHANT_STR)
            self._owner.sendPackets(S_AddSkill(0, 24, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20008:
            self._owner.setSkillMastery(SkillId.HASTE)
            self._owner.sendPackets(S_AddSkill(0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20023:
            self._owner.setSkillMastery(SkillId.GREATER_HASTE)
            self._owner.sendPackets(S_AddSkill(0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    def removeMagicHelm(self, objid, item_inst):
        item_id = item_inst._itemId

        if item_id == 20013:
            if not SkillsTable().spellCheck(objid, SkillId.PHYSICAL_ENCHANT_DEX):
                self._owner.removeSkillMastery(SkillId.PHYSICAL_ENCHANT_DEX)
                self._owner.sendPackets(S_DelSkill(0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            if not SkillsTable().spellCheck(objid, SkillId.HASTE):
                self._owner.removeSkillMastery(SkillId.HASTE)
                self._owner.sendPackets(S_DelSkill(0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20014:
            if not SkillsTable().spellCheck(objid, SkillId.HEAL):
                self._owner.removeSkillMastery(SkillId.HEAL)
                self._owner.sendPackets(S_DelSkill(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            if not SkillsTable().spellCheck(objid, SkillId.EXTRA_HEAL):
                self._owner.removeSkillMastery(SkillId.EXTRA_HEAL)
                self._owner.sendPackets(S_DelSkill(0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20015:
            if not SkillsTable().spellCheck(objid, SkillId.ENCHANT_WEAPON):
                self._owner.removeSkillMastery(SkillId.ENCHANT_WEAPON)
                self._owner.sendPackets(S_DelSkill(0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            if not SkillsTable().spellCheck(objid, SkillId.DETECTION):
                self._owner.removeSkillMastery(SkillId.DETECTION)
                self._owner.sendPackets(S_DelSkill(0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            if not SkillsTable().spellCheck(objid, SkillId.PHYSICAL_ENCHANT_STR):
                self._owner.removeSkillMastery(SkillId.PHYSICAL_ENCHANT_STR)
                self._owner.sendPackets(S_DelSkill(0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20008:
            if not SkillsTable().spellCheck(objid, SkillId.HASTE):
                self._owner.removeSkillMastery(SkillId.HASTE)
                self._owner.sendPackets(S_DelSkill(0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        elif item_id == 20023:
            if not SkillsTable().spellCheck(objid, SkillId.GREATER_HASTE):
                self._owner.removeSkillMastery(SkillId.GREATER_HASTE)
                self._owner.sendPackets(S_DelSkill(0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))