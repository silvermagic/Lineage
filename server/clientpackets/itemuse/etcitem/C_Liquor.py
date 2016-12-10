# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_Liquor(C_EtcItemBase):
    '''
    解毒药剂使用
    '''
    item_ids = [
        40858 # 酒
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        return