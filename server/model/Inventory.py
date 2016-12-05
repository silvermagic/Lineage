# -*- coding: utf-8 -*-

import threading,random
from Config import Config
from server.datatables.ItemTable import ItemTable
from server.IdFactory import IdFactory
from Instance.ItemInstance import ItemInstance
from World import World
from Object import Object

class Inventory(Object):
    MAX_AMOUNT = 2000000000
    MAX_WEIGHT = 1500
    OK = 0
    SIZE_OVER = 1
    WEIGHT_OVER = 2
    AMOUNT_OVER = 3
    WAREHOUSE_TYPE_PERSONAL = 0
    WAREHOUSE_TYPE_CLAN = 1

    def __init__(self):
        Object.__init__(self)
        self._itemInsts = []
        #self._lock = threading.RLock()
    '''
    # 仓库当前道具总重量
    def getWeight(self):
        weight = 0
        for item in self._itemInsts:
            weight += item.getWeight()
        return weight

    def getItem(self, objectId):
        for item in self._itemInsts:
            if item._id == objectId:
                return item

        return None

    # 在仓库中找到对应道具
    def findItemId(self, id):
        for item in self._itemInsts:
            if item._itemId == id:
                return item

        return None

    def findItemsId(self, id):
        itemList = []
        for item in self._itemInsts:
            if item._itemId == id:
                itemList += item

        return itemList

    def findItemsIdNotEquipped(self, id):
        itemList = []
        for item in self._itemInsts:
            if item._itemId == id:
                if not item._isEquipped:
                    itemList += item

        return itemList

    # 检测是否可以添加count个itemInst道具到背包
    def checkAddItem(self, itemInst, count):
        if not itemInst:
            return -1

        if itemInst._count <= 0 or count <= 0:
            return -1

        # 是否超过仓库容量
        if len(self._itemInsts) > Config.getint('altsettings', 'MaxNpcItem') \
                or (len(self._itemInsts) == Config.getint('altsettings', 'MaxNpcItem')
                    and (not itemInst._item.isStackable() or self.checkItem(itemInst._itemId))):
            return Inventory.SIZE_OVER

        # 是否超过重量限制
        weight = int(self.getWeight() + itemInst._item._weight * count / 1000 + 1)
        if weight < 0 or (itemInst._item._weight * count / 1000 < 0):
            return Inventory.WEIGHT_OVER
        if weight > (Inventory.MAX_WEIGHT * float(Config.getint('rates', 'RateWeightLimitforPet'))):
            return Inventory.WEIGHT_OVER

        # 是否超过道具总数限制
        itemExist = self.findItemId(itemInst._itemId)
        if itemExist and (itemExist._count + count) > Inventory.MAX_AMOUNT:
            return Inventory.AMOUNT_OVER

        return Inventory.OK

    # 检测是否可以添加count个itemInst道具到仓库
    def checkAddItemToWarehouse(self, itemInst, count, type):
        if not itemInst:
            return -1

        if itemInst._count <= 0 or count <= 0:
            return -1

        maxSize = 100
        if type == Inventory.WAREHOUSE_TYPE_PERSONAL:
            maxSize = Config.getint('altsettings', 'MaxPersonalWarehouseItem')
        elif type == Inventory.WAREHOUSE_TYPE_CLAN:
            maxSize = Config.getint('altsettings', 'MaxClanWarehouseItem')

        if len(self._itemInsts) > maxSize \
                or (len(self._itemInsts) == maxSize
                    and (not itemInst._item.isStackable() or self.checkItem(itemInst._itemId))):
            return Inventory.SIZE_OVER

        return Inventory.OK

    # 检测物品个数是否超过限制
    def checkItem(self, id, count=1):
        if count == 0:
            return True

        if ItemTable()._allTemplates.has_key(id):
            # 物品是否可以堆叠,例如材料类的皮革就是可以堆叠的,就直接返回数量;例如武器类的双手剑就是比可以堆叠的,则需要找出总数
            if ItemTable()._allTemplates[id].isStackable():
                item = self.findItemId(id)
                if item and item._count >= count:
                    return True
            else:
                itemList = self.findItemsId(id)
                if len(itemList) >= count:
                    return True

        return False

    def checkEnchantItem(self, id, enchant, count):
        num = 0
        for itemInst in self._itemInsts:
            if itemInst._isEquipped:
                continue
            if itemInst._itemId == id and itemInst._enchantLevel == enchant:
                num += 1
                if num == count:
                    return True
        return False

    def consumeEnchantItem(self, id, enchant, count):
        num = 0
        for itemInst in self._itemInsts:
            if itemInst._isEquipped:
                continue
            if itemInst._itemId == id and itemInst._enchantLevel == enchant:
                self.removeItemInst(itemInst, itemInst._count)
                return True
        return False

    def checkItemNotEquipped(self, id, count):
        if count == 0:
            return True

        return count <= self.countItems(id)

    def checkItems(self, ids, counts = None):
        if not counts:
            for id in ids:
                if not self.checkItem(id, 1):
                    return False
            return True
        else:
            for i in range(len(ids)):
                if not self.checkItem(ids[i], counts[i]):
                    return False
            return True

    def countItems(self, id):
        if not ItemTable()._allTemplates.has_key(id):
            return 0

        if ItemTable()._allTemplates[id].isStackable():
            itemInst = self.findItemId(id)
            if itemInst:
                return itemInst._count
        else:
            itemInstList = self.findItemsIdNotEquipped(id)
            return len(itemInstList)

        return 0

    def storeItem(self, id, count):
        if count <= 0:
            return None

        if not ItemTable()._allTemplates.has_key(id):
            return None

        temp = ItemTable()._allTemplates[id]
        if temp.isStackable():
            itemInst = ItemInstance(temp, count)
            if self.findItemId(id):
                itemInst._id = IdFactory().nextId()
                World().storeObject(itemInst)

            return self.storeItemInst(itemInst)

        ret = None
        for i in range(count):
            itemInst = ItemInstance(temp, 1)
            itemInst._id = IdFactory().nextId()
            World().storeObject(itemInst)
            ret = self.storeItemInst(itemInst)
        return ret

    def storeItemInst(self, itemInst):
        with self._lock:
            if itemInst._count <= 0:
                return None

            itemId = itemInst._itemId
            if itemInst._item.isStackable():
                findItemInst = self.findItemId(itemId)
                if findItemInst:
                    findItemInst._count += itemInst._count
                    self.updateItem(findItemInst)
                    return findItemInst

            itemInst._loc = self._loc
            chargeCount = itemInst._item.getMaxChargeCount()
            if itemId in (40006 , 40007, 40008, 140006, 140008, 41401):
                chargeCount -= random.randrange(5)
            if itemId == 20383:
                chargeCount = 50
            itemInst._chargeCount = chargeCount

            if itemInst._item._clsType == 0 and itemInst._item._weaponType:
                itemInst._remainingTime = itemInst._item.getLightFuel()
            else:
                itemInst._remainingTime = itemInst._item._maxUseTime

            itemInst._bless = itemInst._item._bless
            self._itemInsts += itemInst
            self.insertItem(itemInst)
            return itemInst

    def storeTradeItem(self, itemInst):
        if itemInst._item.isStackable():
            findItemInst = self.findItemId(itemInst._itemId)
            if findItemInst:
                findItemInst._count += itemInst._count
                self.updateItem(findItemInst)
                return findItemInst

        itemInst._loc = self._loc
        self._itemInsts += itemInst
        self.insertItem(itemInst)
        return itemInst

    def consumeItem(self, itemId, count):
        if count <= 0:
            return False

        if not ItemTable()._allTemplates.has_key(itemId):
            return False

        if ItemTable()._allTemplates[itemId].isStackable():
            itemInst = self.findItemId(itemId)
            if itemInst and itemInst._count >= count:
                self.removeItem(itemInst, count)
                return True
        else:
            itemInstList = self.findItemsId(itemId)
            if len(itemInstList) == count:
                for i in range(count):
                    self.removeItem(itemInstList[i], 1)
                return True
            elif len(itemInstList) > count:
                itemInstList.sort(key=lambda itemInst:itemInst._enchantLevel)
                for i in range(count):
                    self.removeItem(itemInstList[i], 1)
                return True

        return False

    def removeItem(self, objectId, count):
        return self.removeItemInst(self.getItem(objectId), count)

    def removeItemInst(self, itemInst, count):
        if not itemInst:
            return 0

        if itemInst._count <=0 or count <= 0:
            return 0

        if itemInst._count < count:
            count = itemInst._count

        if itemInst._count == count:
            itemId = itemInst._itemId
            # todo: 宠物 便簽 家具
            if itemId == 40314 or itemId == 40316:
                pass
            elif itemId >= 49016 and itemId <= 49025:
                pass
            elif itemId >= 41383 and itemId <= 41400:
                pass

            self._itemInsts.remove(itemInst)
            World().removeObject(itemInst)
        else:
            itemInst._count -= count
            self.updateItem(itemInst)

        return count

    def tradeItem(self, objectId, count, inventory):
        return self.tradeItemInst(self.getItem(objectId), count, inventory)

    def tradeItemInst(self, itemInst, count, inventory):
        with self._lock:
            if not itemInst:
                return None

            if itemInst._count <= 0 or count <= 0:
                return None

            if itemInst._isEquipped:
                return None

            if not self.checkItem(itemInst._item._itemId, count):
                return None

            if itemInst._count <= count:
                self._itemInsts.remove(itemInst)
                carryItem = itemInst
            else:
                itemInst._count -= count
                self.updateItem(itemInst)
                carryItem = ItemTable().createItem(itemInst._itemId)
                carryItem._count = itemInst._count
                carryItem._enchantLevel = itemInst._enchantLevel
                carryItem._isIdentified = itemInst._isIdentified
                carryItem.set_durability(itemInst._durability)
                carryItem._chargeCount = itemInst._chargeCount
                carryItem._remainingTime = itemInst._remainingTime
                carryItem._lastUsed = itemInst._lastUsed
                carryItem._bless = itemInst._bless
            return inventory.storeTradeItem(carryItem)

    def receiveDamage(self, objectId):
        return self.receiveDamageInst(self.getItem(objectId))

    def receiveDamageInst(self, itemInst, count = 1):
        return None

    def recoveryDamage(self, itemInst):
        return None

    def clearItems(self):
        for itemInst in self._itemInsts:
            World().removeObject(itemInst)
        self._itemInsts = []

    def loadItems(self):
        return

    def insertItem(self, itemInst):
        return

    def updateItem(self, itemInst, column = 0):
        return

    def deleteItem(self, itemInst):
        return
    '''