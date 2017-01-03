# -*- coding: utf-8 -*-

from Config import Config
from server.serverpackets.S_OwnCharStatus import S_OwnCharStatus
from server.serverpackets.S_ServerMessage import S_ServerMessage
from C_EtcItemBase import C_EtcItemBase

class C_ReincarnatePotion(C_EtcItemBase):
    '''
    转生药水使用
    '''
    item_ids = [
        43000,   # 转生药水
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        pc = self._pc
        pc._inventory.takeoffEquip(945)
        if pc.getLevel() == 99:
            pc.setExp(1)
            pc.resetLevel()
            revival_potion = Config.getint('charsettings', 'Revival_Potion')
            if revival_potion == 1:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.9))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.9))
            elif revival_potion == 2:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.8))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.8))
            elif revival_potion == 3:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.7))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.7))
            elif revival_potion == 4:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.6))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.6))
            elif revival_potion == 5:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.5))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.5))
            elif revival_potion == 6:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.4))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.4))
            elif revival_potion == 7:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.3))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.3))
            elif revival_potion == 8:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.2))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.2))
            elif revival_potion == 9:
                pc.addBaseMaxHp(-1 * int(float(pc._baseMaxHp) * 0.1))
                pc.addBaseMaxMp(-1 * int(float(pc._baseMaxMp) * 0.1))

            pc.resetBaseAc()
            pc.resetBaseMr()
            pc.resetBaseHitup()
            pc.resetBaseDmgup()
            pc._bonusStats = 0
            pc.sendPackets(S_SkillSound(pc._id, 3393))
            pc.broadcastPacket(S_SkillSound(pc._id, 3393))
            pc.sendPackets(S_OwnCharStatus(pc))
            pc._inventory.removeItem(inst=item_inst, count=1)
            pc.sendPackets(S_ServerMessage(822))
            pc.save()

