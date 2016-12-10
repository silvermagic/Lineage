# -*- coding: utf-8 -*-

from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_GrindStone(C_EtcItemBase):
    '''
    变身卷轴使用
    '''
    item_ids = [
        40317  # 磨刀石
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        clsType =  item_inst._item._clsType
        durability = item_inst._durability
        if clsType != 0 and durability > 0:
            self._pc._inventory.recoveryDamage(item_inst)
            if durability == 0:
                self._pc.sendPackets(S_ServerMessage(464, item_inst.getLogName()))
            else:
                self._pc.sendPackets(S_ServerMessage(463, item_inst.getLogName()))
        else:
            return self.Banned()
        self._pc._inventory.removeItem(inst=item_inst, count=1)