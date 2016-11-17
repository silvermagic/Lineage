# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_HPUpdate(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_HPUPDATE)
        if pc._currentHp >= 32767:
            self.writeH(32767)
        elif pc._currentHp < 1:
            self.writeH(1)
        else:
            self.writeH(pc._currentHp)

        if pc._maxHp >= 32767:
            self.writeH(32767)
        elif pc._maxHp < 1:
            self.writeH(1)
        else:
            self.writeH(pc._maxHp)