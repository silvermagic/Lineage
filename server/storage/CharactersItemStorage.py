# -*- coding: utf-8 -*-

class CharactersItemStorage():
    _instance = None
    @classmethod
    def create(cls):
        from server.storage.MySqlCharactersItemStorage import MySqlCharactersItemStorage

        if not cls._instance:
            cls._instance = MySqlCharactersItemStorage()
        return cls._instance

    def updateFireMr(self, itemInst):
        raise NotImplementedError

    def updateWaterMr(self, itemInst):
        raise NotImplementedError

    def updateEarthMr(self, itemInst):
        raise NotImplementedError

    def updateWindMr(self, itemInst):
        raise NotImplementedError

    def updateaddSp(self, itemInst):
        raise NotImplementedError

    def updateaddHp(self, itemInst):
        raise NotImplementedError

    def updateaddMp(self, itemInst):
        raise NotImplementedError

    def updateHpr(self, itemInst):
        raise NotImplementedError

    def updateMpr(self, itemInst):
        raise NotImplementedError

    def loadItems(self, objId):
        raise NotImplementedError

    def storeItem(self, objId, itemInst):
        raise NotImplementedError

    def deleteItem(self, itemInst):
        raise NotImplementedError

    def updateItemId(self, itemInst):
        raise NotImplementedError

    def updateItemCount(self, itemInst):
        raise NotImplementedError

    def updateItemIdentified(self, itemInst):
        raise NotImplementedError

    def updateItemEquipped(self, itemInst):
        raise NotImplementedError

    def updateItemEnchantLevel(self, itemInst):
        raise NotImplementedError

    def updateItemDurability(self, itemInst):
        raise NotImplementedError

    def updateItemChargeCount(self, itemInst):
        raise NotImplementedError

    def updateItemRemainingTime(self, itemInst):
        raise NotImplementedError

    def updateItemDelayEffect(self, itemInst):
        raise NotImplementedError

    def getItemCount(self, objId):
        raise NotImplementedError

    def updateItemBless(self, itemInst):
        raise NotImplementedError

    def updateItemAttrEnchantKind(self, itemInst):
        raise NotImplementedError

    def updateItemAttrEnchantLevel(self, itemInst):
        raise NotImplementedError
