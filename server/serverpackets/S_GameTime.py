# -*- coding: utf-8 -*-

import ctypes,logging
from server.codes import Opcodes
from server.model.gametime.GameTimeClock import GameTimeClock
from ServerBasePacket import ServerBasePacket

class S_GameTime(ServerBasePacket):
    def __init__(self, time = None):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_GAMETIME)
        if not time:
            self.writeD(ctypes.c_uint32(GameTimeClock()._currentTime._time).value)
        else:
            self.writeD(ctypes.c_uint32(time).value)

    def getContent(self):
        return self.getBytes()

