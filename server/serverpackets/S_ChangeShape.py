# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_ChangeShape(ServerBasePacket):
    def __init__(self, objId, polyId, weaponTakeoff = False):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_POLY)
        self.writeD(objId)
        self.writeH(polyId)
        if weaponTakeoff:
            self.writeH(0)
        else:
            self.writeH(29)