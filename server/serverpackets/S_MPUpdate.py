# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_MPUpdate(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_MPUPDATE)
        if pc._currentMp >= 32767:
            self.writeH(32767)
        elif pc._currentMp < 1:
            self.writeH(1)
        else:
            self.writeH(pc._currentMp)

        if pc._maxMp >= 32767:
            self.writeH(32767)
        elif pc._maxMp < 1:
            self.writeH(1)
        else:
            self.writeH(pc._maxMp)