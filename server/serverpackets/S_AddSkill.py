# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_AddSkill(ServerBasePacket):
    def __init__(self, Wizard, Wizard2, Wizard3, Wizard4, Wizard5, Wizard6, Wizard7, Wizard8, Wizard9, Wizard10,
                 Knight, Knight2, Darkelf, Darkelf2, Crown, unused, Elf, Elf2, Elf3, Elf4, Elf5, Elf6,
                 DragonKnight, DragonKnight2, DragonKnight3, Illusionist, Illusionist2, Illusionist3):
        '''
        更新角色魔法列表
        :param Wizard: 法师一级魔法
        :param Wizard2: 法师二级魔法
        :param Wizard3: 法师三级魔法
        :param Wizard4: 法师四级魔法
        :param Wizard5: 法师五级魔法
        :param Wizard6: 法师六级魔法
        :param Wizard7: 法师七级魔法
        :param Wizard8: 法师八级魔法
        :param Wizard9: 法师九级魔法
        :param Wizard10: 法师十级魔法
        :param Knight:骑士一级魔法
        :param Knight2:骑士二级魔法
        :param Darkelf:黑暗妖精一级魔法d
        :param Darkelf2:黑暗妖精二级魔法d
        :param Crown:王族魔法
        :param unused:目前没有此等级魔法
        :param Elf:精灵一级魔法
        :param Elf2:精灵二级魔法
        :param Elf3:精灵三级魔法
        :param Elf4:精灵四级魔法
        :param Elf5:精灵五级魔法
        :param Elf6:精灵六级魔法
        :param DragonKnight:龙骑士一级魔法
        :param DragonKnight2:龙骑士二级魔法
        :param DragonKnight3:龙骑士三级魔法
        :param Illusionist:幻术师一级魔法
        :param Illusionist2:幻术师二级魔法
        :param Illusionist3:幻术师三级魔法
        '''
        ServerBasePacket.__init__(self)
        i6 = Wizard5 + Wizard6 + Wizard7 + Wizard8
        j6 = Wizard9 + Wizard10
        self.writeC(Opcodes.S_OPCODE_ADDSKILL)
        if i6 > 0 and j6 == 0:
            self.writeC(50)
        elif j6 > 0:
            self.writeC(100)
        else:
            self.writeC(32)

        self.writeC(Wizard)
        self.writeC(Wizard2)
        self.writeC(Wizard3)
        self.writeC(Wizard4)
        self.writeC(Wizard5)
        self.writeC(Wizard6)
        self.writeC(Wizard7)
        self.writeC(Wizard8)
        self.writeC(Wizard9)
        self.writeC(Wizard10)
        self.writeC(Knight)
        self.writeC(Knight2)
        self.writeC(Darkelf)
        self.writeC(Darkelf2)
        self.writeC(Crown)
        self.writeC(unused)
        self.writeC(Elf)
        self.writeC(Elf2)
        self.writeC(Elf3)
        self.writeC(Elf4)
        self.writeC(Elf5)
        self.writeC(Elf6)
        self.writeC(DragonKnight)
        self.writeC(DragonKnight2)
        self.writeC(DragonKnight3)
        self.writeC(Illusionist)
        self.writeC(Illusionist2)
        self.writeC(Illusionist3)
        self.writeD(0)
        self.writeD(0)

    def getContent(self):
        return self.getBytes()