# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_BravePotion(C_EtcItemBase):
    '''
    二段加速药水使用
    '''
    item_ids = [
        40014,  # 勇敢药水
        140014, # 受祝福的勇敢药水
        41415,  # 强化勇气的药水
        49158,  # 生命之树果实
        40068,  # 精灵饼干
        140068, # 受祝福的精灵饼干
        40031,  # 恶魔之血
        40733   # # 名誉货币
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        item_id = item_inst._itemId

        if item_id in C_BravePotion.item_ids[:3] and not self._pc.isKnight() \
            or item_id in C_BravePotion.item_ids[3] and not (self._pc.isDragonKnight() or self._pc.isIllusionist()) \
            or item_id in C_BravePotion.item_ids[4:6] and not self._pc.isElf() \
            or item_id in C_BravePotion.item_ids[6] and not self._pc.isCrown():
            return self.Banned()

        self.UsePotion(item_inst)
        self._pc._inventory.removeItem(inst=item_inst, count=1)

    def UsePotion(self, item_inst):
        return