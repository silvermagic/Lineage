# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_PolyScale(C_EtcItemBase):
    '''
    变身卷轴使用
    '''
    item_ids = [
        41154,  # 暗之鳞
        41155,  # 火之鳞
        41156,  # 叛之鳞
        41157,  # 恨之鳞
        49220  # 妖魔密使变形卷轴
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        self._pc._inventory.removeItem(inst=item_inst, count=1)