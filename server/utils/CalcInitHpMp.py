# -*- coding: utf-8 -*-

class CalcInitHpMp():
    @classmethod
    def calcInitHp(cls, pc):
        hp = 1
        if pc.isCrown():
            hp = 14
        elif pc.isKnight():
            hp = 16
        elif pc.isElf():
            hp = 15
        elif pc.isWizard():
            hp = 12
        elif pc.isDarkelf():
            hp = 12
        elif pc.isDragonKnight():
            hp = 15
        elif pc.isIllusionist():
            hp = 15
        return hp

    @classmethod
    def calcInitMp(cls, pc):
        mp = 1
        if pc.isCrown():
            if pc._wis == 1:
                mp = 2
            elif pc._wis in range(12,16):
                mp = 3
            elif pc._wis in range(16,19):
                mp = 4
            else:
                mp = 2
        elif pc.isKnight():
            if pc._wis in range(9,12):
                mp = 1
            elif pc._wis in range(12,14):
                mp = 2
            else:
                mp = 1
        elif pc.isElf():
            if pc._wis in range(12,16):
                mp = 4
            elif pc._wis in range(16,19):
                mp = 6
            else:
                mp = 4
        elif pc.isWizard():
            if pc._wis in range(12,16):
                mp = 6
            elif pc._wis in range(16,19):
                mp = 8
            else:
                mp = 6
        elif pc.isDarkelf():
            if pc._wis in range(10,12):
                mp = 3
            elif pc._wis in range(12,16):
                mp = 4
            elif pc._wis in range(16, 19):
                mp = 6
            else:
                mp = 3
        elif pc.isDragonKnight():
            if pc._wis in range(12,16):
                mp = 4
            elif pc._wis in range(16,19):
                mp = 6
            else:
                mp = 4
        elif pc.isIllusionist():
            if pc._wis in range(12, 16):
                mp = 4
            elif pc._wis in range(16, 19):
                mp = 6
            else:
                mp = 4

        return mp