# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_DeleteInventoryItem(ServerBasePacket):
    def __init__(self, item_inst):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_DELETEINVENTORYITEM)
        self.writeD(item_inst._id)

    def getContent(self):
        return self.getBytes()
