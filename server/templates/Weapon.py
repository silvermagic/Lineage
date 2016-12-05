# -*- coding: utf-8 -*-

from Item import Item

class Weapon(Item):
    def __init__(self):
        Item.__init__(self)
        self._range = 0
        self._hitModifier = 0
        self._dmgModifier = 0
        self._doubleDmgChance = 0
        self._magicDmgModifier = 0
        self._canbedmg = 0

    def getRange(self):
        return self._range

    def getHitModifier(self):
        return self._hitModifier

    def getDmgModifier(self):
        return self._dmgModifier

    def getDoubleDmgChance(self):
        return self._doubleDmgChance

    def getMagicDmgModifier(self):
        return self._magicDmgModifier

    def get_canbedmg(self):
        return self._canbedmg

    def isTwohandedWeapon(self):
        return self._type in (3, 4, 5, 11, 12, 15, 16, 18)