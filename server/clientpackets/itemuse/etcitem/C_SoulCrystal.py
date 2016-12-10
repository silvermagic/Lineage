# -*- coding: utf-8 -*-

from server.serverpackets.S_ItemName import S_ItemName
from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_SoulCrystal(C_EtcItemBase):
    '''
    灯油使用
    '''
    item_ids = [
        40576, # 灵魂水晶(精灵)
        40577, # 灵魂水晶(法师)
        40578 # 灵魂水晶(骑士)
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        item_id = item_inst._itemId
        if item_id == 40576 and not self._pc.isElf() \
                or item_id == 40577 and not self._pc.isWizard() \
                or item_id == 40578 and not self._pc.isKnight():
            self._pc.sendPackets(S_ServerMessage(264))