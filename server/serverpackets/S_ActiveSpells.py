# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_ActiveSpells(ServerBasePacket):
    def __init__(self):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_ACTIVESPELLS)
        self.writeC(0x14)
        self.writeC(0x69)

    def getContent(self):
        return self.getBytes()