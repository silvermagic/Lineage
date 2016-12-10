# -*- coding: utf-8 -*-

import logging
from Config import Config
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_ItemStatus import S_ItemStatus
from server.serverpackets.S_ItemColor import S_ItemColor
from server.serverpackets.S_PacketBox import S_PacketBox
from server.serverpackets.S_ItemAmount import S_ItemAmount
from server.serverpackets.S_ItemName import S_ItemName
from server.serverpackets.S_OwnCharStatus import S_OwnCharStatus
from server.serverpackets.S_CharVisualUpdate import S_CharVisualUpdate
from server.serverpackets.S_DeleteInventoryItem import S_DeleteInventoryItem
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

    def checkAddItem(self, item_inst, count):
        ret = Inventory.checkAddItem(self, item_inst, count)
        if ret == Inventory.SIZE_OVER:
            self._owner.sendPackets(S_ServerMessage(263))
        elif ret == Inventory.WEIGHT_OVER:
            self._owner.sendPackets(S_ServerMessage(82))
        elif ret == Inventory.AMOUNT_OVER:
            self._owner.sendPackets(S_ServerMessage(166, '所持有的金币', '超过20亿'))
        return ret

    def receiveDamage(self, objid=None, inst=None, count=1):
        if objid:
            item_inst = self.getItem(objid)
            if not item_inst:
                return 0
        elif inst:
            item_inst = inst
        else:
            return 0
        curDurability = item_inst._durability
        clsType = item_inst._item._clsType

        if (curDurability == 0 and clsType == 0) or curDurability < 0:
            item_inst._durability = 0
            return None

        if clsType == 0: # 材料耐久度计算
            minDurability = (item_inst._enchantLevel + 5) * -1
            durability = curDurability - count
            if durability < minDurability:
                durability = minDurability
            if curDurability > durability:
                item_inst._durability = durability
        else: # 武器 防具的损坏度计算
            maxDurability = item_inst._enchantLevel + 5
            durability = curDurability + count
            if durability > maxDurability:
                durability = maxDurability
            if curDurability < durability:
                item_inst._durability = durability

        self.updateItem(item_inst, PcInventory.COL_DURABILITY)
        return item_inst

    def recoveryDamage(self, item_inst):
        if not item_inst:
            return None

        clsType = item_inst._item._clsType
        durability = item_inst._durability

        if (durability == 0 and clsType != 0) or durability < 0:
            item_inst._durability = 0
            return None

        if clsType == 0: # 耐久度修复
            item_inst._durability += durability + 1
        else: # 损坏度修复
            item_inst._durability += durability - 1

        self.updateItem(item_inst, PcInventory.COL_DURABILITY)
        return item_inst

    def loadItems(self):
        from server.model.World import World

        try:
            for item_inst in CharactersItemStorage.create().loadItems(self._owner._id):
                self._item_insts.append(item_inst)
                if item_inst._isEquipped:
                    item_inst._isEquipped = False
                    self.setEquipped(item_inst, True, True, False)
                if item_inst._item._clsType == 2 and item_inst._item._type == 2:
                    item_inst._remainingTime = item_inst._item.getLightFuel()
                World().storeObject(item_inst)
        except Exception as e:
            logging.error(e)

    def insertItem(self, item_inst):
        # self._owner.sendPackets(S_AddItem(item_inst))
        if item_inst._item._weight != 0:
            self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))
        try:
            CharactersItemStorage.create().storeItem(self._owner._id, item_inst)
        except Exception as e:
            logging.error(e)

    def deleteItem(self, item_inst):
        try:
            CharactersItemStorage.create().deleteItem(item_inst)
        except Exception as e:
            logging.error(e)

        if item_inst._isEquipped:
            self.setEquipped(item_inst, False)
        self._owner.sendPackets(S_DeleteInventoryItem(item_inst))
        self._item_insts.remove(item_inst)
        if item_inst._item._weight != 0:
            self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, self.getWeight240()))

    def updateItem(self, item_inst, col=None):
        try:
            if not col:
                column = PcInventory.COL_COUNT
            else:
                column = col

            if column & (PcInventory.COL_FIREMR | PcInventory.COL_WATERMR | PcInventory.COL_EARTHMR
                             | PcInventory.COL_WINDMR | PcInventory.COL_ADDSP | PcInventory.COL_ADDHP
                             | PcInventory.COL_HPR | PcInventory.COL_MPR | PcInventory.COL_ATTR_ENCHANT_LEVEL
                             | PcInventory.COL_ATTR_ENCHANT_KIND | PcInventory.COL_BLESS | PcInventory.COL_REMAINING_TIME
                             | PcInventory.COL_CHARGE_COUNT | PcInventory.COL_ENCHANTLVL | PcInventory.COL_DURABILITY):
                self._owner.sendPackets(S_ItemStatus(item_inst))
            if column & PcInventory.COL_ITEMID:
                self._owner.sendPackets(S_ItemStatus(item_inst))
                self._owner.sendPackets(S_ItemColor(item_inst))
                self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, value=self.getWeight240()))
            if column & PcInventory.COL_DELAY_EFFECT:
                pass
            if column & PcInventory.COL_COUNT:
                self._owner.sendPackets(S_ItemAmount(item_inst))
                weight = item_inst.getWeight()
                if weight != item_inst._lastWeight:
                    item_inst._lastWeight = weight
                    self._owner.sendPackets(S_ItemStatus(item_inst))
                else:
                    self._owner.sendPackets(S_ItemName(item_inst))
                if item_inst._item._weight != 0:
                    self._owner.sendPackets(S_PacketBox(S_PacketBox.WEIGHT, value=self.getWeight240()))
            if column & PcInventory.COL_EQUIPPED:
                self._owner.sendPackets(S_ItemName(item_inst))
            if column & PcInventory.COL_IS_ID:
                self._owner.sendPackets(S_ItemStatus(item_inst))
                self._owner.sendPackets(S_ItemColor(item_inst))

            if not col:
                if item_inst._item._save_at_once:
                    self.saveItem(item_inst, PcInventory.COL_COUNT)
        except Exception as e:
            logging.error(e)

    def saveItem(self, item_inst, column):
        '''
        更新数据库中的道具信息
        :param item_inst:道具实例(ItemInstance)
        :param column:需要更新的道具属性集(long)
        :return:None
        '''
        if column == 0:
            return
        try:
            storage = CharactersItemStorage.create()
            if column & PcInventory.COL_ATTR_ENCHANT_LEVEL:
                storage.updateItemAttrEnchantLevel(item_inst)
            if column & PcInventory.COL_ATTR_ENCHANT_KIND:
                storage.updateItemAttrEnchantKind(item_inst)
            if column & PcInventory.COL_BLESS:
                storage.updateItemBless(item_inst)
            if column & PcInventory.COL_FIREMR:
                storage.updateFireMr(item_inst)
            if column & PcInventory.COL_WATERMR:
                storage.updateWaterMr(item_inst)
            if column & PcInventory.COL_EARTHMR:
                storage.updateEarthMr(item_inst)
            if column & PcInventory.COL_WINDMR:
                storage.updateWindMr(item_inst)
            if column & PcInventory.COL_ADDSP:
                storage.updateaddSp(item_inst)
            if column & PcInventory.COL_ADDHP:
                storage.updateaddHp(item_inst)
            if column & PcInventory.COL_ADDMP:
                storage.updateaddMp(item_inst)
            if column & PcInventory.COL_HPR:
                storage.updateHpr(item_inst)
            if column & PcInventory.COL_MPR:
                storage.updateMpr(item_inst)
            if column & PcInventory.COL_REMAINING_TIME:
                storage.updateItemRemainingTime(item_inst)
            if column & PcInventory.COL_CHARGE_COUNT:
                storage.updateItemChargeCount(item_inst)
            if column & PcInventory.COL_ITEMID:
                storage.updateItemId(item_inst)
            if column & PcInventory.COL_DELAY_EFFECT:
                storage.updateItemDelayEffect(item_inst)
            if column & PcInventory.COL_COUNT:
                storage.updateItemCount(item_inst)
            if column & PcInventory.COL_EQUIPPED:
                storage.updateItemEquipped(item_inst)
            if column & PcInventory.COL_ENCHANTLVL:
                storage.updateItemEnchantLevel(item_inst)
            if column & PcInventory.COL_IS_ID:
                storage.updateItemIdentified(item_inst)
            if column & PcInventory.COL_DURABILITY:
                storage.updateItemDurability(item_inst)
        except Exception as e:
            logging.error(e)

    def setEquipped(self, item_inst, equipped, loaded = False, changeWeapon = False):
        '''
        设置道具装备状态
        :param item_inst:道具实例(ItemInstance)
        :param equipped:是否装备(True/False)
        :param loaded:
        :param changeWeapon:切换武器(True/False)
        :return:None
        '''
        item_id = item_inst._itemId
        clsType = item_inst._item._clsType
        if item_inst._isEquipped != equipped:
            if equipped:
                item_inst._isEquipped = True
                self._owner._equipSlot.set(item_inst)
            else:
                if not loaded:
                    if item_id in (20077, # 炎魔的血光斗篷
                                   20062, # 隐身斗篷
                                   120077): # 隐身斗篷
                        if self._owner.isInvisble():
                            self._owner.delInvis()
                item_inst._isEquipped = False
                self._owner._equipSlot.remove(item_inst)

            if not loaded:
                self._owner.setCurrentHp(self._owner._currentHp)
                self._owner.setCurrentMp(self._owner._currentMp)
                self.updateItem(item_inst,PcInventory.COL_EQUIPPED)
                self._owner.sendPackets(S_OwnCharStatus(self._owner))
                if clsType == 1 and not changeWeapon:
                    self._owner.sendPackets(S_CharVisualUpdate(self._owner))
                    self._owner.broadcastPacket(S_CharVisualUpdate(self._owner))

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
            for item_inst in self._item_insts:
                if item_inst._itemId == id and item_inst._isEquipped:
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
        for item_inst in self._item_insts:
            if item_inst._item._clsType == clsType and item_inst._item._type == type and item_inst._isEquipped:
                count += 1
        return count

    def getItemEquipped(self, clsType, type):
        '''
        获取装备的特定道具
        :param clsType:道具类别(int)
        :param type:道具详细类型(int)
        :return:道具实例(ItemInstance)
        '''
        for item_inst in self._item_insts:
            if item_inst._item._clsType == clsType and item_inst._item._type == type and item_inst._isEquipped:
                return item_inst
        return None

    def getRingEquipped(self):
        '''
        获取装备的戒指
        :return:道具实例集(ItemInstance[])
        '''
        rings = []
        for item_inst in self._item_insts:
            if item_inst._item._clsType == 2 and item_inst._item._type == 9 and item_inst._isEquipped:
                rings.append(item_inst)
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

        for bullet in self._item_insts:
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
        for item_inst in self._item_insts:
            if item_inst._isEquipped:
                hpr += item_inst._item._addhpr + item_inst._Hpr
        return hpr

    def mpRegenPerTick(self):
        '''
        计算装备道具带来的的MP回复量
        :return:MP回复量(int)
        '''
        mpr = 0
        for item_inst in self._item_insts:
            if item_inst._isEquipped:
                mpr += item_inst._item._addmpr + item_inst._Mpr
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



