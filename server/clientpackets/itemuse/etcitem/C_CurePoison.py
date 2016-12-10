# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_CurePoison(C_EtcItemBase):
    '''
    解毒药剂使用
    '''
    item_ids = [
        40017, # 解毒药水
        40507 # 安特之树枝
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        return