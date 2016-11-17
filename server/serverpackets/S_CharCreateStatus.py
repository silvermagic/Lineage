# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CharCreateStatus(ServerBasePacket):
    REASON_OK = 0x02
    REASON_ALREADY_EXSISTS = 0x06
    REASON_INVALID_NAME = 0x09
    REASON_WRONG_AMOUNT = 0x15
    def __init__(self, reason):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_NEWCHARWRONG)
        self.writeC(reason)
        self.writeD(0x00000000)
        self.writeD(0x0000)

    def getContent(self):
        return self.getBytes()