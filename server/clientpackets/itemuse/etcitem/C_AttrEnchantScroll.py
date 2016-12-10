# -*- coding: utf-8 -*-

import random
from Config import Config
from server.model.PcInventory import PcInventory
from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_AttrEnchantScroll(C_EtcItemBase):
    '''
    属性强化卷轴使用
    '''
    item_ids = [
        41429,   # 风之武器强化卷轴
        41430,   # 地之武器强化卷轴
        41431,   # 水之武器强化卷轴
        41432,   # 火之武器强化卷轴
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        ret = False
        # 被强化的道具对象
        enchant_item_inst = self._pc._inventory.getItem(fd.readD())
        ret = self.EnchantWeapon(item_inst, enchant_item_inst)
        if ret: # 消耗使用成功的道具
            self._pc._inventory.removeItem(inst=item_inst, count=1)

    def EnchantWeapon(self, item_inst, enchant_item_inst):
        '''
        强化武器
        :param item_inst:使用的道具(ItemInstance)
        :param enchant_item_inst:强化的武器(ItemInstance)
        :return:使用道具是否成功(True/False)
        '''
        # 被强化的道具不是武器或者不存在
        if not enchant_item_inst or enchant_item_inst._item._clsType != 1:
            return self.Banned()
        safe_enchant = enchant_item_inst._item._safeEnchant
        if safe_enchant < 0:  # 不可强化
            return self.Banned()
        if enchant_item_inst._bless >= 128:  # 封印道具不可强化
            return self.Banned()

        oldAttrEnchantKind = enchant_item_inst._attrEnchantKind
        oldAttrEnchantLevel = enchant_item_inst._attrEnchantLevel
        isSameAttr = False
        item_id = item_inst._itemId
        if item_id == 41429 and oldAttrEnchantKind == 8 \
                or item_id == 41430 and oldAttrEnchantKind == 1 \
                or item_id == 41431 and oldAttrEnchantKind == 4 \
                or item_id == 41432 and oldAttrEnchantKind == 2:
            isSameAttr = True
        if isSameAttr and oldAttrEnchantLevel >= 3:  # 已经达到强化上限了
            self._pc.sendPackets(S_ServerMessage(1453))
            return False

        rnd = random.randrange(100) + 1
        if Config.getint('rates', 'AttrEnchantChance') >= rnd:
            self._pc.sendPackets(S_ServerMessage(161, enchant_item_inst.getLogName(), "$245", "$247"))
            newAttrEnchantKind = 0
            if isSameAttr:
                newAttrEnchantLevel = oldAttrEnchantLevel + 1
            else:
                newAttrEnchantLevel = 1

            if item_id == 41429:
                newAttrEnchantKind = 8
            elif item_id == 41430:
                newAttrEnchantKind = 1
            elif item_id == 41431:
                newAttrEnchantKind = 4
            elif item_id == 41432:
                newAttrEnchantKind = 2

            enchant_item_inst._attrEnchantKind = newAttrEnchantKind
            self._pc._inventory.updateItem(enchant_item_inst, PcInventory.COL_ATTR_ENCHANT_KIND)
            self._pc._inventory.saveItem(enchant_item_inst, PcInventory.COL_ATTR_ENCHANT_KIND)
            enchant_item_inst._attrEnchantLevel = newAttrEnchantLevel
            self._pc._inventory.updateItem(enchant_item_inst, PcInventory.COL_ATTR_ENCHANT_LEVEL)
            self._pc._inventory.saveItem(enchant_item_inst, PcInventory.COL_ATTR_ENCHANT_LEVEL)
        else:
            return self.Banned()

        return True