# -*- coding: utf-8 -*-

import logging,time
from datetime import datetime
from server.model.Character import Character
from server.model.Karma import Karma
from server.serverpackets.S_HPUpdate import S_HPUpdate
from server.serverpackets.S_MPUpdate import S_MPUpdate
from server.utils.IntRange import IntRange

CLASSID_KNIGHT_MALE = 61
CLASSID_KNIGHT_FEMALE = 48
CLASSID_ELF_MALE = 138
CLASSID_ELF_FEMALE = 37
CLASSID_WIZARD_MALE = 734
CLASSID_WIZARD_FEMALE = 1186
CLASSID_DARK_ELF_MALE = 2786
CLASSID_DARK_ELF_FEMALE = 2796
CLASSID_PRINCE = 0
CLASSID_PRINCESS = 1
CLASSID_DRAGON_KNIGHT_MALE = 6658
CLASSID_DRAGON_KNIGHT_FEMALE = 6661
CLASSID_ILLUSIONIST_MALE = 6671
CLASSID_ILLUSIONIST_FEMALE = 6650

INTERVAL_AUTO_UPDATE = 300
INTERVAL_EXP_MONITOR = 500

class PcInstance(Character):
    def __init__(self):
        Character.__init__(self)
        self._hpr = 0
        self._trueHpr = 0
        self._originalHpr = 0
        self._mpr = 0
        self._trueMpr = 0
        self._originalMpr = 0
        self._baseMaxHp = 0
        self._baseMaxMp = 0
        self._baseAc = 0
        self._baseStr = 0
        self._baseDex = 0
        self._baseCha = 0
        self._baseInt = 0
        self._baseWis = 0
        self._baseCon = 0
        self._originalAc = 0
        self._originalStr = 0
        self._originalCon = 0
        self._originalDex = 0
        self._originalCha = 0
        self._originalInt = 0
        self._originalWis = 0
        self._originalDmgup = 0
        self._originalBowDmgup = 0
        self._originalHitup = 0
        self._originalBowHitup = 0
        self._originalMr = 0
        self._originalMagicHit = 0
        self._originalMagicCritical = 0
        self._originalMagicConsumeReduction = 0
        self._originalMagicDamage = 0
        self._originalHpup = 0
        self._originalMpup = 0
        self._baseDmgup = 0
        self._baseBowDmgup = 0
        self._baseHitup = 0
        self._baseBowHitup = 0
        self._baseMr = 0
        self._advenHp = 0
        self._advenMp = 0
        self._netConnection = None
        self._accountName = ''
        self._birthday = time.time()
        self._highLevel = 0
        self._classId = 0
        self._sex = 0
        self._type = 0
        self._food = 0
        self._clanid = 0
        self._clanname = ''
        self._clanRank = 0
        self._bonusStats = 0
        self._elixirStats = 0
        self._elfAttr = 0
        self._PKcount = 0
        self._PkCountForElf = 0
        self._expRes = 0
        self._partnerId = 0
        self._accessLevel = 0
        self._currentWeapon = 0
        self._gm = False
        self._monitor = False
        self._onlineStatus = 0
        self._homeTownId = 0
        self._contribution = 0
        self._hellTime = 0
        self._banned = 0
        self._karma = Karma()
        self._lastPk = 0
        self._lastPkForElf = 0
        self._deleteTime = 0
        self._lastActive = time.time()
        self._ainZone = 0
        self._ainPoint = 0
        self._moveSpeed = 0
        self._braveSpeed = 0
        self._gmInvis = False

    def sendPackets(self, serverbasepacket):
        if not self._netConnection:
            return
        try:
            self._netConnection.sendPacket(serverbasepacket)
        except Exception as e:
            logging.error(e)

    def setExp(self, exp):
        with self._lock:
            self._exp = exp

    def setCurrentHp(self, i):
        if self._currentHp == i:
            return

        Character.setCurrentHp(self, i)
        self.sendPackets(S_HPUpdate(self))

    def setCurrentMp(self, i):
        if self._currentMp == i:
            return

        Character.setCurrentMp(self, i)
        self.sendPackets(S_MPUpdate(self))

    def addHpr(self, i):
        self._trueHpr += i
        self._hpr = max(0, self._trueHpr)

    def addMpr(self, i):
        self._trueMpr += i
        self._mpr = max(0, self._trueMpr)

    def isCrown(self):
        return (self._classId == CLASSID_PRINCE or self._classId == CLASSID_PRINCESS)

    def isKnight(self):
        return (self._classId == CLASSID_KNIGHT_MALE or self._classId == CLASSID_KNIGHT_FEMALE)

    def isElf(self):
        return (self._classId == CLASSID_ELF_MALE or self._classId == CLASSID_ELF_FEMALE)

    def isWizard(self):
        return (self._classId == CLASSID_WIZARD_MALE or self._classId == CLASSID_WIZARD_FEMALE)

    def isDarkelf(self):
        return (self._classId == CLASSID_DARK_ELF_MALE or self._classId == CLASSID_DARK_ELF_FEMALE)

    def isDragonKnight(self):
        return (self._classId == CLASSID_DRAGON_KNIGHT_MALE or self._classId == CLASSID_DRAGON_KNIGHT_FEMALE)

    def isIllusionist(self):
        return (self._classId == CLASSID_ILLUSIONIST_MALE or self._classId == CLASSID_ILLUSIONIST_FEMALE)

    def addBaseMaxHp(self, i):
        i += self._baseMaxHp
        i = IntRange.ensure(i, 1, 32767)
        self.addMaxHp(i - self._baseMaxHp)
        self._baseMaxHp = i

    def addBaseMaxMp(self, i):
        i += self._baseMaxMp
        i = IntRange.ensure(i, 1, 32767)
        self.addMaxMp(i - self._baseMaxMp)
        self._baseMaxMp = i

    def addBaseStr(self, i):
        i += self._baseStr
        i = IntRange.ensure(i, 1, 127)
        self.addStr(i - self._baseStr)
        self._baseStr = i

    def addBaseCon(self, i):
        i += self._baseCon
        i = IntRange.ensure(i, 1, 127)
        self.addCon(i - self._baseCon)
        self._baseCon = i

    def addBaseDex(self, i):
        i += self._baseDex
        i = IntRange.ensure(i, 1, 127)
        self.addDex(i - self._baseDex)
        self._baseDex = i

    def addBaseCha(self, i):
        i += self._baseCha
        i = IntRange.ensure(i, 1, 127)
        self.addCha(i - self._baseCha)
        self._baseCha = i

    def addBaseInt(self, i):
        i += self._baseInt
        i = IntRange.ensure(i, 1, 127)
        self.addInt(i - self._baseInt)
        self._baseInt = i

    def addBaseWis(self, i):
        i += self._baseWis
        i = IntRange.ensure(i, 1, 127)
        self.addWis(i - self._baseWis)
        self._baseWis = i

    def getSimpleBirthday(self):
        dt = datetime.fromtimestamp(self._birthday).date().timetuple()
        return int(time.mktime(dt))

if __name__ == '__main__':
    pc = PcInstance()
    print(pc.__dict__)