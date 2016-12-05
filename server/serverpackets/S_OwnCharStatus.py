# -*- coding: utf-8 -*-

import ctypes
from server.codes import Opcodes
from server.model.gametime.GameTimeClock import GameTimeClock
from ServerBasePacket import ServerBasePacket

class S_OwnCharStatus(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        time = GameTimeClock()._currentTime._time
        time -= time % 300
        self.writeC(Opcodes.S_OPCODE_OWNCHARSTATUS)
        self.writeD(pc._id)
        if pc._level < 1:
            self.writeC(1)
        elif pc._level > 127:
            self.writeC(127)
        else:
            self.writeC(pc._level)
        self.writeD(pc.getExp())
        self.writeC(pc._str)
        self.writeC(pc._int)
        self.writeC(pc._wis)
        self.writeC(pc._dex)
        self.writeC(pc._con)
        self.writeC(pc._cha)
        self.writeH(pc._currentHp)
        self.writeH(pc._maxHp)
        self.writeH(pc._currentMp)
        self.writeH(pc._maxMp)
        self.writeC(pc._ac)
        self.writeD(ctypes.c_uint32(time).value)
        self.writeC(pc._food)
        self.writeC(pc._inventory.getWeight240())
        self.writeH(pc._lawful)
        self.writeC(pc._fire)
        self.writeC(pc._water)
        self.writeC(pc._wind)
        self.writeC(pc._earth)

    def getContent(self):
        return self.getBytes()