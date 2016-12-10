# -*- coding: utf-8 -*-

import random
from Config import Config
from server.model.PcInventory import PcInventory
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_SPMR import S_SPMR
from server.serverpackets.S_OwnCharStatus import S_OwnCharStatus
from C_EtcItemBase import C_EtcItemBase

class C_EnchantScroll(C_EtcItemBase):
    '''
    强化卷轴使用
    '''
    item_ids = [
        40087,   # 对武器施法的卷轴
        140087,  # 受祝福的对武器施法的卷轴
        240087,  # 受诅咒的对武器施法的卷轴
        40660,   # 试炼卷轴
        40077,   # 古代人的炼金术卷轴
        40128,   # 对武器施法的幻象卷轴
        40130,   # 金侃的卷轴
        140130,  # 受祝福的金侃的卷轴
        40074,   # 对盔甲施法的卷轴
        140074,  # 受祝福的对盔甲施法的卷轴
        240074,  # 受诅咒的对盔甲施法的卷轴
        40078,   # 古代人的咒术卷轴
        40127,   # 对盔甲施法的幻象卷轴
        40129,   # 奇安的卷轴
        140129   # 受祝福的奇安的卷轴
    ]

    quest_item_ids = [
        246, # 试炼之剑
        247, # 试炼之剑
        248, # 试炼之剑
        249  # 试炼之剑
    ]

    fantasy_item_ids = [
        36,    # 幻象之剑
        183,   # 幻象之弓
        250,   # 幻象短剑
        251,   # 幻象巨剑
        252,   # 幻象之矛
        253,   # 幻象之弓
        254,   # 幻象双刀
        255,   # 幻象魔杖
        20161, # 幻象盔甲
        21035, # 幻象 头盔
        21036, # 幻象 上衣
        21037, # 幻象 盾牌
        21038  # 幻象 长靴
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        ret = False
        # 被强化的道具对象
        enchant_item_inst = self._pc._inventory.getItem(fd.readD())
        if item_inst._itemId in C_EnchantScroll.item_ids[:8]:
            ret = self.EnchantWeapon(item_inst, enchant_item_inst)
        elif item_inst._itemId in C_EnchantScroll.item_ids[8:]:
            ret = self.EnchantArmor(item_inst, enchant_item_inst)
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

        # 特殊武器判断
        item_id = item_inst._itemId
        weapon_id = enchant_item_inst._itemId
        if weapon_id in C_EnchantScroll.quest_item_ids and item_id != 40660:
            return self.Banned()
        if weapon_id in C_EnchantScroll.fantasy_item_ids and item_id != 40128:
            return self.Banned()

        enchant_level = enchant_item_inst._enchantLevel
        if item_id == 240087:
            if enchant_level < -6:
                return self.FailureEnchant(enchant_item_inst)
            else:
                return self.SuccessEnchant(enchant_item_inst, -1)
        elif enchant_level < safe_enchant:
            return self.SuccessEnchant(enchant_item_inst, self.RandomELevel(enchant_item_inst, item_id))
        else:
            rnd = random.randrange(100) + 1
            if enchant_level >= 9:
                enchant_chance_weapon = int((100 + 3 * Config.getint('rates', 'EnchantChanceWeapon')) / 6)
            else:
                enchant_chance_weapon = int((100 + 3 * Config.getint('rates', 'EnchantChanceWeapon')) / 3)
            if rnd < enchant_chance_weapon:
                return self.SuccessEnchant(enchant_item_inst, self.RandomELevel(enchant_item_inst, item_id))
            elif enchant_level >= 9 and rnd < (enchant_chance_weapon * 2):  # 武器发出强烈的银色光芒但是没有任何事情发生
                self._pc.sendPackets(S_ServerMessage(160, enchant_item_inst.getLogName(), "$245", "$248"))
            else:
                return self.FailureEnchant(enchant_item_inst)

        return True

    def EnchantArmor(self, item_inst, enchant_item_inst):
        '''
        强化装备
        :param item_inst:使用的道具(ItemInstance)
        :param enchant_item_inst:强化的装备(ItemInstance)
        :return:使用道具是否成功(True/False)
        '''
        # 被强化的道具不是武器或者不存在
        if not enchant_item_inst or enchant_item_inst._item._clsType != 2:
            return self.Banned()
        safe_enchant = enchant_item_inst._item._safeEnchant
        if safe_enchant < 0:  # 不可强化
            return self.Banned()
        if enchant_item_inst._bless >= 128:  # 封印道具不可强化
            return self.Banned()

        # 特殊武器判断
        item_id = item_inst._itemId
        armor_id = enchant_item_inst._itemId
        if armor_id in C_EnchantScroll.fantasy_item_ids and item_id != 40127:
            return self.Banned()

        enchant_level = enchant_item_inst._enchantLevel
        if item_id == 240074:
            if enchant_level < -6:
                return self.FailureEnchant(enchant_item_inst)
            else:
                return self.SuccessEnchant(enchant_item_inst, -1)
        elif enchant_level < safe_enchant:
            return self.SuccessEnchant(enchant_item_inst, self.RandomELevel(enchant_item_inst, item_id))
        else:
            rnd = random.randrange(100) + 1
            if safe_enchant == 0:
                enchant_level_tmp = enchant_level + 2
            else:
                enchant_level_tmp = enchant_level

            if enchant_level >= 9:
                enchant_chance_armor = int(
                    (100 + enchant_level_tmp * Config.getint('rates', 'EnchantChanceArmor')) / (enchant_level_tmp * 2))
            else:
                enchant_chance_armor = int(
                    (100 + enchant_level_tmp * Config.getint('rates', 'EnchantChanceArmor')) / enchant_level_tmp)

            if rnd < enchant_chance_armor:
                return self.SuccessEnchant(enchant_item_inst, self.RandomELevel(enchant_item_inst, item_id))
            elif enchant_level >= 9 and rnd < (enchant_chance_armor * 2):
                self._pc.sendPackets(S_ServerMessage(160, enchant_item_inst.getLogName(), "$252", "$248"))
            else:
                return self.FailureEnchant(enchant_item_inst)

        return True

    def SuccessEnchant(self, enchant_item_inst, level):
        '''
        返回装备/武器强化成功消息到客户端,并更新道具信息
        :param enchant_item_inst:强化成功的装备/武器(ItemInstance)
        :param level:强化成功的等级(int)
        :return:True
        '''

        s =''
        sa = ''
        sb = ''
        pm = ''
        item_name = enchant_item_inst._item._name
        enchantLevel = enchant_item_inst._enchantLevel
        if enchantLevel > 0:
            pm = '+'
        if not enchant_item_inst._isIdentified or enchantLevel == 0:
            s = item_name
        else:
            s = pm + str(enchantLevel) + ' ' + item_name

        clsType = enchant_item_inst._item._clsType
        if level == -1:
            sa = '$246'
            sb = '$247'
        elif level == 1:
            if clsType == 1:
                sa = '$245'
            else:
                sa = '$252'
            sb = '$247'
        elif level == 2 or level == 3:
            if clsType == 1:
                sa = '$245'
            else:
                sa = '$252'
            sb = '$248'

        self._pc.sendPackets(S_ServerMessage(161, s, sa, sb))
        enchant_item_inst._enchantLevel += level
        self._pc._inventory.updateItem(enchant_item_inst, PcInventory.COL_ENCHANTLVL)
        if enchant_item_inst._enchantLevel > enchant_item_inst._item._safeEnchant: # 过了安定值也要存下数据库
            self._pc._inventory.saveItem(enchant_item_inst, PcInventory.COL_ENCHANTLVL)
        # todo: 日志记录
        if clsType == 2:
            if enchant_item_inst._isEquipped:
                self._pc.addAc(-1 * level)
                armor_id = enchant_item_inst._item._itemId
                if armor_id in (20011,  # 抗魔法头盔
                                20110,  # 抗魔法链甲
                                21108,  # 霸王头盔(力智)
                                120011):  # 受祝福的抗魔法头盔
                    self._pc.addMr(level)
                    self._pc.sendPackets(S_SPMR(self._pc))
                elif armor_id in (20056,  # 抗魔法斗篷
                                  120056,  # 受祝福的抗魔法斗篷
                                  220056):  # 受诅咒的抗魔法斗篷
                    self._pc.addMr(level * 2)
                    self._pc.sendPackets(S_SPMR(self._pc))
            self._pc.sendPackets(S_OwnCharStatus(self._pc))
        return True

    def FailureEnchant(self, enchant_item_inst):
        '''
        返回装备/武器强化失败消息到客户端,并更新道具信息
        :param enchant_item_inst:强化失败的装备/武器(ItemInstance)
        :return:False
        '''
        s = ''
        sa = ''
        pm = ''
        item_name = enchant_item_inst._item._name
        enchantLevel = enchant_item_inst._enchantLevel
        if not enchant_item_inst._isIdentified or enchantLevel == 0:
            s = item_name
        else:
            if enchantLevel > 0:
                pm = '+'
            s = pm + str(enchantLevel) + ' ' + item_name
        if enchant_item_inst._item._clsType == 1:
            sa = '$245'
        else:
            sa = '$252'
        self._pc.sendPackets(S_ServerMessage(164, s, sa))
        self._pc._inventory.removeItem(inst=enchant_item_inst)
        return False

    def RandomELevel(self, enchant_item_inst, item_id):
        '''
        返回强化等级
        :param enchant_item_inst:强化的装备/武器(ItemInstance)
        :param item_id:强化使用的道具模板ID(int)
        :return:等级(int)
        '''
        enchantLevel = enchant_item_inst._enchantLevel
        if item_id in (140074, 140087, 140129, 140130): # 受祝福的强化卷轴强化等级1~3
            if enchantLevel <= 2:
                j = random.randrange(100) + 1
                if j < 32:
                    return 1
                elif j >= 33 and j <= 76:
                    return 2
                elif j >= 77 and j <= 100:
                    return 3
            elif enchantLevel >= 3 and enchantLevel <= 5:
                j = random.randrange(100) + 1
                if j < 50:
                    return 2
                else:
                    return 1
            else:
                return 1

        return 1