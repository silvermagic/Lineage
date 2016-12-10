# -*- coding: utf-8 -*-

import random
from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_MagicRecoveryPotion(C_EtcItemBase):
    '''
    魔力回复药水使用
    '''
    item_ids = [
        40066, # 年糕
        41413, # 月饼
        40067, # 艾草年糕
        41414, # 福月饼
        40735, # 勇气货币
        40042, # 精神药水
        41404, # 库杰的灵药
        41412 # 金粽子
    ]

    # 药水效果(Fix, Random.Range)
    effects = [
        (7, 6), # 年糕
        (7, 6),  # 月饼
        (15, 16), # 艾草年糕
        (15, 16), # 福月饼
        (0, 60), # 勇气货币
        (0, 50), # 精神药水
        (80, 21), # 库杰的灵药
        (5, 16) # 金粽子
    ]

    effects_map = dict(zip(item_ids, effects))

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        item_id = item_inst._itemId
        if not C_MagicRecoveryPotion.effects_map.has_key(item_id):
            return

        fix, rng = C_MagicRecoveryPotion.effects_map[item_id]
        self._pc.sendPackets(S_ServerMessage(338, "$1084"))
        self._pc.setCurrentMp(self._pc._currentMp + (fix + random.randrange(rng)))
        self._pc._inventory.removeItem(inst=item_inst, count=1)