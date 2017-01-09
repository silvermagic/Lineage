# -*- coding: utf-8 -*-

class Skills:
    ATTR_NONE = 0
    ATTR_EARTH = 1
    ATTR_FIRE = 2
    ATTR_WATER = 4
    ATTR_WIND = 8
    ATTR_RAY = 16
    TYPE_PROBABILITY = 1
    TYPE_CHANGE = 2
    TYPE_CURSE = 4
    TYPE_DEATH = 8
    TYPE_HEAL = 16
    TYPE_RESTORE = 32
    TYPE_ATTACK = 64
    TYPE_OTHER = 128
    TARGET_TO_ME = 0
    TARGET_TO_PC = 1
    TARGET_TO_NPC = 2
    TARGET_TO_CLAN = 4
    TARGET_TO_PARTY = 8
    TARGET_TO_PET = 16
    TARGET_TO_PLACE = 32

    def __init__(self):
        self._skillId = 0
        self._name = '' # 技能名
        self._skillLevel = 0 # 技能等级: 1~10:法师一到十级魔法 11~12:骑士一到二级魔法 13~14:黑暗精灵一到二级魔法 15:王族一级魔法 17~22:精灵一到六级魔法 23~25:龙骑士一到三级魔法 26~28:幻术师一到三级魔法
        self._skillNumber = 0
        self._mpConsume = 0 # 魔力消耗
        self._hpConsume = 0 # 体力消耗
        self._itmeConsumeId = 0 # 道具消耗
        self._itmeConsumeCount = 0 # 道具消耗个数
        self._reuseDelay = 0
        self._buffDuration = 0 # 效果时长
        self._target = '' # 对象名
        self._targetTo = 0 # 0:自身  1:PC  2:NPC  4:血盟  8:队伍  16:宠物  32:场所
        self._damageValue = 0
        self._damageDice = 0
        self._damageDiceCount = 0
        self._probabilityValue = 0
        self._probabilityDice = 0
        self._attr = 0 # 技能属性  0:无属性魔法  1:地属性魔法  2:火属性魔法  4:水属性魔法  8:风属性魔法  16:光魔法
        self._type = 0 # 技能种类  1:概率型魔法  2:  4:诅咒型魔法  8:死亡型魔法  16:治疗型魔法  32:复活型魔法  64:攻击型魔法  128:其他特殊类型魔法
        self._lawful = 0 # 正义值消耗
        self._ranged = 0 # 技能范围
        self._area = 0 # 技能使用区域
        self._isThrough = False # 技能是否能穿透地形
        self._id = 0
        self._nameId = 0
        self._actionId = 0 # 技能施法动作
        self._castGfx = 0
        self._castGfx2 = 0
        self._sysmsgIdHappen = 0
        self._sysmsgIdStop = 0
        self._sysmsgIdFail = 0