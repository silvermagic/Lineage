# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_MapID(ServerBasePacket):
    def __init__(self, mapid, isUnderwater):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_MAPID)
        self.writeH(mapid)
        self.writeC(int(isUnderwater))
        self.writeC(0)
        self.writeH(0)
        self.writeC(0)
        self.writeD(0)

    def getContent(self):
        return self.getBytes()