# -*- coding: utf-8 -*-

import logging
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_ItemStatus import S_ItemStatus
from server.serverpackets.S_ItemColor import S_ItemColor
from server.serverpackets.S_PacketBox import S_PacketBox
from server.serverpackets.S_ItemAmount import S_ItemAmount
from server.serverpackets.S_ItemName import S_ItemName
from server.storage.CharactersItemStorage import CharactersItemStorage
from Inventory import Inventory

COL_FIREMR = 137
COL_WATERMR = 136
COL_WINDMR = 135
COL_EARTHMR = 134
COL_ADDSP = 133
COL_ADDHP = 132
COL_ADDMP = 131
COL_HPR = 130
COL_MPR = 129
COL_ATTR_ENCHANT_LEVEL = 2048
COL_ATTR_ENCHANT_KIND = 1024
COL_BLESS = 512
COL_REMAINING_TIME = 256
COL_CHARGE_COUNT = 128
COL_ITEMID = 64
COL_DELAY_EFFECT = 32
COL_COUNT = 16
COL_EQUIPPED = 8
COL_ENCHANTLVL = 4
COL_IS_ID = 2
COL_DURABILITY = 1

class PcInventory(Inventory):
    '''
    游戏玩家背包系统
    '''
    def __init__(self, pc):
        Inventory.__init__(self)
        self._owner = pc
        self._arrowId = 0
        self._stingId = 0
    '''
    def checkAddItem(self, itemInst, count):

        ret = Inventory.checkAddItem(self, itemInst, count)
        if ret == Inventory.SIZE_OVER:
            self._owner.sendPackets(S_ServerMessage(263))
        elif ret == Inventory.WEIGHT_OVER:
            self._owner.sendPackets(S_ServerMessage(82))
        elif ret == Inventory.AMOUNT_OVER:
            self._owner.sendPackets(S_ServerMessage(166, '所持有的金币', '超过20亿'))

        return ret

    def receiveDamageInst(self, itemInst, count=1):
        if not itemInst:
            return None

        clsType = itemInst._item._clsType
        curDurability = itemInst._durability

        if (curDurability == 0 and clsType == 0) or curDurability < 0:
            itemInst._durability = 0
            return None

        if clsType == 0:
            minDurability = (itemInst._enchantLevel + 5) * -1
            durability = curDurability - count
            if durability < minDurability:
                durability = minDurability
            if curDurability > durability:
                itemInst._durability = durability
        else:
            maxDurability = itemInst._enchantLevel + 5
            durability = curDurability - count
            if durability > maxDurability:
                durability = maxDurability
            if curDurability < durability:
                itemInst._durability = durability

        self.updateItem(itemInst, 1)
        return itemInst

    def recoveryDamage(self, itemInst):
        if not itemInst:
            return None

        clsType = itemInst._item._clsType
        durability = itemInst._durability

        if (durability == 0 and clsType != 0) or durability < 0:
            itemInst._durability = 0
            return None

        if clsType == 0:
            itemInst._durability += durability + 1
        else:
            itemInst._durability += durability - 1

        self.updateItem(itemInst, 1)
        return itemInst
    '''

    def getWeight240(self):
        return 0
    '''
    def calcWeight240(self, weight):
        pass

    def setEquipped(self, itemInst, equipped, loaded = False, changeWeapon = False):
        if itemInst._isEquipped != equipped:
            item = itemInst._item
            if equipped:
                itemInst._isEquipped = True
                self._owner._equipSlot = itemInst
            else:
                if not loaded:
                    if item._itemId in (20077, 20062, 120077):
                        # todo: 隐身
                        return
                itemInst._isEquipped = True
                self._owner._equipSlot.remove(item)
            if not loaded:
                self._owner.setCurrentHp(self._owner._currentHp)
                self._owner.setCurrentMp(self._owner._currentMp)

    def checkEquipped(self, ids):
        ret = False
        if type(ids) != type([]):
            ids = [ids]
        for id in ids:
            for itemInst in self._itemInsts:
                if itemInst._itemId == id and itemInst._isEquipped:
                    ret = True
                    break
            if not ret:
                break

        return ret

    def getTypeEquipped(self, clsType, type):
        count = 0
        for itemInst in self._itemInsts:
            if itemInst._item._clsType == clsType and itemInst._item._type == type:
                count += 1
        return count

    def getItemEquipped(self, clsType, type):
        for itemInst in self._itemInsts:
            if itemInst._item._clsType == clsType and itemInst._item._type == type and itemInst._isEquipped:
                return itemInst

    def getRingEquipped(self):
        rings = []
        for itemInst in self._itemInsts:
            if itemInst._item._clsType == 2 and itemInst._item._type == 9 and itemInst._isEquipped:
                rings.append(itemInst)
                if len(rings) == 2:
                    return rings

    def takeoffEquip(self, polyid):
        self.takeoffWeapon(polyid)
        self.takeoffArmor(polyid)

    def takeoffWeapon(self, polyid):
        if not self._owner._weapon:
            return

        takeoff = False
        weapon_type = self._owner._weapon._item._type
        # todo: 变身系统
        if takeoff:
            self.setEquipped(self._owner._weapon, False, False, False)

    def takeoffArmor(self, polyid):
        # todo: 变身系统
        pass

    def getArrow(self):
        return self.getBullet(0)

    def getSting(self):
        return self.getBullet(15)

    def getBullet(self, type):
        priorityId = 0
        if type == 0:
            priorityId = self._arrowId
        elif type == 15:
            priorityId = self._stingId

        if priorityId > 0:
            bullet = self.findItemId(priorityId)
            if not bullet:
                if type == 0:
                    self._arrowId = 0
                elif type == 15:
                    self._stingId = 0
            else:
                return bullet

        for bullet in self._itemInsts:
            if bullet._item._type == type:
                if type == 0:
                    self._arrowId = bullet._itemId
                elif type == 15:
                    self._stingId = bullet._itemId
                return bullet
        return None

    def hpRegenPerTick(self):
        hpr = 0
        for itemInst in self._itemInsts:
            if itemInst._isEquipped:
                hpr += itemInst._item._addhpr + itemInst._Hpr
        return hpr

    def mpRegenPerTick(self):
        mpr = 0
        for itemInst in self._itemInsts:
            if itemInst._isEquipped:
                mpr += itemInst._item._addmpr + itemInst._Mpr
        return mpr

    def CaoPenalty(self):
        # todo: 宠物系统
        pass

    def getWeight30(self):
        return 0

    def saveItem(self, itemInst, column):
        if column == 0:
            return
        try:
            storage = CharactersItemStorage.create()
            if column >= COL_ATTR_ENCHANT_LEVEL:
                storage.updateItemAttrEnchantLevel(itemInst)
                column -= COL_ATTR_ENCHANT_LEVEL
            if column >= COL_ATTR_ENCHANT_KIND:
                storage.updateItemAttrEnchantKind(itemInst)
                column -= COL_ATTR_ENCHANT_KIND
            if column >= COL_BLESS:
                storage.updateItemBless(itemInst)
                column -= COL_BLESS
            if column >= COL_FIREMR:
                storage.updateFireMr(itemInst)
                column -= COL_FIREMR
            if column >= COL_WATERMR:
                storage.updateWaterMr(itemInst)
                column -= COL_WATERMR
            if column >= COL_EARTHMR:
                storage.updateEarthMr(itemInst)
                column -= COL_EARTHMR
            if column >= COL_WINDMR:
                storage.updateWindMr(itemInst)
                column -= COL_WINDMR
            if column >= COL_ADDSP:
                storage.updateaddSp(itemInst)
                column -= COL_ADDSP
            if column >= COL_ADDHP:
                storage.updateaddHp(itemInst)
                column -= COL_ADDHP
            if column >= COL_ADDMP:
                storage.updateaddMp(itemInst)
                column -= COL_ADDMP
            if column >= COL_HPR:
                storage.updateHpr(itemInst)
                column -= COL_HPR
            if column >= COL_MPR:
                storage.updateMpr(itemInst)
                column -= COL_MPR
            if column >= COL_REMAINING_TIME:
                storage.updateItemRemainingTime(itemInst)
                column -= COL_REMAINING_TIME
            if column >= COL_CHARGE_COUNT:
                storage.updateItemChargeCount(itemInst)
                column -= COL_CHARGE_COUNT
            if column >= COL_ITEMID:
                storage.updateItemId(itemInst)
                column -= COL_ITEMID
            if column >= COL_DELAY_EFFECT:
                storage.updateItemDelayEffect(itemInst)
                column -= COL_DELAY_EFFECT
            if column >= COL_COUNT:
                storage.updateItemCount(itemInst)
                column -= COL_COUNT
            if column >= COL_EQUIPPED:
                storage.updateItemEquipped(itemInst)
                column -= COL_EQUIPPED
            if column >= COL_ENCHANTLVL:
                storage.updateItemEnchantLevel(itemInst)
                column -= COL_ENCHANTLVL
            if column >= COL_IS_ID:
                storage.updateItemIdentified(itemInst)
                column -= COL_IS_ID
            if column >= COL_DURABILITY:
                storage.updateItemDurability(itemInst)
                column -= COL_DURABILITY
        except Exception as e:
            logging.error(e)

    def loadItems(self):
        from server.model.World import World

        for itemInst in CharactersItemStorage.create().loadItems(self._owner._id):
            self._itemInsts.append(itemInst)
            if itemInst._isEquipped:
                itemInst._isEquipped = False
                self.setEquipped(itemInst, True, True, False)
            if itemInst._item._clsType == 2 and itemInst._item._type == 2:
                itemInst._remainingTime = itemInst._item.getLightFuel()
            World().storeObject(itemInst)

    def updateItem(self, itemInst, col = None):
        if not col:
            column = COL_COUNT
        else:
            column = col

        if column >= COL_FIREMR:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_FIREMR
        if column >= COL_WATERMR:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_WATERMR
        if column >= COL_EARTHMR:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_EARTHMR
        if column >= COL_WINDMR:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_WINDMR
        if column >= COL_ADDSP:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_ADDSP
        if column >= COL_ADDHP:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_ADDHP
        if column >= COL_HPR:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_HPR
        if column >= COL_MPR:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_MPR
        if column >= COL_ATTR_ENCHANT_LEVEL:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_ATTR_ENCHANT_LEVEL
        if column >= COL_ATTR_ENCHANT_KIND:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_ATTR_ENCHANT_KIND
        if column >= COL_BLESS:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_BLESS
        if column >= COL_REMAINING_TIME:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_REMAINING_TIME
        if column >= COL_CHARGE_COUNT:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_CHARGE_COUNT
        if column >= COL_ITEMID:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            self._owner.sendPackets(S_ItemColor(itemInst))
            self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))
            column -= COL_ITEMID
        if column >= COL_DELAY_EFFECT:
            column -= COL_DELAY_EFFECT
        if column >= COL_COUNT:
            self._owner.sendPackets(S_ItemAmount(itemInst))
            weight = itemInst.getWeight()
            if weight != itemInst._lastWeight:
                itemInst._lastWeight = weight
                self._owner.sendPackets(S_ItemStatus(itemInst))
            else:
                self._owner.sendPackets(S_ItemName(itemInst))
            if itemInst._item._weight != 0:
                self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))
            column -= COL_COUNT
        if column >= COL_EQUIPPED:
            self._owner.sendPackets(S_ItemName(itemInst))
            column -= COL_EQUIPPED
        if column >= COL_ENCHANTLVL:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_ENCHANTLVL
        if column >= COL_IS_ID:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            self._owner.sendPackets(S_ItemColor(itemInst))
            column -= COL_IS_ID
        if column >= COL_DURABILITY:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            column -= COL_DURABILITY

        if not col:
            if itemInst._item._save_at_once:
                self.saveItem(itemInst, COL_COUNT)

    def deleteItem(self, itemInst):
        try:
            CharactersItemStorage.create().deleteItem(itemInst)
        except Exception as e:
            logging.error(e)

        if itemInst._isEquipped:
            self.setEquipped(itemInst, False)
        # self._owner.sendPackets(S_DeleteInventoryItem(itemInst))
        self._itemInsts.remove(itemInst)
        if itemInst._item._weight != 0:
            self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))
    '''



