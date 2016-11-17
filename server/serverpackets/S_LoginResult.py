# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_LoginResult(ServerBasePacket):

    REASON_LOGIN_OK = 0x00
    REASON_ACCOUNT_IN_USE = 0x16
    REASON_ACCOUNT_ALREADY_EXISTS = 0x07
    REASON_ACCESS_FAILED = 0x08
    REASON_USER_OR_PASS_WRONG = 0x08
    REASON_PASS_WRONG = 0x08

    def __init__(self, reason):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_LOGINRESULT)
        self.writeC(reason)
        self.writeD(0x00000000)
        self.writeD(0x00000000)
        self.writeD(0x00000000)