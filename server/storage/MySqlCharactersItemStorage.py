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

    def storeItem(self, objId, item_inst):
        with Session() as session:
            item = character_items(id=item_inst._id,
                                   item_id=item_inst._itemId,
                                   char_id=objId,
                                   item_name=item_inst._item._name,
                                   count=item_inst._count,
                                   is_equipped=0,
                                   enchantlvl=item_inst._enchantLevel,
                                   is_id=int(item_inst._isIdentified),
                                   durability=item_inst._durability,
                                   charge_count=item_inst._chargeCount,
                                   remaining_time=item_inst._remainingTime,
                                   last_used=TimeUtil.ts2dt(item_inst._lastUsed),
                                   bless=item_inst._bless,
                                   attr_enchant_kind=item_inst._attrEnchantKind,
                                   attr_enchant_level=item_inst._attrEnchantLevel,
                                   firemr=item_inst._FireMr,
                                   watermr=item_inst._WaterMr,
                                   earthmr=item_inst._EarthMr,
                                   windmr=item_inst._WindMr,
                                   addsp=item_inst._addSp,
                                   addhp=item_inst._addHp,
                                   addmp=item_inst._addMp,
                                   hpr=item_inst._Hpr,
                                   mpr=item_inst._Mpr)
            session.add(item)

    def deleteItem(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).delete()

    def updateFireMr(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.firemr : item_inst._FireMr})
            item_inst._lastStatus.firemr = item_inst._FireMr

    def updateWaterMr(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.watermr : item_inst._WaterMr})
            item_inst._lastStatus.watermr = item_inst._WaterMr

    def updateEarthMr(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.earthmr : item_inst._EarthMr})
            item_inst._lastStatus.earthmr = item_inst._EarthMr

    def updateWindMr(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.windmr : item_inst._WindMr})
            item_inst._lastStatus.windmr = item_inst._WindMr

    def updateaddSp(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.addsp : item_inst._addSp})
            item_inst._lastStatus.addsp = item_inst._addSp

    def updateaddHp(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.addhp : item_inst._addHp})
            item_inst._lastStatus.addhp = item_inst._addHp

    def updateaddMp(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.addmp : item_inst._addMp})
            item_inst._lastStatus.addmp = item_inst._addMp

    def updateHpr(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.hpr : item_inst._Hpr})
            item_inst._lastStatus.hpr = item_inst._Hpr

    def updateMpr(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.mpr : item_inst._Mpr})
            item_inst._lastStatus.mpr = item_inst._Mpr

    def updateItemId(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.item_id : item_inst._itemId})
            item_inst._lastStatus.item_id = item_inst._itemId

    def updateItemCount(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.count : item_inst._count})
            item_inst._lastStatus.count = item_inst._count

    def updateItemDurability(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.durability : item_inst._durability})
            item_inst._lastStatus.durability = item_inst._durability

    def updateItemChargeCount(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.charge_count : item_inst._chargeCount})
            item_inst._lastStatus.charge_count = item_inst._chargeCount

    def updateItemRemainingTime(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.remaining_time : item_inst._remainingTime})
            item_inst._lastStatus.remaining_time = item_inst._remainingTime

    def updateItemEnchantLevel(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.enchantlvl : item_inst._enchantLevel})
            item_inst._lastStatus.enchantlvl = item_inst._enchantLevel

    def updateItemEquipped(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.is_equipped : int(item_inst._isEquipped)})
            item_inst._lastStatus.is_equipped = item_inst._isEquipped

    def updateItemIdentified(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.is_id : int(item_inst._isIdentified)})
            item_inst._lastStatus.is_id = item_inst._isIdentified

    def updateItemDelayEffect(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.last_used : TimeUtil.ts2dt(item_inst._lastUsed)})
            item_inst._lastStatus.last_used = item_inst._lastUsed

    def updateItemBless(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.bless: item_inst._bless})
            item_inst._lastStatus.bless = item_inst._bless

    def updateItemAttrEnchantKind(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.attr_enchant_kind: item_inst._attrEnchantKind})
            item_inst._lastStatus.attr_enchant_kind = item_inst._attrEnchantKind

    def updateItemAttrEnchantLevel(self, item_inst):
        with Session() as session:
            session.query(character_items).filter(character_items.id == item_inst._id).update(
                {character_items.attr_enchant_level: item_inst._attrEnchantLevel})
            item_inst._lastStatus.attr_enchant_level = item_inst._attrEnchantLevel

    def getItemCount(self, objId):
        with Session() as session:
            count = session.query(character_items).filter(character_items.char_id == objId).count()
        return count