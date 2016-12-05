# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CharTitle(ServerBasePacket):
    def __init__(self, objid, title):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_CHARTITLE)
        self.writeD(objid)
        self.writeS(title)

    def getContent(self):
        return self.getBytes()