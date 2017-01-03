# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_SPMR(ServerBasePacket):
    '''
    返回魔功和魔防
    '''
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_SPMR)
        if False:
            self.writeC(pc._trueSp - pc._baseSp - 2)
        else:
            self.writeC(pc._trueSp - pc._baseSp)
        self.writeC(pc._trueMr - pc._baseMr)

    def getContent(self):
        return self.getBytes()
