# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_NewCharPacket(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_NEWCHARPACK)
        self.writeS(pc._name)
        self.writeS('')
        self.writeC(pc._type)
        self.writeC(pc._sex)
        self.writeH(pc._lawful)
        self.writeH(pc._maxHp)
        self.writeH(pc._maxMp)
        self.writeC(pc._ac)
        self.writeC(pc.getLevel())
        self.writeC(pc._str)
        self.writeC(pc._dex)
        self.writeC(pc._con)
        self.writeC(pc._wis)
        self.writeC(pc._cha)
        self.writeC(pc._int)
        self.writeC(0)
        self.writeD(pc.getSimpleBirthday())