# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_ItemAmount(ServerBasePacket):
    def __init__(self, itemInst):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_ITEMAMOUNT)
        self.writeD(itemInst._id)
        self.writeS(itemInst.getViewName())
        self.writeD(itemInst._count)
        if not itemInst._isIdentified:
            self.writeC(0)
        else:
            status = itemInst.getStatusBytes()
            self.writeC(len(status))
            self.writeByte(status)


    def getContent(self):
        return self.getBytes()