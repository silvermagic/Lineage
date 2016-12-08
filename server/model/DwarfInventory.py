# -*- coding: utf-8 -*-

import logging
from sqlalchemy import and_
from Inventory import Inventory
from Datatables import Session,character_warehouse,accounts,characters
from server.datatables.ItemTable import ItemTable
from server.model.Instance.ItemInstance import ItemInstance
from server.utils.TimeUtil import TimeUtil

class DwarfInventory(Inventory):
    '''
    侏儒仓库系统
    '''
    def __init__(self, pc):
        Inventory.__init__(self)
        self._owner = pc

    def loadItems(self):
        '''
        加载玩家侏儒仓库道具到游戏世界中
        :return:None
        '''
        from server.model.World import World

        try:
            with Session() as session:
                for rs in session.query(character_warehouse).filter(character_warehouse.account_name == self._owner._accountName).all():
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
                    self._item_insts.append(item)
                    World().storeObject(item)
        except Exception as e:
            logging.error(e)


    def insertItem(self, item_inst):
        '''
        存放道具
        :param itemInst:道具(ItemInstance)
        :return:None
        '''
        try:
            item = character_warehouse(id = item_inst._id,
                                       account_name = self._owner._accountName,
                                       item_id = item_inst._itemId,
                                       item_name = item_inst._item._name,
                                       count = item_inst._count,
                                       is_equipped = 0,
                                       enchantlvl = item_inst._enchantLevel,
                                       is_id = int(item_inst._isIdentified),
                                       durability = item_inst._durability,
                                       charge_count = item_inst._chargeCount,
                                       remaining_time = item_inst._remainingTime,
                                       last_used = TimeUtil.ts2dt(item_inst._lastUsed),
                                       bless = item_inst._bless,
                                       attr_enchant_kind = item_inst._attrEnchantKind,
                                       attr_enchant_level = item_inst._attrEnchantLevel,
                                       firemr = item_inst._FireMr,
                                       watermr = item_inst._WaterMr,
                                       earthmr = item_inst._EarthMr,
                                       windmr = item_inst._WindMr,
                                       addsp = item_inst._addSp,
                                       addhp = item_inst._addHp,
                                       addmp = item_inst._addMp,
                                       hpr = item_inst._Hpr,
                                       mpr = item_inst._Mpr)
            with Session() as session:
                session.add(item)
        except Exception as e:
            logging.error(e)

    def updateItem(self, item_inst, colmn = 0):
        '''
        更新玩家仓库道具数目
        :param item_inst:道具(ItemInstance)
        :param colmn:
        :return:None
        '''
        try:
            with Session() as session:
                session.query(character_warehouse).filter(character_warehouse.id == item_inst._id).update({character_warehouse.count : item_inst._count})
        except Exception as e:
            logging.error(e)

    def deleteItem(self, item_inst):
        '''
        删除仓库中的道具
        :param item_inst:道具(ItemInstance)
        :return:None
        '''
        try:
            with Session() as session:
                session.query(character_warehouse).filter(character_warehouse.id == item_inst._id).delete()
        except Exception as e:
            logging.error(e)
        self._item_insts.remove(item_inst)
    '''
    @classmethod
    def present(cls, itemid, enchant, count, account=None, lvl=None, accountList=None):
        if not accountList:
            accountList = []

        if not ItemTable()._allTemplates.has_key(itemid):
            raise Exception("指定的道具编号不存在.")
        try:
            if account:
                with Session() as session:
                    if account.lower() == '*':
                        for rs in session.query(Accounts).all():
                            accountList.append(rs.login)
                    else:
                        for rs in session.query(Accounts).filter(Accounts.login == account).all():
                            accountList.append(rs.login)
            elif lvl:
                minlvl, maxlvl = lvl
                with Session() as session:
                    for rs in session.query(Characters).filter(and_(Characters.level >= minlvl, Characters.level <= maxlvl)).all():
                        accountList.append(rs.login)

            isStackable = ItemTable()._allTemplates[itemid].isStackable()
            for name in accountList:
                if isStackable:
                    item_inst = ItemTable().createItem(itemid)
                    item = Character_Warehouse(id=item_inst._id,
                                               account_name=name,
                                               item_id=item_inst._itemId,
                                               item_name=item_inst._item._name,
                                               count=count,
                                               is_equipped=0,
                                               enchantlvl=enchant,
                                               is_id=int(item_inst._isIdentified),
                                               durability=item_inst._durability,
                                               charge_count=item_inst._chargeCount,
                                               remaining_time=item_inst._remainingTime)
                    with Session() as session:
                        session.add(item)
                else:
                    with Session() as session:
                        for i in range(count):
                            item_inst = ItemTable().createItem(itemid)
                            item = Character_Warehouse(id=item_inst._id,
                                                       account_name=name,
                                                       item_id=item_inst._itemId,
                                                       item_name=item_inst._item._name,
                                                       count=item_inst._count,
                                                       is_equipped=0,
                                                       enchantlvl=enchant,
                                                       is_id=int(item_inst._isIdentified),
                                                       durability=item_inst._durability,
                                                       charge_count=item_inst._chargeCount,
                                                       remaining_time=item_inst._remainingTime)
                            session.add(item)

        except Exception as e:
            logging.error(e)
    '''