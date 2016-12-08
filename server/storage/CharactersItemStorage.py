# -*- coding: utf-8 -*-

class CharactersItemStorage():
    _instance = None
    @classmethod
    def create(cls):
        from server.storage.MySqlCharactersItemStorage import MySqlCharactersItemStorage

        if not cls._instance:
            cls._instance = MySqlCharactersItemStorage()
        return cls._instance

    def updateFireMr(self, item_inst):
        raise NotImplementedError

    def updateWaterMr(self, item_inst):
        raise NotImplementedError

    def updateEarthMr(self, item_inst):
        raise NotImplementedError

    def updateWindMr(self, item_inst):
        raise NotImplementedError

    def updateaddSp(self, item_inst):
        raise NotImplementedError

    def updateaddHp(self, item_inst):
        raise NotImplementedError

    def updateaddMp(self, item_inst):
        raise NotImplementedError

    def updateHpr(self, item_inst):
        raise NotImplementedError

    def updateMpr(self, item_inst):
        raise NotImplementedError

    def loadItems(self, objId):
        raise NotImplementedError

    def storeItem(self, objId, item_inst):
        raise NotImplementedError

    def deleteItem(self, item_inst):
        raise NotImplementedError

    def updateItemId(self, item_inst):
        raise NotImplementedError

    def updateItemCount(self, item_inst):
        raise NotImplementedError

    def updateItemIdentified(self, item_inst):
        raise NotImplementedError

    def updateItemEquipped(self, item_inst):
        raise NotImplementedError

    def updateItemEnchantLevel(self, item_inst):
        raise NotImplementedError

    def updateItemDurability(self, item_inst):
        raise NotImplementedError

    def updateItemChargeCount(self, item_inst):
        raise NotImplementedError

    def updateItemRemainingTime(self, item_inst):
        raise NotImplementedError

    def updateItemDelayEffect(self, item_inst):
        raise NotImplementedError

    def getItemCount(self, objId):
        raise NotImplementedError

    def updateItemBless(self, item_inst):
        raise NotImplementedError

    def updateItemAttrEnchantKind(self, item_inst):
        raise NotImplementedError

    def updateItemAttrEnchantLevel(self, item_inst):
        raise NotImplementedError
