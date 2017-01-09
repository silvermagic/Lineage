# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CharPacks(ServerBasePacket):
    def __init__(self, name, clanName, type, sex, lawful,
                 hp, mp, ac, lv, str, dex, con, wis, cha,
                 intel, accessLevel, birthday):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_CHARLIST)
        self.writeS(name)
        self.writeS(clanName)
        self.writeC(type)
        self.writeC(sex)
        self.writeH(lawful)
        self.writeH(hp)
        self.writeH(mp)
        self.writeC(ac)
        self.writeC(lv)
        self.writeC(str)
        self.writeC(dex)
        self.writeC(con)
        self.writeC(wis)
        self.writeC(cha)
        self.writeC(intel)
        self.writeC(0) # is Administrator
        self.writeD(birthday)

    def getContent(self):
        return self.getBytes()