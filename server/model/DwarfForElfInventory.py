# -*- coding: utf-8 -*-

import logging
from Inventory import Inventory
from Datatables import Session,Character_Elf_Warehouse
from server.datatables.ItemTable import ItemTable
from server.model.Instance.ItemInstance import ItemInstance
from server.utils.TimeUtil import TimeUtil

class DwarfForElfInventory(Inventory):
    '''
    精灵仓库系统
    '''
    def __init__(self, pc):
        Inventory.__init__(self)
        self._owner = pc

    def loadItems(self):
        '''
        加载玩家的精灵仓库中的道具到游戏世界中
        :return:None
        '''
        from server.model.World import World

        try:
            with Session() as session:
                for rs in session.query(Character_Elf_Warehouse).filter(Character_Elf_Warehouse.account_name == self._owner._accountName).all():
                    item = ItemInstance()
                    item._id = rs.id
                    item.setItem(ItemTable()._allTemplates[rs.item_id])
                    item._count = rs.count
                    item._isEquipped = False
                    item._enchantLevel = rs.enchantlvl
                    item._isIdentified = rs.is_id != 0
                    item.set_durability(rs.durability)
                    item._chargeCount = rs.charge_count
                    item._remainingTime = rs.remaining_time
                    item._lastUsed = TimeUtil.dt2ts(rs.last_used)
                    item._bless = rs.bless
                    item._attrEnchantKind = rs.attr_enchant_kind
                    item._attrEnchantLevel = rs.attr_enchant_level
                    item._FireMr = rs.firemr
                    item._WaterMr = rs.watermr
                    item._EarthMr = rs.earthmr
                    item._WindMr = rs.windmr
                    item._addSp = rs.addsp
                    item._addHp = rs.addhp
                    item._addMp = rs.addmp
                    item._Hpr = rs.hpr
                    item._Mpr = rs.mpr
                    self._itemInsts.append(item)
                    World().storeObject(item)
        except Exception as e:
            logging.error(e)

    def insertItem(self, itemInst):
        '''
        存入道具
        :param itemInst:道具(ItemInstance)
        :return:None
        '''
        try:
            item = Character_Elf_Warehouse(id = itemInst._id,
                                           account_name = self._owner._accountName,
                                           item_id = itemInst._itemId,
                                           item_name = itemInst._item._name,
                                           count = itemInst._count,
                                           is_equipped = 0,
                                           enchantlvl = itemInst._enchantLevel,
                                           is_id = int(itemInst._isIdentified),
                                           durability = itemInst._durability,
                                           charge_count = itemInst._chargeCount,
                                           remaining_time = itemInst._remainingTime,
                                           last_used = TimeUtil.ts2dt(itemInst._lastUsed),
                                           bless = itemInst._bless,
                                           attr_enchant_kind = itemInst._attrEnchantKind,
                                           attr_enchant_level = itemInst._attrEnchantLevel,
                                           firemr = itemInst._FireMr,
                                           watermr = itemInst._WaterMr,
                                           earthmr = itemInst._EarthMr,
                                           windmr = itemInst._WindMr,
                                           addsp = itemInst._addSp,
                                           addhp = itemInst._addHp,
                                           addmp = itemInst._addMp,
                                           hpr = itemInst._Hpr,
                                           mpr = itemInst._Mpr)
            with Session() as session:
                session.add(item)
        except Exception as e:
            logging.error(e)

    def updateItem(self, itemInst, colmn = 0):
        '''
        更新玩家仓库道具数目
        :param itemInst:道具(ItemInstance)
        :param colmn:
        :return:None
        '''
        try:
            with Session() as session:
                session.query(Character_Elf_Warehouse).filter(Character_Elf_Warehouse.id == itemInst._id).update({Character_Elf_Warehouse.count : itemInst._count})
        except Exception as e:
            logging.error(e)

    def deleteItem(self, itemInst):
        '''
        删除仓库中的道具
        :param itemInst:道具(ItemInstance)
        :return:None
        '''
        try:
            with Session() as session:
                session.query(Character_Elf_Warehouse).filter(Character_Elf_Warehouse.id == itemInst._id).delete()
        except Exception as e:
            logging.error(e)
        self._itemInsts.remove(itemInst)