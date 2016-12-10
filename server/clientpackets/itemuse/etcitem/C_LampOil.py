# -*- coding: utf-8 -*-

from server.serverpackets.S_ItemName import S_ItemName
from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_LampOil(C_EtcItemBase):
    '''
    灯油使用
    '''
    item_ids = [
        40003,   # 灯油
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        for light_inst in self._pc._inventory._item_insts:
            if light_inst._itemId == 40002:
                light_inst._remainingTime = item_inst._item.getLightFuel()
                self._pc.sendPackets(S_ItemName(light_inst))
                self._pc.sendPackets(S_ServerMessage(230))  # 向灯笼里添加灯油