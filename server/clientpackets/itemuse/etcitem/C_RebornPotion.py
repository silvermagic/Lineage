# -*- coding: utf-8 -*-

from Config import Config
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_OwnCharStatus import S_OwnCharStatus
from C_EtcItemBase import C_EtcItemBase

class RebornPotion(C_EtcItemBase):
    '''
    使用
    '''
    item_ids = [
        240105 # 重生药水
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        pc = self._pc
        if pc._level <= 10:
            pc.sendPackets(S_ServerMessage(79))
            return
        pc.sendPackets(S_SkillSound(pc._id, 6505))
        pc.broadcastPacket(S_SkillSound(pc._id, 6505))
        pc._inventory.takeoffEquip(945)
        pc.setExp(10000)
        pc.resetLevel()
        pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) - 12))
        pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) - 12))
        pc.resetBaseAc()
        pc.resetBaseMr()
        pc.resetBaseHitup()
        pc.resetBaseDmgup()
        pc.sendPackets(S_OwnCharStatus(pc))
        pc.sendPackets(S_ServerMessage(822))
        pc._inventory.removeItem(inst=item_inst, count=1)