# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_PolyPotion(C_EtcItemBase):
    '''
    变身卷轴使用
    '''
    item_ids = [
        41143,  # 海贼骷髅首领变身药水
        41144,  # 海贼骷髅士兵变身药水
        41145,  # 海贼骷髅刀手变身药水
        49149,  # 夏纳的变形卷轴(等级：30)
        49150,  # 夏纳的变形卷轴(等级：40)
        49151,  # 夏纳的变形卷轴(等级：52)
        49152,  # 夏纳的变形卷轴(等级：55)
        49153,  # 夏纳的变形卷轴(等级：60)
        49154,  # 纳的变形卷轴(等级：65)
        49155  # 夏纳的变形卷轴(等级：70)
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        self._pc._inventory.removeItem(inst=item_inst, count=1)

    def UsePolyScroll(self, item_inst, s):
        return True