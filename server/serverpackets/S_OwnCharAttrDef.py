# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_OwnCharAttrDef(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_OWNCHARATTRDEF)
        self.writeC(pc._ac)
        self.writeC(pc._fire)
        self.writeC(pc._water)
        self.writeC(pc._wind)
        self.writeC(pc._earth)

    def getContent(self):
        return self.getBytes()
