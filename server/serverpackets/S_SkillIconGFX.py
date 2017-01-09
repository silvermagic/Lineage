# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_SkillIconGFX(ServerBasePacket):
    def __init__(self, iconId, timeSecs):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_SKILLICONGFX)
        self.writeC(iconId)
        self.writeH(timeSecs)