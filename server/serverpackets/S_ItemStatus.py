# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_ItemStatus(ServerBasePacket):
    def __init__(self, itemInst):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_ITEMSTATUS)
        self.writeD(itemInst._id)
        self.writeC(itemInst.getViewName())
        self.writeD(itemInst._count)
        if not itemInst._isIdentified:
            self.writeC(0)
        else:
            status = itemInst.getStatusBytes()
            self.writeC(len(status))
            self.writeByte(status)