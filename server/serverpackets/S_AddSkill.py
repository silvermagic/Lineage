# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_AddSkill(ServerBasePacket):
    def __init__(self, level1, level2, level3, level4, level5, level6, level7, level8, level9, level10,
                 knight, l2, de1, de2, royal, l3, elf1, elf2, elf3, elf4, elf5, elf6,
                 k5, l5, m5, n5, o5, p5):
        ServerBasePacket.__init__(self)
        i6 = level5 + level6 + level7 + level8
        j6 = level9 + level10
        self.writeC(Opcodes.S_OPCODE_ADDSKILL)
        if i6 > 0 and j6 == 0:
            self.writeC(50)
        elif j6 > 0:
            self.writeC(100)
        else:
            self.writeC(32)

        self.writeC(level1)
        self.writeC(level2)
        self.writeC(level3)
        self.writeC(level4)
        self.writeC(level5)
        self.writeC(level6)
        self.writeC(level7)
        self.writeC(level8)
        self.writeC(level9)
        self.writeC(level10)
        self.writeC(knight)
        self.writeC(l2)
        self.writeC(de1)
        self.writeC(de2)
        self.writeC(royal)
        self.writeC(l3)
        self.writeC(elf1)
        self.writeC(elf2)
        self.writeC(elf3)
        self.writeC(elf4)
        self.writeC(elf5)
        self.writeC(elf6)
        self.writeC(k5)
        self.writeC(l5)
        self.writeC(m5)
        self.writeC(n5)
        self.writeC(o5)
        self.writeC(p5)
        self.writeD(0)
        self.writeD(0)

    def getContent(self):
        return self.getBytes()