# -*- coding: utf-8 -*-

from C_EtcItemBase import C_EtcItemBase

class C_HastenPotion(C_EtcItemBase):
    '''
    加速药水使用
    '''
    item_ids = [
        40013,  # 受祝福的自我加速药水
        140013, # 自我加速药水
        40018,  # 强化自我加速药水
        40030,  # 象牙塔加速药水
        40039,  # 红酒
        40040,  # 威士忌
        41261,  # 饭团
        41262,  # 鸡肉串烧
        41268,  # 小比萨
        41269,  # 烤玉米
        41271,  # 爆米花
        41272,  # 甜不辣
        41273,  # 松饼
        41338,  # 受祝福的葡萄酒
        41342,  # 梅杜莎之血
        140018  # 强化自我加速药水
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        self.UsePotion(item_inst)
        self._pc._inventory.removeItem(inst=item_inst, count=1)

    def UsePotion(self, item_inst):
        return