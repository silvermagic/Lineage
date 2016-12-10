# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_Ability(ServerBasePacket):
    def __init__(self, type, equipped):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_ABILITY)
        self.writeC(type)
        if equipped:
            self.writeC(0x01)
        else:
            self.writeC(0x00)
        self.writeC(0x02)
        self.writeH(0x0000)

    def getContent(self):
        return self.getBytes()