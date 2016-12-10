# -*- coding: utf-8 -*-

import threading
from server.model.skill import SkillId
from server.utils.IntRange import IntRange
from Object import Object

class Character(Object):
    def __init__(self):
        Object.__init__(self)
        self._level = 1
        self._exp = 0
        self._name = ''
        self._currentHp = 0
        self._maxHp = 0
        self._trueMaxHp = 0
        self._currentMp = 0
        self._maxMp = 0
        self._trueMaxMp = 0
        self._ac = 0
        self._trueAc = 0
        self._str = 0
        self._trueStr = 0
        self._con = 0
        self._trueCon = 0
        self._dex = 0
        self._trueDex = 0
        self._cha = 0
        self._trueCha = 0
        self._int = 0
        self._trueInt = 0
        self._wis = 0
        self._trueWis = 0
        self._wind = 0
        self._trueWind = 0
        self._water = 0
        self._trueWater = 0
        self._fire = 0
        self._trueFire = 0
        self._earth = 0
        self._trueEarth = 0
        self._addAttrKind = 0
        self._registStun = 0
        self._trueRegistStun = 0
        self._registStone = 0
        self._trueRegistStone = 0
        self._registSleep = 0
        self._trueRegistSleep = 0
        self._registFreeze = 0
        self._trueRegistFreeze = 0
        self._registSustain = 0
        self._trueRegistSustain = 0
        self._registBlind = 0
        self._trueRegistBlind = 0
        self._dmgup = 0
        self._trueDmgup = 0
        self._bowDmgup = 0
        self._trueBowDmgup = 0
        self._hitup = 0
        self._trueHitup = 0
        self._bowHitup = 0
        self._trueBowHitup = 0
        self._mr = 0
        self._trueMr = 0
        self._sp = 0
        self._isDead = False
        self._status = 0
        self._title = ''
        self._lawful = 0
        self._heading = 0 # 0.左上 1.上 2.右上 3.右 4.右下 5.下 6.左下 7.左
        self._moveSpeed = 0 # 一段加速
        self._braveSpeed = 0 # 二段加速
        self._tempCharGfx = 0
        self._gfxid = 0
        self._chaLightSize = 0
        self._ownLightSize = 0
        self._lock = threading.Lock()

        self._skillEffect = {}
        self._itemdelay = {}
        # todo: 延迟系统

    def setExp(self, exp):
        self._exp = exp

    def setCurrentHp(self, i):
        if self._currentHp == i:
            return
        self._currentHp = i
        if self._currentHp >= self._maxHp:
            self._currentHp = self._maxHp

    def setMaxHp(self, hp):
        self._trueMaxHp = hp
        self._maxHp = IntRange.ensure(self._trueMaxHp, 1, 32767)
        self._currentHp = min(self._currentHp, self._maxHp)

    def addMaxHp(self, i):
        self.setMaxHp(self._trueMaxHp + i)

    def setCurrentMp(self, i):
        if self._currentMp == i:
            return
        self._currentMp = i
        if self._currentMp >= self._maxMp:
            self._currentMp = self._maxMp

    def setMaxMp(self, mp):
        self._trueMaxMp = mp
        self._maxMp = IntRange.ensure(self._trueMaxMp, 0, 32767)
        self._currentMp = min(self._currentMp, self._maxMp)

    def addMaxMp(self, i):
        self.setMaxMp(self._trueMaxMp + i)

    def setAc(self, i):
        self._trueAc = i
        self._ac = IntRange.ensure(i, -128, 127)

    def addAc(self, i):
        self.setAc(self._trueAc + i)

    def setStr(self, i):
        self._trueStr = i
        self._str = IntRange.ensure(i, 1, 127)

    def addStr(self, i):
        self.setStr(self._trueStr + i)

    def setCon(self, i):
        self._trueCon = i
        self._con = IntRange.ensure(i, 1, 127)

    def addCon(self, i):
        self.setCon(self._trueCon + i)

    def setDex(self, i):
        self._trueDex = i
        self._dex = IntRange.ensure(i, 1, 127)

    def addDex(self, i):
        self.setDex(self._trueDex + i)

    def setCha(self, i):
        self._trueCha = i
        self._cha = IntRange.ensure(i, 1, 127)

    def addCha(self, i):
        self.setCha(self._trueCha + i)

    def setInt(self, i):
        self._trueInt = i
        self._int = IntRange.ensure(i, 1, 127)

    def addInt(self, i):
        self.setInt(self._trueInt + i)

    def setWis(self, i):
        self._trueWis = i
        self._wis = IntRange.ensure(i, 1, 127)

    def addWis(self, i):
        self.setWis(self._trueWis + i)

    def addWind(self, i):
        self._trueWind += i
        self._wind = IntRange.ensure(self._trueWind, -128, 127)

    def addWater(self, i):
        self._trueWater += i
        self._water = IntRange.ensure(self._trueWater, -128, 127)

    def addFire(self, i):
        self._trueFire += i
        self._fire = IntRange.ensure(self._trueFire, -128, 127)

    def addEarth(self, i):
        self._trueEarth += i
        self._earth = IntRange.ensure(self._trueEarth, -128, 127)

    def addRegistStun(self, i):
        self._trueRegistStun += i
        self._registStun = IntRange.ensure(self._trueRegistStun, -128, 127)

    def addRegistStone(self, i):
        self._trueRegistStone += i
        self._registStone = IntRange.ensure(self._trueRegistStone, -128, 127)

    def addRegistSleep(self, i):
        self._trueRegistSleep += i
        self._registSleep = IntRange.ensure(self._trueRegistSleep, -128, 127)

    def addRegistFreeze(self, i):
        self._trueRegistFreeze += i
        self._registFreeze = IntRange.ensure(self._trueRegistFreeze, -128, 127)

    def addRegistSustain(self, i):
        self._trueRegistSustain += i
        self._registSustain = IntRange.ensure(self._trueRegistSustain, -128, 127)

    def addRegistBlind(self, i):
        self._trueRegistBlind += i
        self._registBlind = IntRange.ensure(self._trueRegistBlind, -128, 127)

    def addDmgup(self, i):
        self._trueDmgup += i
        self._dmgup = IntRange.ensure(self._trueDmgup, -128, 127)

    def addBowDmgup(self, i):
        self._trueBowDmgup += i
        self._bowDmgup = IntRange.ensure(self._trueBowDmgup, -128, 127)

    def addHitup(self, i):
        self._trueHitup += i
        self._hitup = IntRange.ensure(self._trueHitup, -128, 127)

    def addBowHitup(self, i):
        self._trueBowHitup += i
        self._bowHitup = IntRange.ensure(self._trueBowHitup, -128, 127)

    # 特殊处理
    def getMr(self):
        return self._mr

    def addMr(self, i):
        self._trueMr += i
        if self._trueMr <= 0:
            self._mr = 0
        else:
            self._mr = self._trueMr

    def getMagicBonus(self):
        i = self._int
        if i <= 5:
            return -2
        elif i <= 8:
            return -1
        elif i <= 11:
            return 0
        elif i <= 14:
            return 1
        elif i <= 17:
            return 2
        elif i <= 24:
            return i - 15
        elif i <= 35:
            return 10
        elif i <= 42:
            return 11
        elif i <= 49:
            return 12
        elif i <= 50:
            return 13
        else:
            return i - 25

    def getSp(self):
        return self.getTrueSp() + self._sp

    def getTrueSp(self):
        return int(self._level / 4) + self.getMagicBonus()

    def addSp(self, i):
        self._sp += i

    def addLawful(self, i):
        with self._lock:
            self._lawful += i
            self._lawful = IntRange.ensure(self._lawful, -32768, 32767)

    def broadcastPacket(self, packet):
        from server.model.World import World
        for pc in World().getVisiblePlayer(self):
            pc.sendPackets(packet)

    def turnOnOffLight(self):
        pass

    def hasItemDelay(self, delayId):
        return self._itemdelay.has_key(delayId)

    def isInvisble(self):
        return self.hasSkillEffect(SkillId.INVISIBILITY) or self.hasSkillEffect(SkillId.BLIND_HIDING)

    def broadcastPacketForFindInvis(self):
        return

    def hasSkillEffect(self, skillId):
        return self._skillEffect.has_key(skillId)

    def setSkillEffect(self, skillId, timeMillis):
        return

    def removeSkillEffect(self, skillId):
        return

    def killSkillEffectTimer(self, skillId):
        return
