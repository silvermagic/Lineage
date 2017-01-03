# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_Karma(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_PACKETBOX)
        self.writeC(0x57)
        self.writeD(pc._karma._karma)

    def getContent(self):
        return self.getBytes()