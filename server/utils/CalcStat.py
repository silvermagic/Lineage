# -*- coding: utf-8 -*-

import random
from Config import Config

class CalcStat():
    @classmethod
    def calcAc(cls, level, dex):
        acBonus = 10
        if dex <= 9:
            acBonus -= level / 8
        elif dex >= 10 and dex <= 12:
            acBonus -= level / 7
        elif dex >= 13 and dex <= 15:
            acBonus -= level / 6
        elif dex >= 16 and dex <= 17:
            acBonus -= level / 5
        elif dex >= 18:
            acBonus -= level / 4
        return int(acBonus)

    @classmethod
    def calcStatMr(cls, wis):
        if wis <= 14:
            mrBonus = 0
        elif wis >= 15 or wis <= 16:
            mrBonus = 3
        elif wis == 17:
            mrBonus = 6
        elif wis == 18:
            mrBonus = 10
        elif wis == 19:
            mrBonus = 15
        elif wis == 20:
            mrBonus = 21
        elif wis == 21:
            mrBonus = 28
        elif wis == 22:
            mrBonus = 37
        elif wis == 23:
            mrBonus = 47
        elif wis == 24:
            mrBonus = 50
        else:
            mrBonus = 50
        return mrBonus

    @classmethod
    def calcDiffMr(cls, wis, diff):
        cls.calcStatMr(wis + diff) - cls.calcStatMr(wis)

    @classmethod
    def calcStatHp(cls, charType, baseMaxHp, baseCon, originalHpup):
        randomhp = 0
        if baseCon > 15:
            randomhp = baseCon - 15
        if charType == 0:
            randomhp += 11 + random.randint(0,2)
            if baseMaxHp + randomhp > Config.getint('charsettings', 'PrinceMaxHP'):
                randomhp = Config.getint('charsettings', 'PrinceMaxHP') - baseMaxHp
        elif charType == 1:
            randomhp += 17 + random.randint(0,2)
            if baseMaxHp + randomhp > Config.getint('charsettings', 'KnightMaxHP'):
                randomhp = Config.getint('charsettings', 'KnightMaxHP') - baseMaxHp
        elif charType == 2:
            randomhp += 10 + random.randint(0,2)
            if baseMaxHp + randomhp > Config.getint('charsettings', 'ElfMaxHP'):
                randomhp = Config.getint('charsettings', 'ElfMaxHP') - baseMaxHp
        elif charType == 3:
            randomhp += 7 + random.randint(0,2)
            if baseMaxHp + randomhp > Config.getint('charsettings', 'WizardMaxHP'):
                randomhp = Config.getint('charsettings', 'WizardMaxHP') - baseMaxHp
        elif charType == 4:
            randomhp += 10 + random.randint(0,2)
            if baseMaxHp + randomhp > Config.getint('charsettings', 'DarkelfMaxHP'):
                randomhp = Config.getint('charsettings', 'DarkelfMaxHP') - baseMaxHp
        elif charType == 5:
            randomhp += 13 + random.randint(0,2)
            if baseMaxHp + randomhp > Config.getint('charsettings', 'DragonKnightMaxHP'):
                randomhp = Config.getint('charsettings', 'DragonKnightMaxHP') - baseMaxHp
        elif charType == 6:
            randomhp += 9 + random.randint(0,2)
            if baseMaxHp + randomhp > Config.getint('charsettings', 'IllusionistMaxHP'):
                randomhp = Config.getint('charsettings', 'IllusionistMaxHP') - baseMaxHp

        randomhp += originalHpup
        if randomhp < 0:
            randomhp = 0

        return randomhp

    @classmethod
    def calcStatMp(cls, charType, baseMaxMp, baseWis, originalMpup):
        if baseWis < 9 or baseWis > 9 and baseWis < 12:
            seedY = 2
        elif baseWis == 9 or baseWis >= 12 and baseWis <= 17:
            seedY = 3
        elif baseWis >= 18 and baseWis <= 23 or baseWis == 25 or baseWis == 26 \
                or baseWis == 29 or baseWis == 30 or baseWis == 33 or baseWis == 34:
            seedY = 4
        elif baseWis == 24 or baseWis == 27 or baseWis == 28 \
                or baseWis == 31 or baseWis == 32 or baseWis >= 35:
            seedY = 5

        seedZ = 0
        if baseWis >= 7 and baseWis <= 9:
            seedZ = 0
        elif baseWis >= 10 and baseWis <= 14:
            seedZ = 1
        elif baseWis >= 15 and baseWis <= 20:
            seedZ = 2
        elif baseWis >= 21 and baseWis <= 24:
            seedZ = 3
        elif baseWis >= 25 and baseWis <= 28:
            seedZ = 4
        elif baseWis >= 29 and baseWis <= 32:
            seedZ = 5
        elif baseWis >= 33:
            seedZ = 6

        randommp = random.randint(0, seedY) + 1 + seedZ

        if charType == 0:
            if baseMaxMp + randommp > Config.getint('charsettings', 'PrinceMaxMP'):
                randommp = Config.getint('charsettings', 'PrinceMaxMP') - baseMaxMp
        elif charType == 1:
            randommp = int(randommp * 2 / 3)
            if baseMaxMp + randommp > Config.getint('charsettings', 'KnightMaxMP'):
                randommp = Config.getint('charsettings', 'KnightMaxMP') - baseMaxMp
        elif charType == 2:
            randommp = int(randommp * 1.5)
            if baseMaxMp + randommp > Config.getint('charsettings', 'ElfMaxMP'):
                randommp = Config.getint('charsettings', 'ElfMaxMP') - baseMaxMp
        elif charType == 3:
            randommp *= 2
            if baseMaxMp + randommp > Config.getint('charsettings', 'WizardMaxMP'):
                randommp = Config.getint('charsettings', 'WizardMaxMP')
        elif charType == 4:
            randommp = int(randommp * 1.5)
            if baseMaxMp + randommp > Config.getint('charsettings', 'DarkelfMaxMP'):
                randommp = Config.getint('charsettings', 'DarkelfMaxMP') - baseMaxMp
        elif charType == 5:
            randommp = int(randommp * 2 / 3)
            if baseMaxMp + randommp > Config.getint('charsettings', 'DragonKnightMaxMP'):
                randommp = Config.getint('charsettings', 'DragonKnightMaxMP') - baseMaxMp
        elif charType == 6:
            randommp = int(randommp * 5 / 3)
            if baseMaxMp + randommp > Config.getint('charsettings', 'IllusionistMaxMP'):
                randommp = Config.getint('charsettings', 'IllusionistMaxMP') - baseMaxMp

        randommp += originalMpup

        if randommp < 0:
            randommp = 0

        return randommp