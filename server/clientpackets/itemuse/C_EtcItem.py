# -*- coding: utf-8 -*-

from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_ItemName import S_ItemName
from etcitem.C_EtcItemBase import C_EtcItemBase
from etcitem.C_EnchantScroll import C_EnchantScroll

class C_EtcItem():
    def __init__(self, fd, item_inst):
        self._fd = fd
        self._pc = fd._client._activeChar
        self._item_inst = item_inst

    def handle(self):
        return self._handle(self._fd, self._item_inst)

    def _handle(self, fd, item_inst):
        if not self.LevelLimit(item_inst):
            return

        if self.PreHandle(item_inst):
            return

        item_id = item_inst._itemId
        handler = C_EtcItemBase(fd, item_inst)
        if item_id in C_EnchantScroll.item_ids:
            handler = C_EnchantScroll(fd, item_inst)
        handler.handle()

    def LevelLimit(self, item_inst):
        item_minlvl = item_inst._item._minLevel
        item_maxlvl = item_inst._item._maxLevel

        if item_minlvl != 0 and item_minlvl > self._pc.getLevel() and not self._pc._gm:
            self._pc.sendPackets.S_ServerMessage(318, str(item_minlvl))
            return False
        elif item_maxlvl != 0 and item_maxlvl < self._pc.getLevel() and not self._pc._gm:
            self._pc.sendPackets.S_ServerMessage(673, str(item_maxlvl))
            return False

        return True

    def PreHandle(self, item_inst):
        type = item_inst._item._type
        item_id = item_inst._itemId

        if type == 0:  # 选着箭矢
            self._pc._inventory._arrowId = item_id
            self._pc.sendPackets(S_ServerMessage(452, item_inst.getLogName()))
            return True
        elif type == 15:
            self._pc._inventory._stingId = item_id
            self._pc.sendPackets(S_ServerMessage(452, item_inst.getLogName()))
            return True
        elif type == 16:
            # todo: 宝箱系统
            return True
        elif type == 2:
            if item_inst._remainingTime <= 0 and item_id != 40004:  # 魔法灯笼
                return True

            if item_inst._isNowLighting:
                item_inst._isNowLighting = False
                self._pc.turnOnOffLight()
            else:
                item_inst._isNowLighting = True
                self._pc.turnOnOffLight()
            self._pc.sendPackets(S_ItemName(item_inst))
            return True

        return False