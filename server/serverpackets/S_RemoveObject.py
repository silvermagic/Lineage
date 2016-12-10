# -*- coding: utf-8 -*-

import ctypes
from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_RemoveObject(ServerBasePacket):
    def __init__(self, obj):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_REMOVE_OBJECT)
        self.writeD(obj._id)

    def getContent(self):
        return self.getBytes()

