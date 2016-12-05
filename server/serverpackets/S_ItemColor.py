# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_ItemColor(ServerBasePacket):
    def __init__(self, itemInst):
        ServerBasePacket.__init__(self)
        if not itemInst:
            return
        self.writeC(Opcodes.S_OPCODE_ITEMCOLOR)
        self.writeD(itemInst._id)
        self.writeC(itemInst._bless)