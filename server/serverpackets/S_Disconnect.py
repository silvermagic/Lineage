# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_Disconnect(ServerBasePacket):
    def __init__(self):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_DISCONNECT)
        self.writeH(500)
        self.writeD(0x00000000)
