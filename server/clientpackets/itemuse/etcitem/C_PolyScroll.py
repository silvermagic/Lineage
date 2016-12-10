# -*- coding: utf-8 -*-

from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_PolyScroll(C_EtcItemBase):
    '''
    变身卷轴使用
    '''
    item_ids = [
        40088,  # 变形卷轴
        40096,  # 象牙塔变身卷轴
        140088  # 变形卷轴
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        ret = False
        ret = self.UsePolyScroll(item_inst, fd.readS())
        if ret: # 消耗使用成功的道具
            self._pc._inventory.removeItem(inst=item_inst, count=1)
        else:
            self._pc.sendPackets(S_ServerMessage(181))

    def UsePolyScroll(self, item_inst, s):
        return True