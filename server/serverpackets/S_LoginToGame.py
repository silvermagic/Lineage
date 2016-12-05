# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_LoginToGame(ServerBasePacket):
    def __init__(self):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_LOGINTOGAME)
        self.writeC(0x03)
        self.writeC(0x00)
        self.writeC(0xF7)
        self.writeC(0xAD)
        self.writeC(0x74)
        self.writeC(0x00)
        self.writeC(0xE5)

    def getContent(self):
        return self.getBytes()
