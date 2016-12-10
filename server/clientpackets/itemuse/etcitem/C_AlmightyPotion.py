# -*- coding: utf-8 -*-

from Config import Config
from server.serverpackets.S_SystemMessage import S_SystemMessage
from C_EtcItemBase import C_EtcItemBase

class C_AlmightyPotion(C_EtcItemBase):
    '''
    万能药水使用
    '''
    item_ids = [
        40033, # 万能药(力量)
        40034, # 万能药(体质)
        40035, # 万能药(敏捷)
        40036, # 万能药(智力)
        40037, # 万能药(精神)
        40038, # 万能药(魅力)
    ]

    def __init__(self, fd, item_inst):
        C_EtcItemBase.__init__(self, fd, item_inst)

    def _handle(self, fd, item_inst):
        pc = self._pc
        item_id = item_inst._itemId
        if item_id == 40033:  # 万能药(力量)
            if pc._baseStr < Config.getint('charsettings', 'BONUS_STATS3') \
                    and pc._elixirStats < Config.getint('charsettings', 'BONUS_STATS2'):
                pc.addBaseStr(1)
                pc._elixirStats += 1
                pc._inventory.removeItem(inst=item_inst, count=1)
                pc.sendPackets(S_OwnCharStatus2(pc))
                pc.save()
            else:
                pc.sendPackets(S_SystemMessage('力量已经达到上限请选择其他能力值'))
        elif item_id == 40034:  # 万能药(体质)
            if pc._baseCon < Config.getint('charsettings', 'BONUS_STATS3') \
                    and pc._elixirStats < Config.getint('charsettings', 'BONUS_STATS2'):
                pc.addBaseCon(1)
                pc._elixirStats += 1
                pc._inventory.removeItem(inst=item_inst, count=1)
                pc.sendPackets(S_OwnCharStatus2(pc))
                pc.save()
            else:
                pc.sendPackets(S_SystemMessage('体质已经达到上限请选择其他能力值'))
        elif item_id == 40035:  # 万能药(敏捷)
            if pc._baseDex < Config.getint('charsettings', 'BONUS_STATS3') \
                    and pc._elixirStats < Config.getint('charsettings', 'BONUS_STATS2'):
                pc.addBaseDex(1)
                pc.resetBaseAc()
                pc._elixirStats += 1
                pc._inventory.removeItem(inst=item_inst, count=1)
                pc.sendPackets(S_OwnCharStatus2(pc))
                pc.save()
            else:
                pc.sendPackets(S_SystemMessage('敏捷已经达到上限请选择其他能力值'))
        elif item_id == 40036:  # 万能药(智力)
            if pc._baseInt < Config.getint('charsettings', 'BONUS_STATS3') \
                    and pc._elixirStats < Config.getint('charsettings', 'BONUS_STATS2'):
                pc.addBaseInt(1)
                pc._elixirStats += 1
                pc._inventory.removeItem(inst=item_inst, count=1)
                pc.sendPackets(S_OwnCharStatus2(pc))
                pc.save()
            else:
                pc.sendPackets(S_SystemMessage('智力已经达到上限请选择其他能力值'))
        elif item_id == 40037:  # 万能药(精神)
            if pc._baseWis < Config.getint('charsettings', 'BONUS_STATS3') \
                    and pc._elixirStats < Config.getint('charsettings', 'BONUS_STATS2'):
                pc.addBaseWis(1)
                pc._elixirStats += 1
                pc._inventory.removeItem(inst=item_inst, count=1)
                pc.sendPackets(S_OwnCharStatus2(pc))
                pc.save()
            else:
                pc.sendPackets(S_SystemMessage('精神已经达到上限请选择其他能力值'))
        elif item_id == 40038:  # 万能药(魅力)
            if pc._baseCha < Config.getint('charsettings', 'BONUS_STATS3') \
                    and pc._elixirStats < Config.getint('charsettings', 'BONUS_STATS2'):
                pc.addBaseCha(1)
                pc._elixirStats += 1
                pc._inventory.removeItem(inst=item_inst, count=1)
                pc.sendPackets(S_OwnCharStatus2(pc))
                pc.save()
            else:
                pc.sendPackets(S_SystemMessage('魅力已经达到上限请选择其他能力值'))