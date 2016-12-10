# -*- coding: utf-8 -*-

import numpy
from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_BloodRecoveryPotion(C_EtcItemBase):
    '''
    血量回复药水使用
    '''
    item_ids = [
        40029, # 象牙塔治愈药水
        40010, # 治愈药水
        40019, # 浓缩体力恢复剂
        40022, # 古代体力恢复剂
        40011, # 强力治愈药水
        40020, # 浓缩强力体力恢复剂
        40023, # 古代强力体力恢复剂
        40012, # 终极治愈药水
        40021, # 浓缩终极体力恢复剂
        40024, # 古代终极体力恢复剂
        40506, # 安特的水果
        40026, # 香蕉汁
        40027, # 橘子汁
        40028, # 苹果汁
        40058, # 烟熏的面包屑
        40071, # 烤焦的面包屑
        40734, # 信赖货币
        140010, # 受祝福的治愈药水
        240010, # 被诅咒的治愈药水
        140011, # 受祝福的强力治愈药水
        140012, # 受祝福的终极治愈药水
        140506, # 受祝福的安特的水果
        40043, # 兔子的肝
        41403, # 库杰的粮食
        41417, # 草莓刨冰
        41418, # 柠檬刨冰
        41419, # 芒果刨冰
        41420, # 甜瓜刨冰
        41421, # 红豆刨冰
        41337 # 受祝福的五谷面包
    ]

    # 药水效果(healHp, gfxid)
    effects = [
        (15, 189), # 象牙塔治愈药水
        (15, 189), # 治愈药水
        (15, 189), # 浓缩体力恢复剂
        (20, 189), # 古代体力恢复剂
        (45, 194), # 强力治愈药水
        (45, 194), # 浓缩强力体力恢复剂
        (30, 194), # 古代强力体力恢复剂
        (75, 197), # 终极治愈药水
        (75, 197), # 浓缩终极体力恢复剂
        (55, 197), # 古代终极体力恢复剂
        (70, 197), # 安特的水果
        (25, 189), # 香蕉汁
        (25, 189), # 橘子汁
        (25, 189), # 苹果汁
        (30, 189), # 烟熏的面包屑
        (70, 197), # 烤焦的面包屑
        (50, 189), # 信赖货币
        (25, 189), # 受祝福的治愈药水
        (10, 189), # 被诅咒的治愈药水
        (55, 194), # 受祝福的强力治愈药水
        (85, 197), # 受祝福的终极治愈药水
        (80, 197), # 受祝福的安特的水果
        (600, 189), # 兔子的肝
        (300, 189), # 库杰的粮食
        (90, 197), # 草莓刨冰
        (90, 197), # 柠檬刨冰
        (90, 197), # 芒果刨冰
        (90, 197), # 甜瓜刨冰
        (90, 197), # 红豆刨冰
        (85, 197) # 受祝福的五谷面包
    ]

    effects_map = dict(zip(item_ids, effects))

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        item_id = item_inst._itemId
        if not C_BloodRecoveryPotion.effects_map.has_key(item_id):
            return
        healHp, gfxid = C_BloodRecoveryPotion.effects_map[item_id]
        self.UsePotion(healHp, gfxid)
        self._pc._inventory.removeItem(inst=item_inst, count=1)

    def UsePotion(self, healHp, gfxid):
        # todo: pc状态判断
        self._pc.sendPackets(S_SkillSound(self._pc._id, gfxid))
        self._pc.broadcastPacket(S_SkillSound(self._pc._id, gfxid))
        self._pc.sendPackets(S_ServerMessage(77))
        healHp *= (numpy.random.normal() / 5.0) + 1.0
        self._pc.setCurrentHp(self._pc._currentHp + int(healHp))