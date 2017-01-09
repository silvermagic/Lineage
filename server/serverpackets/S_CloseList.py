# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CloseList(ServerBasePacket):
    def __init__(self, objid):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_SHOWHTML)
        self.writeD(objid)
        self.writeS("")