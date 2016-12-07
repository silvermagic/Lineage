# -*- coding: utf-8 -*-

import logging
from Datatables import Session,character_items
from server.utils.TimeUtil import TimeUtil
from server.datatables.ItemTable import ItemTable
from server.model.Instance.ItemInstance import ItemInstance
from CharactersItemStorage import CharactersItemStorage

class MySqlCharactersItemStorage(CharactersItemStorage):
    def loadItems(self, objId):
        items = []
        with Session() as session:
            for rs in session.query(character_items).filter(character_items.char_id == objId).all():
                itemId = rs.item_id
                if not ItemTable()._allTemplates.has_key(itemId):
                    logging.warning('item id:' + str(itemId) + ' not found')
                    continue

                item = ItemInstance()
                item._id = rs.id
                item.setItem(ItemTable()._allTemplates[itemId])
                item._count = rs.count
                item._isEquipped = rs.is_equipped != 0
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
                item._lastStatus.updateAll()
                items.append(item)

        return items

    def storeItem(self, objId, itemInst):
        with Session() as session:
            item = character_items(id=itemInst._id,
                                   item_id=itemInst._itemId,
                                   char_id=objId,
                                   item_name=itemInst._item._name,
                                   count=itemInst._count,
                                   is_equipped=0,
                                   enchantlvl=itemInst._enchantLevel,
                                   is_id=int(itemInst._isIdentified),
                                   durability=itemInst._durability,
                                   charge_count=itemInst._chargeCount,
                                   remaining_time=itemInst._remainingTime,
                                   last_used=TimeUtil.ts2dt(itemInst._lastUsed),
                                   bless=itemInst._bless,
                                   attr_enchant_kind=itemInst._attrEnchantKind,
                                   attr_enchant_level=itemInst._attrEnchantLevel,
                                   firemr=itemInst._FireMr,
                                   watermr=itemInst._WaterMr,
                                   earthmr=itemInst._EarthMr,
                                   windmr=itemInst._WindMr,
                                   addsp=itemInst._addSp,
                                   addhp=itemInst._addHp,
                                   addmp=itemInst._addMp,
                                   hpr=itemInst._Hpr,
                                   mpr=itemInst._Mpr)
            session.add(item)

    def deleteItem(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).delete()

    def updateFireMr(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.firemr : itemInst._FireMr})
            itemInst._lastStatus.firemr = itemInst._FireMr

    def updateWaterMr(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.watermr : itemInst._WaterMr})
            itemInst._lastStatus.watermr = itemInst._WaterMr

    def updateEarthMr(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.earthmr : itemInst._EarthMr})
            itemInst._lastStatus.earthmr = itemInst._EarthMr

    def updateWindMr(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.windmr : itemInst._WindMr})
            itemInst._lastStatus.windmr = itemInst._WindMr

    def updateaddSp(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.addsp : itemInst._addSp})
            itemInst._lastStatus.addsp = itemInst._addSp

    def updateaddHp(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.addhp : itemInst._addHp})
            itemInst._lastStatus.addhp = itemInst._addHp

    def updateaddMp(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.addmp : itemInst._addMp})
            itemInst._lastStatus.addmp = itemInst._addMp

    def updateHpr(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.hpr : itemInst._Hpr})
            itemInst._lastStatus.hpr = itemInst._Hpr

    def updateMpr(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.mpr : itemInst._Mpr})
            itemInst._lastStatus.mpr = itemInst._Mpr

    def updateItemId(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.item_id : itemInst._itemId})
            itemInst._lastStatus.item_id = itemInst._itemId

    def updateItemCount(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.count : itemInst._count})
            itemInst._lastStatus.count = itemInst._count

    def updateItemDurability(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.durability : itemInst._durability})
            itemInst._lastStatus.durability = itemInst._durability

    def updateItemChargeCount(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.charge_count : itemInst._chargeCount})
            itemInst._lastStatus.charge_count = itemInst._chargeCount

    def updateItemRemainingTime(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.remaining_time : itemInst._remainingTime})
            itemInst._lastStatus.remaining_time = itemInst._remainingTime

    def updateItemEnchantLevel(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.enchantlvl : itemInst._enchantLevel})
            itemInst._lastStatus.enchantlvl = itemInst._enchantLevel

    def updateItemEquipped(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.is_equipped : int(itemInst._isEquipped)})
            itemInst._lastStatus.is_equipped = itemInst._isEquipped

    def updateItemIdentified(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.is_id : int(itemInst._isIdentified)})
            itemInst._lastStatus.is_id = itemInst._isIdentified

    def updateItemDelayEffect(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.last_used : TimeUtil.ts2dt(itemInst._lastUsed)})
            itemInst._lastStatus.last_used = itemInst._lastUsed

    def updateItemBless(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.bless: itemInst._bless})
            itemInst._lastStatus.bless = itemInst._bless

    def updateItemAttrEnchantKind(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.attr_enchant_kind: itemInst._attrEnchantKind})
            itemInst._lastStatus.attr_enchant_kind = itemInst._attrEnchantKind

    def updateItemAttrEnchantLevel(self, itemInst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == itemInst._id).update(
                {character_items.attr_enchant_level: itemInst._attrEnchantLevel})
            itemInst._lastStatus.attr_enchant_level = itemInst._attrEnchantLevel

    def getItemCount(self, objId):
        with Session() as session:
            count = session.query(character_items).filter(character_items.char_id == objId).count()
        return count