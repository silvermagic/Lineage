#include "templates/L1Item.h"

L1Item::L1Item()
{
	isUseRoyal = false;
	isUseKnight = false;
	isUseElf = false;
	isUseMage = false;
	isUseDarkelf = false;
	isUseDragonknight = false;
	isUseIllusionist = false;
	addStr = 0;
	addDex = 0;
	addCon = 0;
	addInt = 0;
	addWis = 0;
	addCha = 0;
	addHp = 0;
	addMp = 0;
	addHpr = 0;
	addMpr = 0;
	addSp = 0;
	mdef = 0;
	isHasteItem = false;
	maxUseTime = 0;
}

L1Item::~L1Item()
{
}

/**
 * 取得物理防御.
 *
 * @return 值(被L1Armor覆盖)
 */
int L1Item::getAc()
{
	return 0;
}

/**
 * 取得弓类装备的伤害修正.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getBowDmgModifierByArmor()
{
	return 0;
}

/**
    * 取得弓类装备的命中修正.
    *
    * @return 值 (会被L1Armor覆盖)
    */
int L1Item::getBowHitModifierByArmor()
{
	return 0;
}

/**
 * 取得有无损伤.
 *
 * @return 值(被L1Weapon覆盖)
 */
int L1Item::getCanbedmg()
{
	return 0;
}

/**
 * 取得伤害减免.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getDamageReduction()
{
	return 0;
}

/**
 * 取得地属性防御.
 *
 * @return 值(被L1Armor覆盖)
 */
int L1Item::getDefenseEarth()
{
	return 0;
}

/**
 * 取得火属性防御.
 *
 * @return 值(被L1Armor覆盖)
 */
int L1Item::getDefenseFire()
{
	return 0;
}

/**
 * 取得水属性防御.
 *
 * @return 值(被L1Armor覆盖)
 */
int L1Item::getDefenseWater()
{
	return 0;
}

/**
 * 取得风属性防御.
 *
 * @return 值(被L1Armor覆盖)
 */
int L1Item::getDefenseWind()
{
	return 0;
}

/**
 * 取得延迟编号.
 *
 * @return 值 (会被L1EtcItem覆盖)
 */
int L1Item::getDelayId()
{
	return 0;
}

/**
 * 取得延迟时间.
 *
 * @return 值 (会被L1EtcItem覆盖)
 */
int L1Item::getDelayTime()
{
	return 0;
}

/**
 * 取得伤害修正.
 *
 * @return 值 (会被L1Weapon覆盖)
 */
int L1Item::getDmgModifier()
{
	return 0;
}

/**
 * 取得装备的伤害修正.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getDmgModifierByArmor()
{
	return 0;
}

/**
 * 取得双倍伤害发动几率.
 *
 * @return 值 (会被L1Weapon覆盖)
 */
int L1Item::getDoubleDmgChance()
{
	return 0;
}
/**
 * 取得经验值加成.
 *
 * @return 值 (会被L1Armor覆盖)
 */
double L1Item::getExpBonus()
{
	return 0;
}

/**
 * 取得动画效果(一般防具).
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getGfxEffect()
{
	return 0;
}

/**
 * 取得动画效果时间(单位:秒).
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getGfxEffectTime()
{
	return 0;
}

/**
 * 取得饰品强化等级.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getGrade()
{
	return 0;
}

/**
 * 取得命中率修正.
 *
 * @return 值 (会被L1Weapon覆盖)
 */
int L1Item::getHitModifier()
{
	return 0;
}

/**
 * 取得装备的命中修正.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getHitModifierByArmor()
{
	return 0;
}

/**
 * 取得照明类道具的燃料量.
 *
 * @return 燃料量
 */
int L1Item::getLightFuel()
{
	if (itemId == 40001)   // 灯
	{
		return 6000;
	}
	else if (itemId == 40002)     // 灯笼
	{
		return 12000;
	}
	else if (itemId == 40003)     // 灯油
	{
		return 12000;
	}
	else if (itemId == 40004)     // 魔法灯笼
	{
		return 0;
	}
	else if (itemId == 40005)     // 蜡烛
	{
		return 600;
	}
	else
	{
		return 0;
	}
}

/**
 * 取得照明类道具的亮度设置.
 *
 * @return 亮度
 */
int L1Item::getLightRange()
{
	if (itemId == 40001)   // 灯
	{
		return 11;
	}
	else if (itemId == 40002)     // 灯笼
	{
		return 14;
	}
	else if (itemId == 40004)     // 魔法灯笼
	{
		return 14;
	}
	else if (itemId == 40005)     // 蜡烛
	{
		return 8;
	}
	else
	{
		return 0;
	}
}

/**
 * 取得X坐标.
 *
 * @return 值 (会被L1EtcItem覆盖)
 */
int L1Item::getLocX()
{
	return 0;
}

/**
 * 取得Y坐标.
 *
 * @return 值 (会被L1EtcItem覆盖)
 */
int L1Item::getLocY()
{
	return 0;
}

/**
 * 取得幸运值.
 *
 * @return (会被L1Armor覆盖)
 */
int L1Item::getLuck()
{
	return 0;
}

/**
 * 取得魔法攻击的伤害修正.
 *
 * @return 值 (会被L1Weapon覆盖)
 */
int L1Item::getMagicDmgModifier()
{
	return 0;
}

/**
 * 取得地图ID.
 *
 * @return 值 (会被L1EtcItem覆盖)
 */
int L1Item::getMapId()
{
	return 0;
}

/**
 * 取得最大可用次数.
 *
 * @return 值(会被L1EtcItem覆盖)
 */
int L1Item::getMaxChargeCount()
{
	return 0;
}

/**
 * 取得获得的道具编号(一般防具).
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getObtainProps()
{
	return 0;
}

/**
 * 取得获得特定道具的时间(单位:秒).
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getObtainPropsTime()
{
	return 0;
}

/**
 * 取得变身编号(防具).
 *
 * @return 值(会被L1Armor覆盖)
 */
int L1Item::getPolyId()
{
	return 0;
}

/**
 * 取得武器的射程范围.
 *
 * @return 值(会被L1Weapon覆盖)
 */
int L1Item::getRange()
{
	return 0;
}

/**
 * 取得暗闇耐性.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getRegistBlind()
{
	return 0;
}

/**
 * 取得寒冰耐性.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getRegistFreeze()
{
	return 0;
}

/**
 * 取得睡眠耐性.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getRegistSleep()
{
	return 0;
}

/**
 * 取得石化耐性.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getRegistStone()
{
	return 0;
}

/**
 * 取得昏迷耐性.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getRegistStun()
{
	return 0;
}

/**
 * 取得支撑耐性.
 *
 * @return 值 (会被L1Armor覆盖)
 */
int L1Item::getRegistSustain()
{
	return 0;
}

/**
 * 取得负重减轻.
 *
 * @return 值(会被L1Armor覆盖)
 */
int L1Item::getWeightReduction()
{
	return 0;
}

/**
 * 是否封印.
 *
 * @return 值(会被L1EtcItem覆盖)
 */
bool L1Item::isCanSeal()
{
	return false;
}

/**
 * 是否可堆叠物品.
 *
 * @return 值(会被L1EtcItem覆盖)
 */
bool L1Item::isStackable()
{
	return false;
}

/**
 * 是否双手武器.
 *
 * @return 值(会被L1Weapon覆盖)
 */
bool L1Item::isTwohandedWeapon()
{
	return false;
}
