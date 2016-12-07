# -*- coding: utf-8 -*-

import logging
from Config import Config
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_ItemStatus import S_ItemStatus
from server.serverpackets.S_ItemColor import S_ItemColor
from server.serverpackets.S_PacketBox import S_PacketBox
from server.serverpackets.S_ItemAmount import S_ItemAmount
from server.serverpackets.S_ItemName import S_ItemName
from server.storage.CharactersItemStorage import CharactersItemStorage
from Inventory import Inventory

class PcInventory(Inventory):
    '''
    游戏玩家背包系统
    '''
    COL_FIREMR = 1 << 20
    COL_WATERMR = 1 << 19
    COL_WINDMR = 1 << 18
    COL_EARTHMR = 1 << 17
    COL_ADDSP = 1 << 16
    COL_ADDHP = 1 << 15
    COL_ADDMP = 1 << 14
    COL_HPR = 1 << 13
    COL_MPR = 1 << 12
    COL_ATTR_ENCHANT_LEVEL = 1 << 11
    COL_ATTR_ENCHANT_KIND = 1 << 10
    COL_BLESS = 1 << 9
    COL_REMAINING_TIME = 1 << 8
    COL_CHARGE_COUNT = 1 << 7
    COL_ITEMID = 1 << 6
    COL_DELAY_EFFECT = 1 << 5
    COL_COUNT = 1 << 4
    COL_EQUIPPED = 1 << 3
    COL_ENCHANTLVL = 1 << 2
    COL_IS_ID = 1 << 1
    COL_DURABILITY = 1 << 0

    def __init__(self, pc):
        Inventory.__init__(self)
        self._owner = pc
        self._arrowId = 0
        self._stingId = 0

    def checkAddItem(self, itemInst, count):
        ret = Inventory.checkAddItem(self, itemInst, count)
        if ret == Inventory.SIZE_OVER:
            self._owner.sendPackets(S_ServerMessage(263))
        elif ret == Inventory.WEIGHT_OVER:
            self._owner.sendPackets(S_ServerMessage(82))
        elif ret == Inventory.AMOUNT_OVER:
            self._owner.sendPackets(S_ServerMessage(166, '所持有的金币', '超过20亿'))
        return ret

    def receiveDamage(self, objid=None, inst=None, count=1):
        if objid:
            itemInst = self.getItem(objid)
            if not itemInst:
                return 0
        elif inst:
            itemInst = inst
        else:
            return 0
        curDurability = itemInst._durability
        clsType = itemInst._item._clsType

        if (curDurability == 0 and clsType == 0) or curDurability < 0:
            itemInst._durability = 0
            return None

        if clsType == 0: # 材料耐久度计算
            minDurability = (itemInst._enchantLevel + 5) * -1
            durability = curDurability - count
            if durability < minDurability:
                durability = minDurability
            if curDurability > durability:
                itemInst._durability = durability
        else: # 武器 防具的损坏度计算
            maxDurability = itemInst._enchantLevel + 5
            durability = curDurability + count
            if durability > maxDurability:
                durability = maxDurability
            if curDurability < durability:
                itemInst._durability = durability

        self.updateItem(itemInst, PcInventory.COL_DURABILITY)
        return itemInst

    def recoveryDamage(self, itemInst):
        if not itemInst:
            return None

        clsType = itemInst._item._clsType
        durability = itemInst._durability

        if (durability == 0 and clsType != 0) or durability < 0:
            itemInst._durability = 0
            return None

        if clsType == 0: # 耐久度修复
            itemInst._durability += durability + 1
        else: # 损坏度修复
            itemInst._durability += durability - 1

        self.updateItem(itemInst, PcInventory.COL_DURABILITY)
        return itemInst

    def loadItems(self):
        from server.model.World import World

        try:
            for itemInst in CharactersItemStorage.create().loadItems(self._owner._id):
                self._itemInsts.append(itemInst)
                if itemInst._isEquipped:
                    itemInst._isEquipped = False
                    self.setEquipped(itemInst, True, True, False)
                if itemInst._item._clsType == 2 and itemInst._item._type == 2:
                    itemInst._remainingTime = itemInst._item.getLightFuel()
                World().storeObject(itemInst)
        except Exception as e:
            logging.error(e)

    def insertItem(self, itemInst):
        # self._owner.sendPackets(S_AddItem(itemInst))
        if itemInst._item._weight != 0:
            self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))
        try:
            CharactersItemStorage.create().storeItem(self._owner._id, itemInst)
        except Exception as e:
            logging.error(e)

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

    def updateItem(self, itemInst, col=None):
        if not col:
            column = PcInventory.COL_COUNT
        else:
            column = col

        if column & (PcInventory.COL_FIREMR | PcInventory.COL_WATERMR | PcInventory.COL_EARTHMR
                         | PcInventory.COL_WINDMR | PcInventory.COL_ADDSP | PcInventory.COL_ADDHP
                         | PcInventory.COL_HPR | PcInventory.COL_MPR | PcInventory.COL_ATTR_ENCHANT_LEVEL
                         | PcInventory.COL_ATTR_ENCHANT_KIND | PcInventory.COL_BLESS | PcInventory.COL_REMAINING_TIME
                         | PcInventory.COL_CHARGE_COUNT | PcInventory.COL_ENCHANTLVL | PcInventory.COL_DURABILITY):
            self._owner.sendPackets(S_ItemStatus(itemInst))
        if column & PcInventory.COL_ITEMID:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            self._owner.sendPackets(S_ItemColor(itemInst))
            self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))
        if column & PcInventory.COL_DELAY_EFFECT:
            pass
        if column & PcInventory.COL_COUNT:
            self._owner.sendPackets(S_ItemAmount(itemInst))
            weight = itemInst.getWeight()
            if weight != itemInst._lastWeight:
                itemInst._lastWeight = weight
                self._owner.sendPackets(S_ItemStatus(itemInst))
            else:
                self._owner.sendPackets(S_ItemName(itemInst))
            if itemInst._item._weight != 0:
                self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))
        if column & PcInventory.COL_EQUIPPED:
            self._owner.sendPackets(S_ItemName(itemInst))
        if column & PcInventory.COL_IS_ID:
            self._owner.sendPackets(S_ItemStatus(itemInst))
            self._owner.sendPackets(S_ItemColor(itemInst))

        if not col:
            if itemInst._item._save_at_once:
                self.saveItem(itemInst, PcInventory.COL_COUNT)

    def saveItem(self, itemInst, column):
        '''
        更新数据库中的道具信息
        :param itemInst:道具实例(ItemInstance)
        :param column:需要更新的道具属性集(long)
        :return:None
        '''
        if column == 0:
            return
        try:
            storage = CharactersItemStorage.create()
            if column & PcInventory.COL_ATTR_ENCHANT_LEVEL:
                storage.updateItemAttrEnchantLevel(itemInst)
            if column & PcInventory.COL_ATTR_ENCHANT_KIND:
                storage.updateItemAttrEnchantKind(itemInst)
            if column & PcInventory.COL_BLESS:
                storage.updateItemBless(itemInst)
            if column & PcInventory.COL_FIREMR:
                storage.updateFireMr(itemInst)
            if column & PcInventory.COL_WATERMR:
                storage.updateWaterMr(itemInst)
            if column & PcInventory.COL_EARTHMR:
                storage.updateEarthMr(itemInst)
            if column & PcInventory.COL_WINDMR:
                storage.updateWindMr(itemInst)
            if column & PcInventory.COL_ADDSP:
                storage.updateaddSp(itemInst)
            if column & PcInventory.COL_ADDHP:
                storage.updateaddHp(itemInst)
            if column & PcInventory.COL_ADDMP:
                storage.updateaddMp(itemInst)
            if column & PcInventory.COL_HPR:
                storage.updateHpr(itemInst)
            if column & PcInventory.COL_MPR:
                storage.updateMpr(itemInst)
            if column & PcInventory.COL_REMAINING_TIME:
                storage.updateItemRemainingTime(itemInst)
            if column & PcInventory.COL_CHARGE_COUNT:
                storage.updateItemChargeCount(itemInst)
            if column & PcInventory.COL_ITEMID:
                storage.updateItemId(itemInst)
            if column & PcInventory.COL_DELAY_EFFECT:
                storage.updateItemDelayEffect(itemInst)
            if column & PcInventory.COL_COUNT:
                storage.updateItemCount(itemInst)
            if column & PcInventory.COL_EQUIPPED:
                storage.updateItemEquipped(itemInst)
            if column & PcInventory.COL_ENCHANTLVL:
                storage.updateItemEnchantLevel(itemInst)
            if column & PcInventory.COL_IS_ID:
                storage.updateItemIdentified(itemInst)
            if column & PcInventory.COL_DURABILITY:
                storage.updateItemDurability(itemInst)
        except Exception as e:
            logging.error(e)

    def setEquipped(self, itemInst, equipped, loaded = False, changeWeapon = False):
        '''
        设置道具装备状态
        :param itemInst:道具实例(ItemInstance)
        :param equipped:是否装备(True/False)
        :param loaded:
        :param changeWeapon:切换武器(True/False)
        :return:None
        '''
        pass

    def checkEquipped(self, ids):
        '''
        判断是否装备了特定道具
        :param ids:道具模板ID集(int[])
        :return:True/False
        '''
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
        '''
        获取装备了特定道具的数目
        :param clsType:道具类别(int)
        :param type:道具详细类型(int)
        :return:int
        '''
        count = 0
        for itemInst in self._itemInsts:
            if itemInst._item._clsType == clsType and itemInst._item._type == type:
                count += 1
        return count

    def getItemEquipped(self, clsType, type):
        '''
        获取装备的特定道具
        :param clsType:道具类别(int)
        :param type:道具详细类型(int)
        :return:道具实例(ItemInstance)
        '''
        for itemInst in self._itemInsts:
            if itemInst._item._clsType == clsType and itemInst._item._type == type and itemInst._isEquipped:
                return itemInst
        return None

    def getRingEquipped(self):
        '''
        获取装备的戒指
        :return:道具实例集(ItemInstance[])
        '''
        rings = []
        for itemInst in self._itemInsts:
            if itemInst._item._clsType == 2 and itemInst._item._type == 9 and itemInst._isEquipped:
                rings.append(itemInst)
                if len(rings) == 2:
                    return rings

    def takeoffEquip(self, polyid):
        '''
        变身时候强制解除装备
        :param polyid:变身怪物ID(int)
        :return:None
        '''
        self.takeoffWeapon(polyid)
        self.takeoffArmor(polyid)

    def takeoffWeapon(self, polyid):
        '''
        变身时候强制解除武器
        :param polyid:变身怪物ID(int)
        :return:None
        '''
        pass

    def takeoffArmor(self, polyid):
        '''
        变身时候强制解除防具
        :param polyid:变身怪物ID(int)
        :return:None
        '''
        # todo: 变身系统
        pass

    def getArrow(self):
        '''
        获取优先使用的箭矢
        :return:箭矢(ItemInstance)
        '''
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
        '''
        计算装备道具带来的的HP回复量
        :return:HP回复量(int)
        '''
        hpr = 0
        for itemInst in self._itemInsts:
            if itemInst._isEquipped:
                hpr += itemInst._item._addhpr + itemInst._Hpr
        return hpr

    def mpRegenPerTick(self):
        '''
        计算装备道具带来的的MP回复量
        :return:MP回复量(int)
        '''
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

    def getWeight240(self):
        '''
        ???
        :return:???(int)
        '''
        return self.calcWeight240(self.getWeight())

    def calcWeight240(self, weight):
        '''
        ???
        :param weight:重量
        :return:???
        '''
        weight240 = 0
        if Config.getint('rates', 'RateWeightLimit') != 0:
            maxWeight = self._owner.getMaxWeight()
            if weight > maxWeight:
                weight240 = 240
            else:
                weight240 = int(round(weight * 100 / maxWeight * 240.0 / 100.00, 2))
        return weight240



