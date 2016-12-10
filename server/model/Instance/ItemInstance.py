# -*- coding: utf-8 -*-

import random
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
            self._chargeCount = 0
            self._remainingTime = 0
            self._bless = 0 # 道具封印状态
        else:
            self._itemId = item._itemId
            self._item = item
            self._chargeCount = item.getMaxChargeCount()
            if self._itemId in (40006, 40007, 40008, 140006, 140008, 41401):
                self._chargeCount -= random.randrange(5)
            if self._itemId == 20383:
                self._chargeCount = 50
            if item._clsType == 0 and item._type == 2: # 蜡烛 灯笼
                self._remainingTime = item.getLightFuel()
            else:
                self._remainingTime = item._maxUseTime
            self._bless = item._bless
        self._remainingTime = 0
        self._isEquipped = False
        self._enchantLevel = 0 # 武卷 防卷强化成功次数
        self._isIdentified = False # 是否已经使用鉴定卷轴鉴定过
        self._durability = 0 # 耐久度(耐久为0则武器装备失效,需要到修理将修理才能使用)
        self._lastUsed = 0
        self._lastWeight = 0
        self._lastStatus = LastStatus(self)
        self._pc = None
        self._isRunning = False
        self._timer = None
        self._attrEnchantKind = 0 # 属性强化类型: 1地 2火 3水 4风
        self._attrEnchantLevel = 0 # 属性强化等级: +4
        # 使用道具模板创建实例后,道具实例经过强化会获得额外的属性加层
        self._FireMr = 0
        self._WaterMr = 0
        self._EarthMr = 0
        self._WindMr = 0
        self._Mpr = 0
        self._Hpr = 0
        self._addHp = 0 # 血量加层
        self._addMp = 0 # 魔量加层
        self._addSp = 0 # 魔功加层
        self._acByMagic = 0
        self._dmgByMagic = 0
        self._holyDmgByMagic = 0
        self._hitByMagic = 0
        self._itemOwnerId = 0
        self._equipmentTimer = None
        self._isNowLighting = False
        self._Pt = False

    def setItem(self, item):
        self._item = item
        self._itemId = item._itemId

    def getMr(self):
        '''
        获取道具魔抗
        :return:道具魔抗(int)
        '''
        mr = self._item._mdef
        itemId = self._item._itemId
        if itemId == 20011 or itemId == 20110 or itemId == 21108 or itemId == 120011: # 抗魔法头盔和抗魔法链甲每次强化成功道具魔抗+1
            mr += self._enchantLevel
        if itemId == 20056 or itemId == 120056 or itemId == 220056: # 抗魔法斗篷每次强化成功道具魔抗+2
            mr += self._enchantLevel * 2

        return mr

    def set_durability(self, i):
        '''
        设置装备耐久性
        :param i:耐久性(int)
        :return:None
        '''
        self._durability = IntRange.ensure(i, 0, 127)

    def getWeight(self):
        '''
        获取道具总重量
        :return:总重量(int)
        '''
        if self._item._weight == 0:
            return 0
        else:
            return max(int(self._count * self._item._weight / 1000), 1)

    def getViewName(self):
        '''
        获取道具在仓库中显示的名字,例如:银箭(2000)
        :return:
        '''
        return self.getNumberedViewName(self._count)

    def getNumberedViewName(self, count):
        '''
        获取道具装备时的显示字符,先获取道具显示的名字然后添加上使用状态字符
        :param count:道具个数(int)
        :return:道具显示名称(str)
        '''
        name = self.getNumberedName(count)
        clsType = self._item._clsType
        Type = self._item._type
        itemId = self._item._itemId

        # todo: 宠物项圈
        if itemId == 40314 or itemId == 40316:
            pass

        if clsType == 0 or Type == 2: # 照明道具
            if self._isNowLighting: # 显示: 使用中
                name += ' ($10)'
            if itemId == 40001 or itemId == 40002: # 灯笼
                if self._remainingTime <= 0: # 显示:
                    name += ' ($11)'

        if self._isEquipped: # 道具使用时显示的字符
            if clsType == 1: # 武器显示: 挥舞
                name += ' ($9)'
            elif clsType == 2: # 装备显示: 使用中
                name += ' ($117)'
            elif clsType == 0 and Type == 1: # 宠物项圈显示: 使用中
                name += ' ($117)'

        return name

    def getLogName(self):
        return self.getNumberedName(self._count)

    def getNumberedName(self, count):
        '''
        获取道具的显示字符
        :param count:个数
        :return:显示名称(str)
        '''
        name = ''

        if self._isIdentified: # 道具是否已经使用鉴定卷轴鉴定过了
            if self._item._clsType == 1: # 武器
                lvl = self._attrEnchantLevel
                if lvl > 0:
                    attrStr = ''
                    if self._attrEnchantKind == 1: # 地属性强化卷轴
                        if lvl == 1:
                            attrStr = '$6124'
                        elif lvl == 2: # 崩裂
                            attrStr = '$6125'
                        elif lvl == 3: # 地灵
                            attrStr = '$6126'
                    elif self._attrEnchantKind == 2: # 火属性强化卷轴
                        if lvl == 1: # 火之
                            attrStr = '$6115'
                        elif lvl == 2: # 爆炎
                            attrStr = '$6116'
                        elif lvl == 3: # 火灵
                            attrStr = '$6117'
                    elif self._attrEnchantKind == 4: # 水属性强化卷轴
                        if lvl == 1: # 水之
                            attrStr = '$6118'
                        elif lvl == 2: # 海啸
                            attrStr = '$6119'
                        elif lvl == 3: # 水灵
                            attrStr = '$6120'
                    elif self._attrEnchantKind == 8: # 风属性强化卷轴
                        if lvl == 1: # 风之
                            attrStr = '$6121'
                        elif lvl == 2: # 暴风
                            attrStr = '$6122'
                        elif lvl == 3: # 风灵
                            attrStr = '$6123'
                    name += attrStr + ' '

            if self._item._clsType == 1 or self._item._clsType == 2:# 武器 防具
                # 显示强化等级(武卷 防卷强化成功次数): +3
                if self._attrEnchantLevel >= 0:
                    name += '+' + str(self._attrEnchantLevel) + ' '
                elif self._attrEnchantLevel < 0:
                    name += str(self._attrEnchantLevel) + ' '

        # 祝福 诅咒 普通
        if self._isIdentified:
            name += self._item._identifiedNameId
        else:
            name += self._item._unidentifiedNameId

        if self._isIdentified:
            if self._item.getMaxChargeCount() > 0:
                name += ' (' + str(self._chargeCount) + ')'
            if self._item._itemId == 20383:
                name += ' (' + str(self._chargeCount) + ')'
            if self._item._maxUseTime > 0 and self._item._clsType != 0: # 武器 防具剩余使用时间
                name += ' (' + str(self._remainingTime) + ')'

        if count > 1:
            name += ' (' + str(count) + ')'

        return name

    def getStatusBytes(self):
        '''
        获取道具状态的二进制描述,用于发送道具封包到客户端
        :return:道具的二进制描述(bytes)
        '''
        clsType = self._item._clsType
        itemId = self._item._itemId
        type = self._item._type
        os = BinaryOutputStream()

        if clsType == 0: # 材料道具
            if type == 2: # 照明系统
                # 照明范围
                os.writeC(22)
                os.writeH(self._item.getLightRange())
            elif type == 7: # 食物
                # 食物提供的饱食度值
                os.writeC(21)
                os.writeH(self._item._foodVolume)
            elif type == 0 or type == 15: # 箭矢
                # 打击值
                os.writeC(1)
                os.writeC(self._item._dmgSmall)
                os.writeC(self._item._dmgLarge)
            else:
                # 材质
                os.writeC(23)
            os.writeC(self._item._material)
            os.writeD(self.getWeight())
        elif clsType == 1 or clsType == 2:
            if clsType == 1: # 武器道具
                # 打击值
                os.writeC(1)
                os.writeC(self._item._dmgSmall)
                os.writeC(self._item._dmgLarge)
                os.writeC(self._item._material)
                os.writeD(self.getWeight())
            elif clsType == 2: # 装备道具
                # 防御值
                os.writeC(19)
                ac = self._item.get_ac()
                if ac < 0:
                    ac = ac - ac - ac
                os.writeH(ac)
                os.writeC(self._item._material)
                os.writeD(self.getWeight())

            if self._enchantLevel != 0:
                # 武器 防具强化次数
                os.writeC(2)
                if clsType == 2 and type in (8, 9, 10, 12):
                    os.writeC(0)
                else:
                    os.writeC(self._enchantLevel)

            if self._durability != 0:
                # 武器 防具耐久度
                os.writeC(3)
                os.writeC(self._durability)

            if self._item.isTwohandedWeapon:
                # 双手武器
                os.writeC(4)

            if clsType == 1:
                if self._item.getHitModifier() != 0:
                    # 近战攻击命中修正
                    os.writeC(5)
                    os.writeC(self._item.getHitModifier())
            elif clsType == 2:
                if self._item.getHitModifierByArmor() != 0:
                    os.writeC(5)
                    os.writeC(self._item.getHitModifierByArmor())

            if clsType == 1:
                if self._item.getDmgModifier() != 0:
                    # 近战攻击伤害加层
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
            # 道具职业使用限制
            os.writeC(7)
            os.writeC(bit)

            if self._item.getBowHitModifierByArmor() != 0:
                # 远距离攻击命中修正
                os.writeC(24)
                os.writeC(self._item.getBowHitModifierByArmor())
            if self._item.getBowDmgModifierByArmor() != 0:
                # 远距离攻击伤害加层
                os.writeC(35)
                os.writeC(self._item.getBowDmgModifierByArmor())

            if itemId in (126, 127): # 玛那魔杖
                # 吸魔
                os.writeC(16)
            if itemId == 262:
                # 吸血
                os.writeC(34)

            if self._item._addstr != 0:
                # 力量属性加层
                os.writeC(8)
                os.writeC(self._item._addstr)
            if self._item._adddex != 0:
                # 敏捷属性加层
                os.writeC(9)
                os.writeC(self._item._adddex)
            if self._item._addcon != 0:
                # 体质属性加层
                os.writeC(10)
                os.writeC(self._item._addcon)
            if self._item._addwis != 0:
                # 精神属性加层
                os.writeC(11)
                os.writeC(self._item._addwis)
            if self._item._addint != 0:
                # 智力属性加层
                os.writeC(12)
                os.writeC(self._item._addint)
            if self._item._addcha != 0:
                # 魅力属性加层
                os.writeC(13)
                os.writeC(self._item._addcha)

            if self._item._isHasteItem:
                # 加速加持
                os.writeC(18)

            if self._item.get_defense_fire() != 0:
                # 火属性防御
                os.writeC(27)
                os.writeC(self._item.get_defense_fire())
            if self._item.get_defense_water != 0:
                # 水属性防御
                os.writeC(28)
                os.writeC(self._item.get_defense_water())
            if self._item.get_defense_wind != 0:
                # 风属性防御
                os.writeC(29)
                os.writeC(self._item.get_defense_wind())
            if self._item.get_defense_earth != 0:
                # 地属性防御
                os.writeC(30)
                os.writeC(self._item.get_defense_earth())

            if self._item._addhp != 0 or self._addHp != 0:
                # 道具模板或道具实例有血量加层
                os.writeC(14)
                os.writeH(self._item._addhp + self._addHp)
            if self._item._addmp != 0 or self._addMp != 0:
                # 魔
                os.writeC(32)
                os.writeH(self._item._addmp + self._addMp)
            if self._item._addsp != 0 or self._addSp != 0:
                # 道具模板或道具实例有魔功加层
                os.writeC(17)
                os.writeH(self._item._addsp + self._addSp)

            if self._item.get_defense_fire() != 0 or self._FireMr != 0:
                # 道具模板或道具实例有火属性防御加层
                os.writeC(27)
                os.writeC(self._item.get_defense_fire() + self._FireMr)
            if self._item.get_defense_water() != 0 or self._WaterMr != 0:
                # 道具模板或道具实例有水属性防御加层
                os.writeC(28)
                os.writeC(self._item.get_defense_water() + self._WaterMr)
            if self._item.get_defense_wind() != 0 or self._WindMr != 0:
                # 道具模板或道具实例有风属性防御加层
                os.writeC(29)
                os.writeC(self._item.get_defense_wind() + self._WindMr)
            if self._item.get_defense_earth() != 0 or self._EarthMr != 0:
                # 道具模板或道具实例有地属性防御加层
                os.writeC(30)
                os.writeC(self._item.get_defense_earth() + self._EarthMr)

            if self._item.get_regist_freeze() != 0:
                # 冻结耐性
                os.writeC(15)
                os.writeC(self._item.get_regist_freeze())
                os.writeC(33)
                os.writeC(1)
            if self._item.get_regist_stone() != 0:
                # 石化耐性
                os.writeC(15)
                os.writeC(self._item.get_regist_stone())
                os.writeC(33)
                os.writeC(2)
            if self._item.get_regist_sleep() != 0:
                # 睡眠耐性
                os.writeC(15)
                os.writeC(self._item.get_regist_sleep())
                os.writeC(33)
                os.writeC(3)
            if self._item.get_regist_blind() != 0:
                # 暗闇耐性
                os.writeC(15)
                os.writeC(self._item.get_regist_blind())
                os.writeC(33)
                os.writeC(4)
            if self._item.get_regist_stun() != 0:
                # 冲晕耐性
                os.writeC(15)
                os.writeC(self._item.get_regist_stun())
                os.writeC(33)
                os.writeC(5)
            if self._item.get_regist_sustain() != 0:
                # 支撑耐性
                os.writeC(15)
                os.writeC(self._item.get_regist_sustain())
                os.writeC(33)
                os.writeC(6)
        return os.getBytes()

    def startEquipmentTimer(self, pc):
        return

    def stopEquipmentTimer(self, pc):
        return

class LastStatus():
    '''
    保存道具实例最近一次存入数据库的值
    '''
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