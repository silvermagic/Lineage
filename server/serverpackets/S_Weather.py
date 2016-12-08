# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_Weather(ServerBasePacket):
    def __init__(self, weather):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_WEATHER)
        self.writeC(weather)

    def getContent(self):
        return self.getBytes()
