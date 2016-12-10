# -*- coding: utf-8 -*-

from server.model.skill import SkillId
from server.serverpackets.S_PacketBox import S_PacketBox
from server.serverpackets.S_SystemMessage import S_SystemMessage
from server.serverpackets.S_ServerMessage import S_ServerMessage

class C_WeaponItem():
    def __init__(self, fd, item_inst):
        self._fd = fd
        self._pc = fd._client._activeChar
        self._item_inst = item_inst

    def handle(self):
        return self._handle(self._fd, self._item_inst)

    def _handle(self, fd, item_inst):
        pc = self._pc
        minlvl = item_inst._item._minLevel
        maxlvl = item_inst._item._maxLevel

        if minlvl != 0 and minlvl > pc.getLevel():
            self._pc.sendPackets.S_ServerMessage(318, str(minlvl))
        elif maxlvl != 0 and maxlvl < pc.getLevel():
            if maxlvl < 50:
                pc.sendPackets(S_PacketBox(S_PacketBox.MSG_LEVEL_OVER, value=maxlvl))
            else:
                pc.sendPackets(S_SystemMessage('等级' + str(maxlvl) + '以下才可以使用此道具.'))
        else:
            if pc.isCrown() and item_inst._item._useRoyal \
                or pc.isKnight() and item_inst._item._useKnight \
                or pc.isElf() and item_inst._item._useElf \
                or pc.isWizard() and item_inst._item._useMage \
                or pc.isDarkelf() and item_inst._item._useDarkelf \
                or pc.isDragonKnight() and item_inst._item._useDragonknight \
                or pc.isIllusionist() and item_inst._item._useIllusionist:
                self.UseWeapon(item_inst)
            else:
                pc.sendPackets(S_ServerMessage(264))

    def UseWeapon(self, weapon):
        pc = self._pc
        inventory = self._pc._inventory
        if not pc._weapon or pc._weapon != weapon:
            # weapon_type = weapon._item._type
            # polyid = pc._tempCharGfx
            # todo: 变身状态检测

            if weapon._item.isTwohandedWeapon() and inventory.getTypeEquipped(2, 7) >= 1:
                pc.sendPackets(S_ServerMessage(128))

        if pc._weapon:
            if pc._weapon._item._bless == 2: # 被诅咒
                pc.sendPackets(S_ServerMessage(150))

            if pc._weapon == weapon:
                inventory.setEquipped(pc._weapon, False, False, False)
            else:
                inventory.setEquipped(pc._weapon, False, False, True)
        else:
            inventory.setEquipped(weapon, True, False, False)

    def CancelAbsoluteBarrier(self, pc):
        if pc.hasSkillEffect(SkillId.ABSOLUTE_BARRIER):
            return

