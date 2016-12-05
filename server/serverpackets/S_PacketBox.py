# -*- coding: utf-8 -*-

import ctypes
from datetime import datetime
from server.Account import Account
from server.codes import Opcodes
from server.model.World import World
from server.utils.TimeUtil import TimeUtil
from ServerBasePacket import ServerBasePacket

class S_PacketBox(ServerBasePacket):
    MSG_WAR_BEGIN = 0
    MSG_WAR_END = 1
    MSG_WAR_GOING = 2
    MSG_WAR_INITIATIVE = 3
    MSG_WAR_OCCUPY = 4
    MSG_DUEL = 5
    MSG_SMS_SENT = 6
    MSG_MARRIED = 9
    WEIGHT = 10
    FOOD = 11
    MSG_LEVEL_OVER = 12
    HTML_UB = 14
    MSG_ELF = 15
    ADD_EXCLUDE2 = 17
    ADD_EXCLUDE = 18
    REM_EXCLUDE = 19
    ICONS1 = 20
    ICONS2 = 21
    ICON_AURA = 22
    MSG_TOWN_LEADER = 23
    MSG_RANK_CHANGED = 27
    MSG_WIN_LASTAVARD = 30
    MSG_FEEL_GOOD = 31
    SOMETHING1 = 33
    ICON_BLUEPOTION = 34
    ICON_POLYMORPH = 35
    ICON_CHATBAN = 36
    SOMETHING2 = 37
    HTML_CLAN1 = 38
    ICON_I2H = 40
    CHARACTER_CONFIG = 41
    LOGOUT = 42
    MSG_CANT_LOGOUT = 43
    CALL_SOMETHING = 45
    MSG_COLOSSEUM = 49
    HTML_CLAN2 = 51
    COOK_WINDOW = 52
    ICON_COOKING = 53
    FISHING = 55
    EXPBLESS = 82

    def __init__(self, subCode, value=None, tt=None, name=None, clan=None, names=None):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_PACKETBOX)
        self.writeC(subCode)

        if value:
            if subCode in (S_PacketBox.ICON_BLUEPOTION, S_PacketBox.ICON_CHATBAN, S_PacketBox.ICON_I2H, S_PacketBox.ICON_POLYMORPH):
                self.writeH(value)
            elif subCode in (S_PacketBox.MSG_WAR_BEGIN, S_PacketBox.MSG_WAR_END, S_PacketBox.MSG_WAR_GOING):
                self.writeC(value)
                self.writeH(0)
            elif subCode in (S_PacketBox.MSG_SMS_SENT, S_PacketBox.WEIGHT, S_PacketBox.FOOD):
                self.writeC(value)
            elif subCode in (S_PacketBox.MSG_ELF, S_PacketBox.MSG_RANK_CHANGED, S_PacketBox.MSG_COLOSSEUM):
                self.writeC(value)
            elif subCode == S_PacketBox.MSG_LEVEL_OVER:
                self.writeC(0)
                self.writeC(value)
            elif subCode == S_PacketBox.COOK_WINDOW:
                self.writeC(0xdb)
                self.writeC(0x31)
                self.writeC(0xdf)
                self.writeC(0x02)
                self.writeC(0x01)
                self.writeC(value)
            elif subCode == S_PacketBox.EXPBLESS:
                self.writeC(value)
            return

        if tt:
            type, time = tt
            if subCode == S_PacketBox.ICON_COOKING:
                if type != 7:
                    self.writeC(0x0c)
                    self.writeC(0x0c)
                    self.writeC(0x0c)
                    self.writeC(0x12)
                    self.writeC(0x0c)
                    self.writeC(0x09)
                    self.writeC(0x00)
                    self.writeC(0x00)
                    self.writeC(type)
                    self.writeC(0x24)
                    self.writeH(time)
                    self.writeH(0x00)
                else:
                    self.writeC(0x0c)
                    self.writeC(0x0c)
                    self.writeC(0x0c)
                    self.writeC(0x12)
                    self.writeC(0x0c)
                    self.writeC(0x09)
                    self.writeC(0xc8)
                    self.writeC(0x00)
                    self.writeC(type)
                    self.writeC(0x26)
                    self.writeH(time)
                    self.writeC(0x3e)
                    self.writeC(0x87)
            elif subCode == S_PacketBox.MSG_DUEL:
                self.writeD(type)
                self.writeD(time)
            return

        if name:
            if subCode in (S_PacketBox.ADD_EXCLUDE, S_PacketBox.REM_EXCLUDE, S_PacketBox.MSG_TOWN_LEADER):
                self.writeS(name)
            return

        if clan:
            id, name, clanName = clan
            if subCode == S_PacketBox.MSG_WIN_LASTAVARD:
                self.writeD(id)
                self.writeS(name)
                self.writeS(clanName)
            return

        if names:
            if subCode == S_PacketBox.ADD_EXCLUDE2:
                self.writeC(len(names))
                for name in names:
                    self.writeS(str(name))
            return

        if subCode == S_PacketBox.CALL_SOMETHING:
            self.callSomething()

    def callSomething(self):
        players = World().getAllPlayers()
        self.writeC(len(players))
        for player in players:
            acc = Account.load(player._accountName)
            if not acc:
                self.writeD(0)
            else:
                time = ctypes.c_int32(TimeUtil.dt2ts(datetime(1970, 1, 1)) + acc._lastActive)
                self.writeD(time)
            self.writeS(player._name)
            self.writeS(player.clanname)