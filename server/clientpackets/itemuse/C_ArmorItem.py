# -*- coding: utf-8 -*-

from server.model.skill import SkillId
from server.serverpackets.S_PacketBox import S_PacketBox
from server.serverpackets.S_SystemMessage import S_SystemMessage
from server.serverpackets.S_ServerMessage import S_ServerMessage
from server.serverpackets.S_OwnCharStatus import S_OwnCharStatus
from server.serverpackets.S_SPMR import S_SPMR
from server.serverpackets.S_OwnCharAttrDef import S_OwnCharAttrDef

class C_ArmorItem():
    def __init__(self, fd, item_inst):
        self._fd = fd
        self._pc = fd._client._activeChar
        self._item_inst = item_inst

    def handle(self):
        return self._handle(self._fd, self._item_inst)

    def _handle(self, fd, item_inst):
        minlvl = item_inst._item._minLevel
        maxlvl = item_inst._item._maxLevel

        if minlvl != 0 and minlvl > self._pc.getLevel():
            self._pc.sendPackets.S_ServerMessage(318, str(minlvl))
        elif maxlvl != 0 and maxlvl < self._pc.getLevel():
            if maxlvl < 50:
                self._pc.sendPackets(S_PacketBox(S_PacketBox.MSG_LEVEL_OVER, value=maxlvl))
            else:
                self._pc.sendPackets(S_SystemMessage('等级' + str(maxlvl) + '以下才可以使用此道具.'))
        else:
            if self._pc.isCrown() and item_inst._item._useRoyal \
                or self._pc.isKnight() and item_inst._item._useKnight \
                or self._pc.isElf() and item_inst._item._useElf \
                or self._pc.isWizard() and item_inst._item._useMage \
                or self._pc.isDarkelf() and item_inst._item._useDarkelf \
                or self._pc.isDragonKnight() and item_inst._item._useDragonknight \
                or self._pc.isIllusionist() and item_inst._item._useIllusionist:
                self.UseArmor(item_inst)
            else:
                self._pc.sendPackets(S_ServerMessage(264))

    def UseArmor(self, armor):
        '''
        处理来自客户端的装备使用动作,更新用户当前使用的装备信息,并返回更新后的状态到客户端
        :param armor:被使用的装备道具实例(ItemInstance)
        :return:None
        '''

        item = armor._item
        type = armor._item._type
        inventory = self._pc._inventory
        pc = self._pc

        # 检测是否已经装备过同类道具
        if type == 9: # 戒子可以带两个
            equipe_space = inventory.getTypeEquipped(2, 9) <= 1
        else:
            equipe_space = inventory.getTypeEquipped(2, type) <= 0

        if equipe_space and not armor._isEquipped: # 没有装备过同类道具,并且道具当前是未使用状态
            polyid = pc._tempCharGfx
            # todo: 变身系统
            import logging
            logging.info('take on:' + str(armor.__dict__))
            if type == 13 and inventory.getTypeEquipped(2, 7) >= 1 \
                    or type == 7 and inventory.getTypeEquipped(2, 13) >= 1: # 准备装备臂甲但是已经装备了盾牌/准备装备盾牌但是已经装备了臂甲
                return  pc.sendPackets(S_ServerMessage(124))
            elif type == 7 and pc._weapon: # 准备装备盾牌并且已经装备武器
                if pc._weapon._item.isTwohandedWeapon(): # 当前装备的武器是双手武器
                    return pc.sendPackets(S_ServerMessage(129))
            elif type == 3 and inventory.getTypeEquipped(2, 4) >= 1: # 准备装备内衣但是已经装备了斗篷
                return pc.sendPackets(S_ServerMessage(126, "$224", "$225"))
            elif type == 3 and inventory.getTypeEquipped(2, 2) >= 1: # 准备装备内衣但是已经装备了盔甲
                return pc.sendPackets(S_ServerMessage(126, "$224", "$226"))
            elif type == 2 and inventory.getTypeEquipped(2, 4) >= 1: # 准备装备盔甲但是已经装备了斗篷
                return pc.sendPackets(S_ServerMessage(126, "$226", "$225"))
            else: # 装备上道具
                self.CancelAbsoluteBarrier(pc)
                inventory.setEquipped(armor, True)
        elif armor._isEquipped: # 已经装备过同类道具,并且道具当前是已使用状态,动作就是脱下当前装备
            if item._bless == 2: # 道具被诅咒了
                return pc.sendPackets(S_ServerMessage(150))
            elif type == 3 and inventory.getTypeEquipped(2, 2) >= 1: # 准备脱下内衣但是已经装备了盔甲
                return pc.sendPackets(S_ServerMessage(150))
            elif (type == 2 or type == 3) and inventory.getTypeEquipped(2, 4) >= 1: # 准备脱下内衣或者盔甲但是已经装备了斗篷
                return pc.sendPackets(S_ServerMessage(127))
            else:
                if type == 7 and pc.hasSkillEffect(SkillId.SOLID_CARRIAGE): # 准备脱下盾牌但是存在骑士的坚固防护魔法
                    pc.removeSkillEffect(SkillId.SOLID_CARRIAGE)
                inventory.setEquipped(armor, False)
        else: # 已经装备了同类道具,并且道具当前是未使用状态,不能和武器一样直接替换,需要先脱下当前使用的装备,然后再使用其他装备
            pc.sendPackets(S_ServerMessage(124))

        pc.setCurrentMp(pc._currentMp)
        pc.sendPackets(S_OwnCharAttrDef(pc))
        pc.sendPackets(S_OwnCharStatus(pc))
        pc.sendPackets(S_SPMR(pc))

    def CancelAbsoluteBarrier(self, pc):
        if pc.hasSkillEffect(SkillId.ABSOLUTE_BARRIER):
            return
