# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_AddItem(ServerBasePacket):
    def __init__(self, item_inst):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_ADDITEM)
        self.writeD(item_inst._id)
        self.writeC(item_inst._useType)
        self.writeC(0)
        self.writeH(item_inst._item._gfxId)
        self.writeC(item_inst._bless)
        self.writeD(item_inst._count)
        if item_inst._isIdentified:
            self.writeC(1)
        else:
            self.writeC(0)
        self.writeS(item_inst.getViewName())
        if not item_inst._isIdentified:
            self.writeC(0)
        else:
            status = item_inst.getStatusBytes()
            self.writeC(len(status))
            self.writeByte(status)