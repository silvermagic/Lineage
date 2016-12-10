# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_BlindnessPotion(C_EtcItemBase):
    '''
    黑色药水使用
    '''
    item_ids = [
        40025 # 失明药水
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        return