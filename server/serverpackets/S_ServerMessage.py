# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_ServerMessage(ServerBasePacket):
    def __init__(self, type, msg1 = None, msg2 = None, msg3 = None, msg4 = None, msg5 = None):
        ServerBasePacket.__init__(self)
        check = 0
        # 如果前面的为None后面的肯定也全是None就不需要继续判断后面的了
        if not msg1:
            check = 0
        elif not msg2:
            check = 1
        elif not msg3:
            check = 2
        elif not msg4:
            check = 3
        elif not msg5:
            check = 4
        else:
            check = 5
        self._buildPacket(type, msg1, msg2, msg3, msg4, msg5, check)

    def _buildPacket(self, type, msg1, msg2, msg3, msg4, msg5, check):
        self.writeC(Opcodes.S_OPCODE_SERVERMSG)
        self.writeH(type)

        if check == 0:
            self.writeC(0)
        elif check == 1:
            self.writeC(1)
            self.writeS(msg1)
        elif check == 2:
            self.writeC(2)
            self.writeS(msg1)
            self.writeS(msg2)
        elif check == 3:
            self.writeC(3)
            self.writeS(msg1)
            self.writeS(msg2)
            self.writeS(msg3)
        elif check == 4:
            self.writeC(4)
            self.writeS(msg1)
            self.writeS(msg2)
            self.writeS(msg3)
            self.writeS(msg4)
        else:
            self.writeC(5)
            self.writeS(msg1)
            self.writeS(msg2)
            self.writeS(msg3)
            self.writeS(msg4)
            self.writeS(msg5)