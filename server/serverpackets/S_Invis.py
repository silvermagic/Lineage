# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_Invis(ServerBasePacket):
    def __init__(self, objid, type):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_INVIS)
        self.writeD(objid)
        self.writeC(type)

    def getContent(self):
        return self.getBytes()

