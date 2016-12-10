# -*- coding: utf-8 -*-

import time,logging
from server.clientpackets.ClientBasePacket import ClientBasePacket
from server.model.PcInventory import PcInventory
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.clientpackets.itemuse.C_EtcItem import C_EtcItem
from server.clientpackets.itemuse.C_WeaponItem import C_WeaponItem
from server.clientpackets.itemuse.C_ArmorItem import C_ArmorItem

class C_ItemUse(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)
        self._client = client
        objid = self.readD()
        pc = client._activeChar
        if pc._ghost: # 幽灵之家活动不允许使用道具
            return
        item_inst = pc._inventory.getItem(objid)

        if not item_inst or pc._isDead:
            return

        use_type = item_inst._item._useType
        if use_type == -1: # 不能使用的物品
            pc.sendPackets(S_ServerMessage(74, item_inst.getLogName()))
            return

        if pc._isTeleport: # 瞬间移动中
            return
        if not pc._loc._map._isUsableItem:
            pc.sendPackets(S_ServerMessage(563)) # 在这里不能使用道具

        if pc._currentHp <= 0:
            return

        delay_id = 0
        clsType = item_inst._item._clsType
        if clsType == 0: # 材料道具
            delay_id = item_inst._item.get_delayid()
        if delay_id != 0:
            if pc.hasItemDelay(delay_id):
                return

        isDelayEffect = False
        if clsType == 0: # 材料道具
            delayEffect = item_inst._item.get_delayEffect()
            if delayEffect > 0:
                isDelayEffect = True
                lastUsed = item_inst._lastUsed
                if lastUsed:
                    if int((time.time() - lastUsed) / 1000) <= delayEffect:
                        pc.sendPackets(S_ServerMessage(78))
                        return

        logging.info("request item use (obj) = " + str(objid))
        if clsType == 0:
            handler = C_EtcItem(self, item_inst)
        elif clsType == 1:
            handler = C_WeaponItem(self, item_inst)
        elif clsType == 2:
            handler = C_ArmorItem(self, item_inst)
        else:
            return
        handler.handle()

        if isDelayEffect:
            item_inst._lastUsed = time.time()
            pc._inventory.updateItem(item_inst, PcInventory.COL_DELAY_EFFECT)
            pc._inventory.saveItem(item_inst, PcInventory.COL_DELAY_EFFECT)