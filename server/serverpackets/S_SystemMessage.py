# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_SystemMessage(ServerBasePacket):
    def __init__(self, msg, nameid=None):
        ServerBasePacket.__init__(self)
        if not nameid:
            self.writeC(Opcodes.S_OPCODE_SYSMSG)
            self.writeC(0x09)
            self.writeS(msg)
        else:
            self.writeC(Opcodes.S_OPCODE_NPCSHOUT)
            self.writeC(2)
            self.writeD(0)
            self.writeS(msg)

    def getContent(self):
        return self.getBytes()
