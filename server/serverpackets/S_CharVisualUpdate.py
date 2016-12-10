# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CharVisualUpdate(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_CHARVISUALUPDATE)
        self.writeD(pc._id)
        self.writeC(pc._weaponType)

    def getContent(self):
        return self.getBytes()