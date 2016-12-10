# -*- coding: utf-8 -*-

import random
from server.serverpackets.S_ItemStatus import S_ItemStatus
from server.storage.CharactersItemStorage import CharactersItemStorage
from C_EnchantScroll import C_EnchantScroll

class C_OrnamentsEnchantScroll(C_EnchantScroll):
    '''
    饰品强化卷轴使用
    '''
    item_ids = [
        49148,  # 饰品强化卷轴
    ]

    def __init__(self, fd, item_inst):
        C_EnchantScroll.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        ret = False
        # 被强化的道具对象
        enchant_item_inst = self._pc._inventory.getItem(fd.readD())
        ret = self.enchantArmor(item_inst, enchant_item_inst)
        if ret: # 消耗使用成功的道具
            self._pc._inventory.removeItem(inst=item_inst, count=1)

    def enchantArmor(self, item_inst, enchant_item_inst):
        '''
        强化装备
        :param item_inst:使用的道具(ItemInstance)
        :param enchant_item_inst:强化的装备(ItemInstance)
        :return:使用道具是否成功(True/False)
        '''
        # 被强化的道具不是武器或者不存在
        if not enchant_item_inst or enchant_item_inst._item._clsType != 2:
            return self.Banned()

        type = enchant_item_inst._item._type
        if type not in (8,  # 项链
                        9,  # 戒子
                        10,  # 腰带
                        12):  # 耳环
            return self.Banned()

        chance = random.randrange(100) + 1
        enchant_level = enchant_item_inst._enchantLevel
        if enchant_level == -1:
            enchant_item_inst._enchantLevel = 0

        if chance < 15:
            enchant_item_inst._addHp += 2
            if enchant_level == 5:
                enchant_item_inst._Mpr += 1
            if enchant_item_inst._isEquipped:
                self._pc.addMaxHp(2)
        elif chance > 15 and chance < 25:
            enchant_item_inst._addMp += 1
            if enchant_level == 5:
                enchant_item_inst._addsp += 1
            if enchant_item_inst._isEquipped:
                self._pc.addMaxMp(1)
        elif chance > 25 and chance < 35:
            enchant_item_inst._FireMr += 1
            enchant_item_inst._WaterMr += 1
            enchant_item_inst._EarthMr += 1
            enchant_item_inst._WindMr += 1
            enchant_item_inst._Mpr += 1
            enchant_item_inst._Hpr += 1
            if enchant_item_inst._isEquipped:
                self._pc.addFire(1)
                self._pc.addWater(1)
                self._pc.addEarth(1)
                self._pc.addWind(1)
        else:
            return self.FailureEnchant(enchant_item_inst)

        self.SuccessEnchant(enchant_item_inst, 1)
        self._pc.sendPackets(S_ItemStatus(enchant_item_inst))
        storage = CharactersItemStorage().create()
        storage.updateFireMr(enchant_item_inst)
        storage.updateWaterMr(enchant_item_inst)
        storage.updateEarthMr(enchant_item_inst)
        storage.updateWindMr(enchant_item_inst)
        storage.updateaddSp(enchant_item_inst)
        storage.updateaddHp(enchant_item_inst)
        storage.updateaddMp(enchant_item_inst)
        storage.updateHpr(enchant_item_inst)
        storage.updateMpr(enchant_item_inst)
        return True