# -*- coding: utf-8 -*-

from server.serverpackets.S_PacketBox import S_PacketBox
from server.serverpackets.S_SystemMessage import S_SystemMessage
from server.serverpackets.S_ServerMessage import S_ServerMessage

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

    def UseArmor(self, use_weapon):
        return
