# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_InvList(ServerBasePacket):
    def __init__(self, items):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_INVLIST)
        self.writeC(len(items))
        for item in items:
            self.writeD(item._id)
            self.writeC(item._item._useType)
            self.writeC(0)
            self.writeH(item._item._gfxId)
            self.writeC(item._bless)
            self.writeD(item._count)
            self.writeC(int(item._isIdentified))
            self.writeS(item.getViewName())
            if not item._isIdentified:
                self.writeC(0)
            else:
                status = item.getStatusBytes()
                self.writeC(len(status))
                self.writeByte(status)