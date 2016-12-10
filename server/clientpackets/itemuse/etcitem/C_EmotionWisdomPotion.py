# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_EmotionWisdomPotion(C_EtcItemBase):
    '''
    慎重药水使用
    '''
    item_ids = [
        40016,  # 慎重药水
        140016 # 受祝福的慎重药水
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        if not self._pc.isWizard():
            return self.Banned()
        self.UsePotion(item_inst)
        self._pc._inventory.removeItem(inst=item_inst, count=1)

    def UsePotion(self, item_inst):
        return