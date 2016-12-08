# -*- coding: utf-8 -*-

import threading,random,copy
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
        self._item_insts = []
        self._lock = threading.RLock()

    def getWeight(self):
        '''
        获取仓库中所有道具的总重量
        :return:重量(int)
        '''
        weight = 0
        for item in self._item_insts:
            weight += item.getWeight()
        return weight

    def getItem(self, objectId):
        '''
        获取仓库中的道具实例
        :param objectId:道具实例对象ID(int)
        :return:道具实例(ItemInstance)
        '''
        for item in self._item_insts:
            if item._id == objectId:
                return item

        return None

    def findItemId(self, itemid):
        '''
        获取仓库中的道具实例
        :param itemid:道具模板ID(int)
        :return:道具实例(ItemInstance)
        '''
        for item in self._item_insts:
            if item._itemId == id:
                return item

        return None

    def findItemsId(self, itemid):
        '''
        获取仓库中道具实例集合
        :param itemid:道具模板ID(int)
        :return:道具实例集合(ItemInstance[])
        '''
        itemList = []
        for item in self._item_insts:
            if item._itemId == itemid:
                itemList += item

        return itemList

    def findItemsIdNotEquipped(self, itemid):
        '''
        获取仓库中未装备的道具实例集合
        :param itemid:道具模板ID(int)
        :return:道具实例集合(ItemInstance[])
        '''
        itemList = []
        for item in self._item_insts:
            if item._itemId == itemid:
                if not item._isEquipped:
                    itemList += item

        return itemList

    def countItems(self, itemid):
        '''
        获取仓库中特定道具的个数
        :param itemid:道具模板ID(int)
        :return:道具个数(int)
        '''
        if not ItemTable()._allTemplates.has_key(itemid):
            return 0

        if ItemTable()._allTemplates[itemid].isStackable():
            item_inst = self.findItemId(itemid)
            if item_inst:
                return item_inst._count
        else:
            item_instList = self.findItemsIdNotEquipped(itemid)
            return len(item_instList)

        return 0

    def checkItemNotEquipped(self, itemid, count):
        '''
        检测仓库中是否存在count个没有装备的道具
        :param itemid:道具模板ID(int)
        :param count:道具个数(int)
        :return:True/False
        '''
        if count == 0:
            return True

        return count <= self.countItems(itemid)

    def checkAddItem(self, item_inst, count):
        '''
        检测是否可以添加count个道具实例到宠物背包中
        :param item_inst:道具实例(ItemInstance)
        :param count:道具个数(int)
        :return:int
        '''
        if not item_inst:
            return -1

        if item_inst._count <= 0 or count <= 0:
            return -1

        # 是否超过仓库容量
        if len(self._item_insts) > Config.getint('altsettings', 'MaxNpcItem') \
                or (len(self._item_insts) == Config.getint('altsettings', 'MaxNpcItem')
                    and (not item_inst._item.isStackable() or self.checkItem(item_inst._itemId))):
            return Inventory.SIZE_OVER

        # 是否超过宠物的负重率
        weight = int(self.getWeight() + item_inst._item._weight * count / 1000 + 1)
        if weight < 0 or (item_inst._item._weight * count / 1000 < 0):
            return Inventory.WEIGHT_OVER
        if weight > (Inventory.MAX_WEIGHT * float(Config.getint('rates', 'RateWeightLimitforPet'))):
            return Inventory.WEIGHT_OVER

        # 是否超过道具总数限制
        itemExist = self.findItemId(item_inst._itemId)
        if itemExist and (itemExist._count + count) > Inventory.MAX_AMOUNT:
            return Inventory.AMOUNT_OVER

        return Inventory.OK

    def checkAddItemToWarehouse(self, item_inst, count, type):
        '''
        检测是否可以添加count个道具实例到玩家仓库或血盟仓库中
        :param item_inst:道具实例(ItemInstance)
        :param count:道具个数(int)
        :param type:仓库类型(int)
        :return:int
        '''
        if not item_inst:
            return -1

        if item_inst._count <= 0 or count <= 0:
            return -1

        maxSize = 100
        if type == Inventory.WAREHOUSE_TYPE_PERSONAL:
            maxSize = Config.getint('altsettings', 'MaxPersonalWarehouseItem')
        elif type == Inventory.WAREHOUSE_TYPE_CLAN:
            maxSize = Config.getint('altsettings', 'MaxClanWarehouseItem')

        if len(self._item_insts) > maxSize \
                or (len(self._item_insts) == maxSize
                    and (not item_inst._item.isStackable() or self.checkItem(item_inst._itemId))):
            return Inventory.SIZE_OVER

        return Inventory.OK

    def checkItem(self, itemid, count=1):
        '''
        检测仓库中是否存在count个道具实例
        :param itemid:道具模板ID(int)
        :param count:道具个数(int)
        :return:True/False
        '''
        if count == 0:
            return True

        if ItemTable()._allTemplates.has_key(itemid):
            # 物品是否可叠加,例如材料类的皮革就是可叠加的,就直接返回数量;例如武器类的双手剑就是不可以叠加的,需要找出所有实例
            if ItemTable()._allTemplates[itemid].isStackable():
                item = self.findItemId(itemid)
                if item and item._count >= count:
                    return True
            else:
                itemList = self.findItemsId(itemid)
                if len(itemList) >= count:
                    return True

        return False

    def checkItems(self, ids, counts=None):
        '''
        检测仓库中是否存在count个特定道具
        :param ids:道具模板ID集合(int[])
        :param counts:道具个数集合(int[])
        :return:True/False
        '''
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

    def checkEnchantItem(self, itemid, enchant, count):
        '''
        检测仓库中是否存在count个强化次数为enchant的道具实例
        :param itemid:道具模板ID(int)
        :param enchant:道具强化次数(int)
        :param count:道具个数(int)
        :return:True/False
        '''
        num = 0
        for item_inst in self._item_insts:
            if item_inst._isEquipped:
                continue
            if item_inst._itemId == itemid and item_inst._enchantLevel == enchant:
                num += 1
                if num == count:
                    return True
        return False

    def consumeItem(self, itemid, count):
        '''
        消耗道具,例如箭矢 魔法宝石 精灵玉的消耗
        :param itemid:道具模板ID(int)
        :param count:消耗的道具个数(int)
        :return:消耗是否成功(True/False)
        '''
        if count <= 0 or not ItemTable()._allTemplates.has_key(itemid):
            return False

        if ItemTable()._allTemplates[itemid].isStackable():
            item_inst = self.findItemId(itemid)
            if item_inst and item_inst._count >= count:
                self.removeItem(inst=item_inst, count=count)
                return True
        else:
            item_insts = self.findItemsId(itemid)
            if len(item_insts) == count:
                for item_inst in item_insts:
                    self.removeItem(inst=item_inst, count=1)
                return True
            elif len(item_insts) > count:
                for item_inst in sorted(item_insts, key=lambda inst: inst._enchantLevel):
                    self.removeItem(inst=item_inst, count=1)
                return True
        return False

    def consumeEnchantItem(self, itemid, enchant, count):
        '''
        道具强化失败时消耗道具,例如+3双刀强化失败会消失
        :param itemid:道具模板ID(int)
        :param enchant:道具强化等级(int)
        :param count:消耗的道具个数(int)
        :return:True/False
        '''
        for item_inst in self._item_insts:
            if item_inst._isEquipped:
                continue
            if item_inst._itemId == itemid and item_inst._enchantLevel == enchant:
                self.removeItem(inst=item_inst)
                return True
        return False

    def removeItem(self, objid=None, inst=None, count=None):
        '''
        调用删除函数移除仓库中的道具,并将其从游戏世界中移除
        :param objid:道具对象ID(int)
        :param inst:道具实例(ItemInstance)
        :param count:道具个数(int)
        :return:int
        '''
        if objid:
            item_inst = self.getItem(objid)
            if not item_inst:
                return 0
        elif inst:
            item_inst = inst
        else:
            return 0

        if not count:
            count = item_inst._count
        elif item_inst._count < count:
            count = item_inst._count
        if count <= 0:
            return 0

        if item_inst._count == count:
            itemId = item_inst._itemId
            # todo: 宠物 便簽 家具
            if itemId == 40314 or itemId == 40316:
                pass
            elif itemId >= 49016 and itemId <= 49025:
                pass
            elif itemId >= 41383 and itemId <= 41400:
                pass

            self.deleteItem(item_inst)
            World().removeObject(item_inst)
        else:
            item_inst._count -= count
            self.updateItem(item_inst)

        return count

    def storeItem(self, itemid, count):
        '''
        向仓库存入道具
        :param itemid:道具模板ID(int)
        :param count:道具个数(int)
        :return:道具实例(ItemInstance)
        '''
        if count <= 0 or not ItemTable()._allTemplates.has_key(itemid):
            return None

        with self._lock:
            item = ItemTable()._allTemplates[itemid]
            if item.isStackable(): # 道具是否可叠加
                findItem = self.findItemId(itemid)
                if not findItem: # 如果已经存在此类道具直接更新道具数目即可
                    findItem._count += count
                    self.updateItem(findItem)
                    return findItem
                # 存入道具并保存到游戏世界
                inst = ItemInstance(item, count)
                inst._loc = copy.copy(self._loc)
                World().storeObject(inst)
                self._item_insts.append(inst)
                self.insertItem(inst)
                return inst
            else:
                # 不可叠加道具需要循环存入道具实例
                c = None
                inst = ItemInstance(item, 1)
                inst._loc = copy.copy(self._loc)
                for i in range(count):
                    c = copy.deepcopy(inst)
                    c._id = IdFactory().nextId()
                    World().storeObject(c)
                    self._item_insts.append(c)
                    self.insertItem(c)
                return c

    '''
    def storeTradeItem(self, item_inst):
        if item_inst._item.isStackable():
            finditem_inst = self.findItemId(item_inst._itemId)
            if finditem_inst:
                finditem_inst._count += item_inst._count
                self.updateItem(finditem_inst)
                return finditem_inst

        item_inst._loc = self._loc
        self._item_insts += item_inst
        self.insertItem(item_inst)
        return item_inst

    def tradeItem(self, objectId, count, inventory):
        return self.tradeitem_inst(self.getItem(objectId), count, inventory)

    def tradeitem_inst(self, item_inst, count, inventory):
        with self._lock:
            if not item_inst:
                return None

            if item_inst._count <= 0 or count <= 0:
                return None

            if item_inst._isEquipped:
                return None

            if not self.checkItem(item_inst._item._itemId, count):
                return None

            if item_inst._count <= count:
                self._item_insts.remove(item_inst)
                carryItem = item_inst
            else:
                item_inst._count -= count
                self.updateItem(item_inst)
                carryItem = ItemTable().createItem(item_inst._itemId)
                carryItem._count = item_inst._count
                carryItem._enchantLevel = item_inst._enchantLevel
                carryItem._isIdentified = item_inst._isIdentified
                carryItem.set_durability(item_inst._durability)
                carryItem._chargeCount = item_inst._chargeCount
                carryItem._remainingTime = item_inst._remainingTime
                carryItem._lastUsed = item_inst._lastUsed
                carryItem._bless = item_inst._bless
            return inventory.storeTradeItem(carryItem)
    '''

    def receiveDamage(self, objid=None, inst=None, count = 1):
        '''
        道具的耐久度和损坏度计算
        :param objid:道具对象ID(int)
        :param inst:道具实例(ItemInstance)
        :param count:损坏度(int)
        :return:道具实例(ItemInstance)
        '''
        return None

    def recoveryDamage(self, item_inst):
        '''
        道具的耐久度和损坏度修复计算
        :param inst:道具实例(ItemInstance)
        :return:道具实例(ItemInstance)
        '''
        return None

    def clearItems(self):
        '''
        清除仓库中的道具
        :return:None
        '''
        for item_inst in self._item_insts:
            World().removeObject(item_inst)
        self._item_insts = []

    def loadItems(self):
        return

    def insertItem(self, item_inst):
        return

    def updateItem(self, item_inst, column = 0):
        '''
        更新道具状态
        :param item_inst:道具实例(ItemInstance)
        :param column:需要更新的道具属性集(long)
        :return:None
        '''
        return

    def deleteItem(self, item_inst):
        '''
        删除仓库中的道具(子类要重写此方法移除数据库中的数据)
        :param item_inst:
        :return:
        '''
        self._item_insts.remove(item_inst)