# -*- coding: utf-8 -*-

from server.model.Object import Object
from server.utils.IntRange import IntRange
from server.utils.BinaryOutputStream import BinaryOutputStream

class ItemInstance(Object):
    def __init__(self, item = None, count = 1):
        Object.__init__(self)
        self._count = count
        if not item:
            self._itemId = 0
            self._item = None
        else:
            self._itemId = item._itemId
            self._item = item
        self._isEquipped = False
        self._enchantLevel = 0
        self._isIdentified = False
        self._durability = 0
        self._chargeCount = 0
        self._remainingTime = 0
        self._lastUsed = 0
        self._lastWeight = 0
        self._lastStatus = LastStatus(self)
        self._pc = None
        self._isRunning = False
        self._timer = None
        self._bless = 0
        self._attrEnchantKind = 0
        self._attrEnchantLevel = 0
        self._FireMr = 0
        self._WaterMr = 0
        self._EarthMr = 0
        self._WindMr = 0
        self._Mpr = 0
        self._Hpr = 0
        self._addHp = 0
        self._addMp = 0
        self._addSp = 0
        self._Pt = False
        self._acByMagic = 0
        self._dmgByMagic = 0
        self._holyDmgByMagic = 0
        self._hitByMagic = 0
        self._itemOwnerId = 0
        self._equipmentTimer = None
        self._isNowLighting = False

    def setItem(self, item):
        self._item = item
        self._itemId = item._itemId

    def getMr(self):
        mr = self._item._mdef
        itemId = self._item._itemId
        if itemId == 20011 or itemId == 20110 or itemId == 21108 or itemId == 120011:
            mr += self._enchantLevel

        if itemId == 20056 or itemId == 120056 or itemId == 220056:
            mr += self._enchantLevel * 2

        return mr

    def set_durability(self, i):
        self._durability = IntRange.ensure(i, 0, 127)

    def getWeight(self):
        if self._item._weight == 0:
            return 0
        else:
            return max(int(self._count * self._item._weight / 1000), 1)

    def getViewName(self):
        return self.getNumberedViewName(self._count)

    def getLogName(self):
        return self.getNumberedName(self._count)

    def getNumberedName(self, count):
        name = ''

        if self._isIdentified:
            if self._item._clsType == 1:
                lvl = self._attrEnchantLevel
                if lvl > 0:
                    attrStr = ''
                    if self._attrEnchantKind == 1:
                        if lvl == 1:
                            attrStr = '$6124'
                        elif lvl == 2:
                            attrStr = '$6125'
                        elif lvl == 3:
                            attrStr = '$6126'

                    elif self._attrEnchantKind == 2:
                        if lvl == 1:
                            attrStr = '$6115'
                        elif lvl == 2:
                            attrStr = '$6116'
                        elif lvl == 3:
                            attrStr = '$6117'
                    elif self._attrEnchantKind == 4:
                        if lvl == 1:
                            attrStr = '$6118'
                        elif lvl == 2:
                            attrStr = '$6119'
                        elif lvl == 3:
                            attrStr = '$6120'
                    elif self._attrEnchantKind == 8:
                        if lvl == 1:
                            attrStr = '$6121'
                        elif lvl == 2:
                            attrStr = '$6122'
                        elif lvl == 3:
                            attrStr = '$6123'
                    name += attrStr + ' '
            if self._item._clsType == 1 or self._item._clsType == 2:
                if self._attrEnchantLevel >= 0:
                    name += '+' + str(self._attrEnchantLevel) + ' '
                elif self._attrEnchantLevel < 0:
                    name += str(self._attrEnchantLevel) + ' '

            if self._isIdentified:
                name += self._item._identifiedNameId
            else:
                name += self._item._unidentifiedNameId

        if self._isIdentified:
            if self._item.getMaxChargeCount() > 0:
                name += ' (' + str(self._chargeCount) + ')'
            if self._item._itemId == 20383:
                name += ' (' + str(self._chargeCount) + ')'
            if self._item._maxUseTime > 0 and self._item._clsType != 0:
                name += ' (' + str(self._remainingTime) + ')'

        if count > 1:
            name += ' (' + str(count) + ')'

        return name

    def getNumberedViewName(self, count):
        name = self.getNumberedName(count)
        clsType = self._item._clsType
        itemId = self._item._itemId

        # todo: 宠物项圈
        if itemId == 40314 or itemId == 40316:
            pass

        if clsType == 0 or clsType == 2:
            if self._isNowLighting:
                name += ' ($10)'
            if itemId == 40001 or itemId == 40002:
                if self._remainingTime <= 0:
                    name += ' ($11)'

        if self._isEquipped:
            if clsType == 1:
                name += ' ($9)'
            elif clsType == 2:
                name += ' ($117)'
            elif clsType == 0 and self._item._type == 1:
                name += ' ($117)'

        return name

    def getStatusBytes(self):
        clsType = self._item._clsType
        itemId = self._item._itemId
        type = self._item._type
        os = BinaryOutputStream()

        # 材料道具
        if clsType == 0:
            if type == 2:
                os.writeC(22)
                os.writeH(self._item.getLightRange())
            elif type == 7:
                os.writeC(21)
                os.writeH(self._item._foodVolume)
            elif type == 0 or type == 15:
                os.writeC(1)
                os.writeC(self._item._dmgSmall)
                os.writeC(self._item._dmgLarge)
            else:
                os.writeC(23)
            os.writeC(self._item._material)
            os.writeD(self.getWeight())
        elif clsType == 1 or clsType == 2:
            # 武器道具
            if clsType == 1:
                os.writeC(1)
                os.writeC(self._item._dmgSmall)
                os.writeC(self._item._dmgLarge)
                os.writeC(self._item._material)
                os.writeD(self.getWeight())
            elif clsType == 2:
                os.writeC(19)
                ac = self._item.get_ac()
                if ac < 0:
                    ac = ac - ac - ac
                os.writeH(ac)
                os.writeC(self._item._material)
                os.writeD(self.getWeight())

            if self._enchantLevel != 0:
                os.writeC(2)
                if clsType == 2 and type in (8, 9, 10, 12):
                    os.writeC(0)
                else:
                    os.writeC(self._enchantLevel)

            if self._durability != 0:
                os.writeC(3)
                os.writeC(self._durability)

            if self._item.isTwohandedWeapon:
                os.writeC(4)

            if clsType == 1:
                if self._item.getHitModifier() != 0:
                    os.writeC(5)
                    os.writeC(self._item.getHitModifier())
            elif clsType == 2:
                if self._item.getHitModifierByArmor() != 0:
                    os.writeC(5)
                    os.writeC(self._item.getHitModifierByArmor())

            if clsType == 1:
                if self._item.getDmgModifier() != 0:
                    os.writeC(6)
                    os.writeC(self._item.getDmgModifier())
            elif clsType == 2:
                if self._item.getDmgModifierByArmor() != 0:
                    os.writeC(6)
                    os.writeC(self._item.getDmgModifierByArmor())

            bit = 0
            if self._item._useRoyal:
                bit |= 1
            else:
                bit |= 0
            if self._item._useKnight:
                bit |= 2
            else:
                bit |= 0
            if self._item._useElf:
                bit |= 4
            else:
                bit |= 0
            if self._item._useMage:
                bit |= 8
            else:
                bit |= 0
            if self._item._useDarkelf:
                bit |= 16
            else:
                bit |= 0
            if self._item._useDragonknight:
                bit |= 32
            else:
                bit |= 0
            if self._item._useIllusionist:
                bit |= 64
            else:
                bit |= 0
            os.writeC(7)
            os.writeC(bit)

            if self._item.getBowHitModifierByArmor() != 0:
                os.writeC(24)
                os.writeC(self._item.getBowHitModifierByArmor())
            if self._item.getBowDmgModifierByArmor() != 0:
                os.writeC(35)
                os.writeC(self._item.getBowDmgModifierByArmor())

            if itemId in (126, 127):
                os.writeC(16)
            if itemId == 262:
                os.writeC(34)

            if self._item._addstr != 0:
                os.writeC(8)
                os.writeC(self._item._addstr)
            if self._item._adddex != 0:
                os.writeC(9)
                os.writeC(self._item._adddex)
            if self._item._addcon != 0:
                os.writeC(10)
                os.writeC(self._item._addcon)
            if self._item._addwis != 0:
                os.writeC(11)
                os.writeC(self._item._addwis)
            if self._item._addint != 0:
                os.writeC(12)
                os.writeC(self._item._addint)
            if self._item._addcha != 0:
                os.writeC(13)
                os.writeC(self._item._addcha)

            if self._item._isHasteItem:
                os.writeC(18)

            '''
            if self._item.get_defense_fire() != 0:
                os.writeC(27)
                os.writeC(self._item.get_defense_fire())
            if self._item.get_defense_water != 0:
                os.writeC(28)
                os.writeC(self._item.get_defense_water())
            if self._item.get_defense_wind != 0:
                os.writeC(29)
                os.writeC(self._item.get_defense_wind())
            if self._item.get_defense_earth != 0:
                os.writeC(30)
                os.writeC(self._item.get_defense_earth())
            '''
            if self._item._addhp != 0 or self._addHp != 0:
                os.writeC(14)
                os.writeH(self._item._addhp + self._addHp)
            if self._item._addmp != 0 or self._addMp != 0:
                os.writeC(32)
                os.writeH(self._item._addmp + self._addMp)
            if self._item._addsp != 0 or self._addSp != 0:
                os.writeC(17)
                os.writeH(self._item._addsp + self._addSp)

            if self._item.get_defense_fire() != 0 or self._FireMr != 0:
                os.writeC(27)
                os.writeC(self._item.get_defense_fire() + self._FireMr)
            if self._item.get_defense_water() != 0 or self._WaterMr != 0:
                os.writeC(28)
                os.writeC(self._item.get_defense_water() + self._WaterMr)
            if self._item.get_defense_wind() != 0 or self._WindMr != 0:
                os.writeC(29)
                os.writeC(self._item.get_defense_wind() + self._WindMr)
            if self._item.get_defense_earth() != 0 or self._EarthMr != 0:
                os.writeC(30)
                os.writeC(self._item.get_defense_earth() + self._EarthMr)

            if self._item.get_regist_freeze() != 0:
                os.writeC(15)
                os.writeC(self._item.get_regist_freeze())
                os.writeC(33)
                os.writeC(1)
            if self._item.get_regist_stone() != 0:
                os.writeC(15)
                os.writeC(self._item.get_regist_stone())
                os.writeC(33)
                os.writeC(2)
            if self._item.get_regist_sleep() != 0:
                os.writeC(15)
                os.writeC(self._item.get_regist_sleep())
                os.writeC(33)
                os.writeC(3)
            if self._item.get_regist_blind() != 0:
                os.writeC(15)
                os.writeC(self._item.get_regist_blind())
                os.writeC(33)
                os.writeC(4)
            if self._item.get_regist_stun() != 0:
                os.writeC(15)
                os.writeC(self._item.get_regist_stun())
                os.writeC(33)
                os.writeC(5)
            if self._item.get_regist_sustain() != 0:
                os.writeC(15)
                os.writeC(self._item.get_regist_sustain())
                os.writeC(33)
                os.writeC(6)
        return os.getBytes()

class LastStatus():
    def __init__(self, inst):
        self._inst = inst
        self.count = 0
        self.isEquipped = False
        self.isIdentified = True
        self.enchantLevel = 0
        self.durability = 0
        self.chargeCount = 0
        self.remainingTime = 0
        self.lastUsed = 0
        self.bless = 0
        self.attrEnchantKind = 0
        self.attrEnchantLevel = 0
        self.firemr = 0
        self.watermr = 0
        self.earthmr = 0
        self.windmr = 0
        self.addhp = 0
        self.addmp = 0
        self.addsp = 0
        self.hpr = 0
        self.mpr = 0

    def updateAll(self):
        self.count = self._inst._count
        self.isEquipped = self._inst._isEquipped
        self.isIdentified = self._inst._isIdentified
        self.enchantLevel = self._inst._enchantLevel
        self.durability = self._inst._durability
        self.chargeCount = self._inst._chargeCount
        self.remainingTime = self._inst._remainingTime
        self.lastUsed = self._inst._lastUsed
        self.bless = self._inst._bless
        self.attrEnchantKind = self._inst._attrEnchantKind
        self.attrEnchantLevel = self._inst._attrEnchantLevel
        self.firemr = self._inst._FireMr
        self.watermr = self._inst._WaterMr
        self.earthmr = self._inst._EarthMr
        self.windmr = self._inst._WindMr
        self.addhp = self._inst._addSp
        self.addmp = self._inst._addHp
        self.addsp = self._inst._addMp
        self.hpr = self._inst._Hpr
        self.mpr = self._inst._Mpr