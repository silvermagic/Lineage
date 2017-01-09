# -*- coding: utf-8 -*-

from server.datatables.PolyTable import PolyTable
from server.model.skill import SkillId
from server.serverpackets.S_CloseList import S_CloseList
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_ChangeShape import S_ChangeShape
from server.serverpackets.S_SkillIconGFX import S_SkillIconGFX
from server.serverpackets.S_CharVisualUpdate import S_CharVisualUpdate

class PolyMorph:
    # 变身武器使用限制
    DAGGER_EQUIP = 1
    SWORD_EQUIP = 2
    TWOHANDSWORD_EQUIP = 4
    AXE_EQUIP = 8
    SPEAR_EQUIP = 16
    STAFF_EQUIP = 32
    EDORYU_EQUIP = 64
    CLAW_EQUIP = 128
    BOW_EQUIP = 256
    KIRINGKU_EQUIP = 512
    CHAINSWORD_EQUIP = 1024
    # 变身装备使用限制
    HELM_EQUIP = 1
    AMULET_EQUIP = 2
    EARRING_EQUIP = 4
    TSHIRT_EQUIP = 8
    ARMOR_EQUIP = 16
    CLOAK_EQUIP = 32
    BELT_EQUIP = 64
    SHIELD_EQUIP = 128
    GLOVE_EQUIP = 256
    RING_EQUIP = 512
    BOOTS_EQUIP = 1024
    GUARDER_EQUIP = 2048
    # 变身原因
    MORPH_BY_ITEMMAGIC = 1
    MORPH_BY_GM = 2
    MORPH_BY_NPC = 4
    MORPH_BY_KEPLISHA = 8
    MORPH_BY_LOGIN = 0

    weaponFlgMap = {1 : SWORD_EQUIP,
                    2 : DAGGER_EQUIP,
                    3 : TWOHANDSWORD_EQUIP,
                    4 : BOW_EQUIP,
                    5 : SPEAR_EQUIP,
                    6 : AXE_EQUIP,
                    7 : STAFF_EQUIP,
                    8 : BOW_EQUIP,
                    9 : BOW_EQUIP,
                    10 : BOW_EQUIP,
                    11 : CLAW_EQUIP,
                    12 : EDORYU_EQUIP,
                    13 : BOW_EQUIP,
                    14 : SPEAR_EQUIP,
                    15 : AXE_EQUIP,
                    16 : STAFF_EQUIP,
                    17 : KIRINGKU_EQUIP,
                    18 : CHAINSWORD_EQUIP}

    armorFlgMap = {1 : HELM_EQUIP,
                   2 : ARMOR_EQUIP,
                   3 : TSHIRT_EQUIP,
                   4 : CLOAK_EQUIP,
                   5 : GLOVE_EQUIP,
                   6 : BOOTS_EQUIP,
                   7 : SHIELD_EQUIP,
                   8 : AMULET_EQUIP,
                   9 : RING_EQUIP,
                   10 : BELT_EQUIP,
                   12 : EARRING_EQUIP,
                   13 : GUARDER_EQUIP}

    @classmethod
    def handleCommands(cls, pc, s):
        if not pc or pc._isDead:
            return

        if s == "none":
            if pc._tempCharGfx != 6034 and pc._tempCharGfx != 6035:
                pc.removeSkillEffect(SkillId.SHAPE_CHANGE)
                pc.sendPackets(S_CloseList(pc._id))
            return
        if PolyTable()._polymorphs.has_key(s):
            poly = PolyTable()._polymorphs[s]
            if pc._level >= poly._minLevel or pc._gm:
                if pc._tempCharGfx == 6034 or pc._tempCharGfx == 6035:
                    pc.sendPackets(S_ServerMessage(181)) # 无法变身成指定怪物
                else:
                    cls.doPoly(pc, poly._polyId, 7200, cls.MORPH_BY_ITEMMAGIC)
                    pc.sendPackets(S_CloseList(pc._id))
            else:
                pc.sendPackets(S_ServerMessage(181))

    @classmethod
    def doPoly(cls, cha, polyId, timeSecs, cause):
        from server.model.Instance.PcInstance import PcInstance
        from server.model.Instance.MonsterInstance import MonsterInstance

        if not cha or cha._isDead:
            return

        if isinstance(cha, PcInstance):
            pc = cha
            if pc._loc._map._mapId == 5124: # 钓鱼区域不允许变身
                pc.sendPackets(S_ServerMessage(1170))
                return

            if pc._tempCharGfx == 6034 or pc._tempCharGfx == 6035:
                pc.sendPackets(S_ServerMessage(181))
                return

            if not cls.isMatchCause(polyId, cause):
                pc.sendPackets(S_ServerMessage(181))
                return

            pc.killSkillEffectTimer(SkillId.SHAPE_CHANGE)
            pc.setSkillEffect(SkillId.SHAPE_CHANGE, timeSecs * 1000)
            if pc._tempCharGfx != polyId: # 相同变身只需要更新图标时间
                weaponTakeoff = (pc._weapon and not cls.isEquipableWeapon(polyId, pc._weapon._item._type))
                pc._tempCharGfx = polyId
                pc.sendPackets(S_ChangeShape(pc._id, polyId, weaponTakeoff))
                import logging
                if pc._gmInvis:
                    pass
                elif pc.isInvisble():
                    pc.broadcastPacketForFindInvis(S_ChangeShape(pc._id, polyId), True)
                else:
                    pc.broadcastPacket(S_ChangeShape(pc._id, polyId))
                pc._inventory.takeoffEquip(polyId)
                if pc._weapon:
                    data = S_CharVisualUpdate(pc)
                    pc.sendPackets(data)
                    pc.broadcastPacket(data)
            pc.sendPackets(S_SkillIconGFX(35, timeSecs))
        elif isinstance(cha, MonsterInstance):
            # todo: 怪物变身
            pass
        return

    @classmethod
    def undoPoly(cls, cha):
        from server.model.Instance.PcInstance import PcInstance
        from server.model.Instance.MonsterInstance import MonsterInstance

        if isinstance(cha, PcInstance):
            pc = cha
            pc._tempCharGfx = pc._classId
            pc.sendPackets(S_ChangeShape(pc._id, pc._classId))
            pc.broadcastPacket(S_ChangeShape(pc._id, pc._classId))
            if pc._weapon:
                data = S_CharVisualUpdate(pc)
                pc.sendPackets(data)
                pc.broadcastPacket(data)

        elif isinstance(cha, MonsterInstance):
            # todo: 怪物变身
            pass

    @classmethod
    def isMatchCause(cls, polyId, cause):
        if not PolyTable()._polyIdIndex.has_key(polyId):
            return True
        if cause == PolyMorph.MORPH_BY_LOGIN:
            return True

        return 0 != (PolyTable()._polyIdIndex[polyId]._causeFlg & cause)

    @classmethod
    def isEquipableWeapon(cls, polyId, weaponType):
        if not PolyTable()._polyIdIndex.has_key(polyId):
            return True

        if cls.weaponFlgMap.has_key(weaponType):
            return 0 != (PolyTable()._polyIdIndex[polyId]._weaponEquipFlg & cls.weaponFlgMap[weaponType])

        return True

    @classmethod
    def isEquipableArmor(cls, polyId, armorFlgMap):
        if not PolyTable()._polyIdIndex.has_key(polyId):
            return True

        if cls.armorFlgMap.has_key(armorFlgMap):
            return 0 != (PolyTable()._polyIdIndex[polyId]._armorEquipFlg & cls.armorFlgMap[armorFlgMap])

        return True