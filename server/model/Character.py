# -*- coding: utf-8 -*-

import threading
from server.model.skill import SkillId
from server.utils.IntRange import IntRange
from Object import Object

class Character(Object):
    def __init__(self):
        Object.__init__(self)
        # 角色属性计算
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
        # 近战/远程伤害加成 近战/远程命中加成 魔法伤害加成 魔法命中加成 魔法暴击加成计算
        self._dmgup = 0
        self._trueDmgup = 0
        self._bowDmgup = 0
        self._trueBowDmgup = 0
        self._hitup = 0
        self._trueHitup = 0
        self._bowHitup = 0
        self._trueBowHitup = 0
        # 防御计算
        self._ac = 0
        self._trueAc = 0
        # 血量魔量计算
        self._currentHp = 0
        self._maxHp = 0
        self._trueMaxHp = 0
        self._currentMp = 0
        self._maxMp = 0
        self._trueMaxMp = 0
        # 魔法防御和魔法攻击计算
        self._mr = 0
        self._trueMr = 0
        self._sp = 0
        self._trueSp = 0
        # 闪避计算
        self._er = 0
        self._trueEr = 0
        # 属性防御、抗性
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
        # 其他属性
        self._level = 1
        self._exp = 0
        self._name = ''
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

    # ============================================================角色力量、敏捷、体质、智力、精神、魅力属性计算============================================================
    def setStr(self, i):
        '''
        更新角色力量属性总值和角色力量属性有效值
        :param i:力量属性总值(int)
        :return:None
        '''
        self._trueStr = i
        self._str = IntRange.ensure(i, 1, 127)

    def addStr(self, i):
        '''
        角色力量属性总值,在角色基础力量属性值变动 装备道具产生力量属性值变动或魔法产生力量属性值变动时会调用此函数更新_trueStr,即_trueStr = 角色基础力量属性值 + 装备奖励的力量属性值 + 魔法奖励的力量属性值
        :param i:变动的力量属性值(int)
        :return:None
        '''
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

    # ==================================近战/远程伤害加成 近战/远程命中加成 魔法伤害加成 魔法命中加成 魔法暴击加成计算==================================
    def addDmgup(self, i):
        '''
        角色伤害近战加成总值,在角色基础近战伤害加成值变动 装备道具产生近战伤害加成值变动或魔法产生近战伤害加成值变动时会调用此函数更新_trueDmgup,即_trueDmgup = 角色基础近战伤害加成值 + 装备奖励的近战伤害加成值 + 魔法奖励的近战伤害加成值
        :param i:变动的近战伤害加成值(int)
        :return:None
        '''
        self._trueDmgup += i
        self._dmgup = IntRange.ensure(self._trueDmgup, -128, 127)

    def addBowDmgup(self, i):
        self._trueBowDmgup += i
        self._bowDmgup = IntRange.ensure(self._trueBowDmgup, -128, 127)

    def addHitup(self, i):
        '''
        角色近战命中加成总值,在角色基础近战命中加成值变动 装备道具产生近战命中加成值变动或魔法产生近战命中加成值变动时会调用此函数更新_trueHitup,即_trueHitup = 角色基础近战命中加成值 + 装备奖励的近战命中加成值 + 魔法奖励的近战命中加成值
        :param i:变动的远程伤害加成值(int)
        :return:None
        '''
        self._trueHitup += i
        self._hitup = IntRange.ensure(self._trueHitup, -128, 127)

    def addBowHitup(self, i):
        self._trueBowHitup += i
        self._bowHitup = IntRange.ensure(self._trueBowHitup, -128, 127)

    # ================================================================防御计算================================================================
    def setAc(self, i):
        '''
        更新角色防御总值和角色力量防御有效值
        :param i:防御总值(int)
        :return:None
        '''
        self._trueAc = i
        self._ac = IntRange.ensure(i, -128, 127)

    def addAc(self, i):
        '''
        角色防御总值,在角色基础防御值变动 角色初始防御值变动 装备道具产生防御值变动或魔法产生防御值变动时会调用此函数更新_trueAc,即_trueAc = 角色基础防御值 + 角色初始防御值 + 装备奖励的防御值 + 魔法奖励的防御值
        :param i:变动的防御值(int)
        :return:None
        '''
        self.setAc(self._trueAc + i)

    # ==============================================================血量魔量计算==============================================================
    def setCurrentHp(self, i):
        '''
        更新角色当前血量值
        :param i:当前血量值(int)
        :return:None
        '''
        if self._currentHp == i:
            return
        self._currentHp = i
        if self._currentHp >= self._maxHp:
            self._currentHp = self._maxHp

    def setMaxHp(self, hp):
        '''
        更新角色血量上限值和角色血量上限有效值以及角色当前血量值
        :param i:血量上限值(int)
        :return:None
        '''
        self._trueMaxHp = hp
        self._maxHp = IntRange.ensure(self._trueMaxHp, 1, 32767)
        self._currentHp = min(self._currentHp, self._maxHp)

    def addMaxHp(self, i):
        '''
        角色血量上限总值,在角色基础血量上限值变动 装备道具产生的血量上限值变动或魔法产生的血量上限值变动时会调用此函数更新_trueMaxHp,即_trueMaxHp = 角色基础血量上限值 + 装备奖励的血量上限值 + 魔法奖励的血量上限值
        :param i:变动的血量上限值(int)
        :return:None
        '''
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

    # ==============================================================魔法防御和魔法攻击计算==============================================================
    def getMr(self):
        '''
        获取魔法防御值,如果角色中了魔法消除,则当前魔防/4
        :return:魔法防御值(int)
        '''
        if self.hasSkillEffect(153):
            return int(self._mr / 4)
        else:
            return self._mr

    def addMr(self, i):
        '''
        角色魔法防御总值,在角色基础魔法防御值变动 角色初始魔法防御值变动 装备道具产生的魔法防御值变动或魔法产生的魔法防御值变动时会调用此函数更新_trueMr,即_trueMr = 角色基础魔法防御值 + 角色初始魔法防御值 + 装备奖励的魔法防御值 + 魔法奖励的魔法防御值
        :param i:变动的魔法防御值(int)
        :return:None
        '''
        self._trueMr += i
        if self._trueMr <= 0:
            self._mr = 0
        else:
            self._mr = self._trueMr

    def addSp(self, i):
        '''
        角色魔法攻击总值,在角色基础魔法攻击值变动 装备道具产生的魔法攻击值变动或魔法产生的魔法攻击值变动时会调用此函数更新_trueSp,即_trueSp = 角色基础魔法攻击值 + 装备奖励的魔法攻击值 + 魔法奖励的魔法攻击值
        :param i:变动的魔法攻击值(int)
        :return:None
        '''
        self._trueSp += i
        if self._trueSp <=0:
            self._sp = 0
        else:
            self._sp = self._trueSp

    # ================================================================闪避计算================================================================
    def getEr(self):
        '''
        获取闪避值,如果角色中了精准目标则闪避值为0
        :return:
        '''
        if self.hasSkillEffect(SkillId.STRIKER_GALE):
            return 0
        else:
            return self._er

    def addEr(self, i):
        '''
        角色闪避总值,在角色基础闪避值变动 角色初始闪避值变动或魔法产生闪避值变动时会调用此函数更新_trueEr,即_trueEr = 角色基础闪避值 + 角色初始闪避值 + 魔法奖励的闪避值
        :param i:变动的闪避值(int)
        :return:None
        '''
        self._trueEr += i
        if self._trueEr <= 0:
            self._er = 0
        else:
            self._er = self._trueEr

    # =================================================================属性防御、抗性=================================================================
    def addWind(self, i):
        '''
        角色风属性防御总值,在装备道具产生的风属性防御值变动或魔法产生的风属性防御值变动时会调用此函数更新_trueWind,即_trueWind = 装备奖励的风属性防御值 + 魔法奖励的风属性防御值
        :param i:变动的风属性防御值(int)
        :return:None
        '''
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
        '''
        角色晕眩抗性值,在装备道具产生的晕眩抗性值变动或魔法产生的晕眩抗性值变动时会调用此函数更新_trueRegistStun,即_trueRegistStun = 装备奖励的晕眩抗性值 + 魔法奖励的晕眩抗性值
        :param i:变动的风属性防御值(int)
        :return:None
        '''
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

    # =================================================================其他属性=================================================================
    def setExp(self, exp):
        self._exp = exp

    def getLevel(self):
        with self._lock:
            return self._level

    def setLevel(self, level):
        with self._lock:
            self._level = int(level)

    def addLawful(self, i) :
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

    def resurrect(self, hp):
        '''
        设置复活后血量
        :param hp: 血量值(int)
        :return: None
        '''
        from server.model.World import World
        if not self._isDead:
            return
        if hp <= 0:
            hp = 1

        self.setCurrentHp(hp)
        self._isDead = False
        self._status = 0
        # todo: 解除变身
        for pc in World().getRecognizePlayer(self):
            pc.sendPackets(S_RemoveObject(self))
            pc.removeKnownObject(self)
            pc.updateObject()

    def removeKnownObject(self, obj):
        self._knownObjects.remove(obj)