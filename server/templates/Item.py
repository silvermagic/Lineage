# -*- coding: utf-8 -*-

class Item():
    def __init__(self):
        # 道具类型:0材料道具 1武器道具 2装备道具
        self._clsType = 0
        self._itemId = 0
        self._name = 0
        # 未鉴定和鉴定后的名字标识
        self._unidentifiedNameId = ''
        self._identifiedNameId = ''
        # 道具详细类型
        # [etcitem]
        # 0=arrow	    	1=wand			    2=light					3=gem				4=totem
        # 5=firecracker		6=potion		    7=food					8=scrol				l9=questitem
        # 10=spellbook		11=petitem		    12=other				13=material			14=event
        # 15=sting
        # [weapon]
        # 1=sword			2=dagger		    3=tohandsword			4=bow				5=spear
        # 6=blunt			7=staff			    8=throwingknife		    9=arrow				10=gauntlet
        # 11=claw			12=edoryu		    13=singlebow			14=singlespear		15=tohandblunt
        # 16=tohandstaff	17=kiringku		    18=chainsword
        # [armor]
        # 1=helm			2=armor				3=T						4=cloak				5=glove
        # 6=boots			7=shield			8=amulet				9=ring				10=belt
        # 11=ring2		    12=earring
        self._type = 0
        self._useType = 0
        # 武器类型
        # 4=sword			46=dagger			50=tohandsword			20=bow				11=blunt
        # 24=spear			40=staff			2922=throwingknife	    66=arrow			62=gauntlet
        # 58=claw			54=edoryu			20=singlebow			24=singlespear		11=tohandblunt
        # 40=tohandstaff	58=kiringku			24=chainsword
        self._weaponType = 0
        # 材料类型
        # 0=none			1=液体				2=web					3=植物性				4=動物性
        # 5=紙				6=布					7=皮					    8=木					9=骨
        # 10=龙鳞			11=鉄				12=鋼鉄					13=銅				14=銀
        # 15=金				16=白金				17=秘银					18=黑秘银		    19=玻璃
        # 20=宝石
        self._material = 0
        self._weight = 0
        # 道具在身上和在地面上时的图片标识
        self._gfxId = 0
        self._groundGfxId = 0
        # 装备使用最小最大等级
        self._minLevel = 0
        self._maxLevel = 0
        # 限时道具
        self._itemDescId = 0
        self._bless = 0
        self._tradable = True
        self._cantDelete = True
        # 道具数目发生变化立即写入数据库
        self._save_at_once = False
        # === 材料道具和武器道具通用特性 ===
        # 最小/最大伤害
        self._dmgSmall = 0
        self._dmgLarge = 0
        # === 材料道具和装备道具通用特性 ===
        # === 武器道具和装备道具通用特性 ===
        # 道具强化安定值
        self._safeEnchant = 0
        # 王族是否可以装备
        self._useRoyal = False
        # 骑士是否可以装备
        self._useKnight = False
        # 精灵是否可以装备
        self._useElf = False
        # 法师是否可以装备
        self._useMage = False
        # 黑暗精灵是否可以装备
        self._useDarkelf = False
        # 龙骑士是否可以装备
        self._useDragonknight = False
        # 幻术师是否可以装备
        self._useIllusionist = False
        self._addstr = 0 # 力量属性加层
        self._adddex = 0 # 敏捷属性加层
        self._addcon = 0 # 体质属性加层
        self._addwis = 0 # 精神属性加层
        self._addint = 0 # 智力属性加层
        self._addcha = 0 # 魅力属性加层
        self._addhp = 0
        self._addmp = 0
        self._addhpr = 0
        self._addmpr = 0
        self._addsp = 0
        self._mdef = 0
        self._isHasteItem = False
        self._maxUseTime = 0
        self._foodVolume = 0

    def getLightRange(self):
        '''
        获取道具的照明范围
        :return:照明范围(int)
        '''
        if self._itemId == 40001:
            return 11
        elif self._itemId == 40002:
            return 14
        elif self._itemId == 40004:
            return 14
        elif self._itemId == 40005:
            return 8
        else:
            return 0

    def getLightFuel(self):
        '''
        获取道具照明剩余燃料
        :return:剩余燃料(int)
        '''
        if self._itemId == 40001:
            return 6000
        elif self._itemId == 40002:
            return 12000
        elif self._itemId == 40003:
            return 12000
        elif self._itemId == 40004:
            return 0
        elif self._itemId == 40005:
            return 600
        else:
            return 0

    # === EtcItem特有方法 ===
    def isStackable(self):
        '''
        道具是否可叠加
        :return:True/False
        '''
        return False

    def get_locx(self):
        '''
        道具在游戏世界的x坐标
        :return:x坐标(int)
        '''
        return 0

    def get_locy(self):
        '''
        道具在游戏世界的y坐标
        :return:y坐标(int)y
        '''
        return 0

    def get_mapid(self):
        '''
        道具所属地图ID
        :return:地图ID(int)
        '''
        return 0

    def get_delayid(self):
        return 0

    def get_delaytime(self):
        return 0

    def getMaxChargeCount(self):
        return 0

    def isCanSeal(self):
        return False

    # === Weapon特有方法 ===
    def getRange(self):
        return 0

    def getHitModifier(self):
        '''
        武器命中修正
        :return:命中修正值(int)
        '''
        return 0

    def getDmgModifier(self):
        '''
        武器伤害加层
        :return:伤害加层值(int)
        '''
        return 0

    def getDoubleDmgChance(self):
        '''
        武器双倍伤害概率
        :return:双倍伤害概率(double)
        '''
        return 0

    def getMagicDmgModifier(self):
        '''
        武器魔法伤害加层
        :return:魔法伤害加层值(int)
        '''
        return 0

    def get_canbedmg(self):
        '''
        武器是否能损坏
        :return:
        '''
        return 0

    def isTwohandedWeapon(self):
        '''
        是否为双手武器
        :return:True/False
        '''
        return False

    # === Armor特有方法 ===
    def get_ac(self):
        '''
        获取防具的防御值
        :return:防御值(int)
        '''
        return 0

    def getDamageReduction(self):
        '''
        获取防具的伤害减免
        :return:伤害减免值(int)
        '''
        return 0

    def getWeightReduction(self):
        '''
        获取防具的负重减免
        :return:负重减免值(int)
        '''
        return 0

    def getHitModifierByArmor(self):
        '''
        获取防具的命中修正
        :return:命中修正值(int)
        '''
        return 0

    def getDmgModifierByArmor(self):
        '''
        获取防具的伤害加层
        :return:伤害加层值(int)
        '''
        return 0

    def getBowHitModifierByArmor(self):
        '''
        获取防具对于弓箭的命中修正
        :return:命中修正值(int)
        '''
        return 0

    def getBowDmgModifierByArmor(self):
        '''
        获取防御对于弓箭的伤害加层
        :return:伤害加层值(int)
        '''
        return 0

    def get_defense_water(self):
        '''
        获取防具的水属性防御
        :return:属性防御值(int)
        '''
        return 0

    def get_defense_fire(self):
        '''
        获取防具的火属性防御
        :return:属性防御值(int)
        '''
        return 0

    def get_defense_earth(self):
        '''
        获取防具的土属性防御
        :return:属性防御值(int)
        '''
        return 0

    def get_defense_wind(self):
        '''
        获取防具的风属性防御
        :return:属性防御值(int)
        '''
        return 0

    def get_regist_stun(self):
        '''
        获取防具的冲晕耐性,对冲击之晕的抗性
        :return:冲晕耐性值(int)
        '''
        return 0

    def get_regist_stone(self):
        '''
        获取防具的石化耐性,对大地屏障的抗性
        :return:石化耐性值(int)
        '''
        return 0

    def get_regist_sleep(self):
        '''
        获取防具的睡眠耐性,对沉睡之雾的抗性
        :return:睡眠耐性值(int)
        '''
        return 0

    def get_regist_freeze(self):
        '''
        获取防具的冻结耐性,对木乃伊的诅咒的抗性
        :return:冻结耐性值(int)
        '''
        return 0

    def get_regist_sustain(self):
        '''
        获取防具的支撑耐性
        :return:支撑耐性值(int)
        '''
        return 0

    def get_regist_blind(self):
        '''
        获取防具的暗闇耐性,对闇盲咒术的抗性
        :return:暗闇耐性值(int)
        '''
        return 0