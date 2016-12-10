# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_BreatheUnderwater(C_EtcItemBase):
    '''
    水下呼吸药剂使用
    '''
    item_ids = [
        40032, # 伊娃的祝福
        40041, # 人鱼之鳞
        41344 # 水中的水
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        self.UsePotion(item_inst)
        self._pc._inventory.removeItem(inst=item_inst, count=1)

    def UsePotion(self, item_inst):
        return