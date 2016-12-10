# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_SkillHaste(ServerBasePacket):
    def __init__(self, i, j, k):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_SKILLHASTE)
        self.writeD(i)
        self.writeC(j)
        self.writeH(k)

    def getContent(self):
        return self.getBytes()
