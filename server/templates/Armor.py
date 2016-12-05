# -*- coding: utf-8 -*-

from Item import Item

class Armor(Item):
    def __init__(self):
        Item.__init__(self)
        self._ac = 0
        self._damageReduction = 0
        self._weightReduction = 0
        self._hitModifierByArmor = 0
        self._dmgModifierByArmor = 0
        self._bowHitModifierByArmor = 0
        self._bowDmgModifierByArmor = 0
        self._defense_water = 0
        self._defense_wind = 0
        self._defense_fire = 0
        self._defense_earth = 0
        self._regist_stun = 0
        self._regist_stone = 0
        self._regist_sleep = 0
        self._regist_freeze = 0
        self._regist_sustain = 0
        self._regist_blind = 0

    def get_ac(self):
        return self._ac

    def getDamageReduction(self):
        return self._damageReduction

    def getWeightReduction(self):
        return self._weightReduction

    def getHitModifierByArmor(self):
        return self._hitModifierByArmor

    def getDmgModifierByArmor(self):
        return self._dmgModifierByArmor

    def getBowHitModifierByArmor(self):
        return self._bowHitModifierByArmor

    def getBowDmgModifierByArmor(self):
        return self._bowDmgModifierByArmor

    def get_defense_water(self):
        return self._defense_water

    def get_defense_fire(self):
        return self._defense_fire

    def get_defense_earth(self):
        return self._defense_earth

    def get_defense_wind(self):
        return self._defense_wind

    def get_regist_stun(self):
        return self._regist_stun

    def get_regist_stone(self):
        return self._regist_stone

    def get_regist_sleep(self):
        return self._regist_sleep

    def get_regist_freeze(self):
        return self._regist_freeze

    def get_regist_sustain(self):
        return self._regist_sustain

    def get_regist_blind(self):
        return self._regist_blind