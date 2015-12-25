#ifndef L1ITEM_H
#define L1ITEM_H

#include <string>

class L1Item
{
public:
	L1Item();
	virtual ~L1Item();

	virtual int getAc();
	virtual int getBowDmgModifierByArmor();
	virtual int getBowHitModifierByArmor();
	virtual int getCanbedmg();
	virtual int getDamageReduction();
	virtual int getDefenseEarth();
	virtual int getDefenseFire();
	virtual int getDefenseWater();
	virtual int getDefenseWind();
	virtual int getDelayId();
	virtual int getDelayTime();
	virtual int getDmgModifier();
	virtual int getDmgModifierByArmor();
	virtual int getDoubleDmgChance();
	virtual double getExpBonus();
	virtual int getGfxEffect();
	virtual int getGfxEffectTime();
	virtual int getGrade();
	virtual int getHitModifier();
	virtual int getHitModifierByArmor();
	virtual int getLocX();
	virtual int getLocY();
	int getLightFuel();
	int getLightRange();
	virtual int getLuck();
	virtual int getMagicDmgModifier();
	virtual int getMapId();
	virtual int getMaxChargeCount();
	virtual int getObtainProps();
	virtual int getObtainPropsTime();
	virtual int getPolyId();
	virtual int getRange();
	virtual int getRegistBlind();
	virtual int getRegistFreeze();
	virtual int getRegistSleep();
	virtual int getRegistStone();
	virtual int getRegistStun();
	virtual int getRegistSustain();
	virtual int getWeightReduction();
	virtual bool isCanSeal();
	virtual bool isStackable();
	virtual bool isTwohandedWeapon();
public:
	/** 道具的类型.
 *0 L1EtcItem,
 *1 L1Weapon
 *2 L1Armor
 */
	int type2;
	/** 道具的 ClassName. */
	std::string className;
	/** 道具ＩＤ. */
	int itemId;
	/** 道具的名称. */
	std::string name;
	/** 道具的名称ID. */
	std::string nameId;
	/** 道具的名称ＩＤ(未鉴定). */
	std::string unidentifiedNameId;
	/** 道具的名称ＩＤ(已鉴定). */
	std::string identifiedNameId;
	/** 道具的详细类型(共通)
	+道具类型
	*0:arrow 箭
	*1:wand 魔杖
	*2:light 光线 (灯)
	*3:gem 宝物 (金币)
	*4:totem 图腾
	*5:firecracker 烟火
	*6:potion 货币 (名誉货币)
	*7:food 肉
	*8:scroll 卷轴
	*9:questitem 任务物品
	*10:spellbook 魔法书
	*11:petitem 宠物装备
	*12:other 其他
	*13:material 材料
	*14:event 活动物品
	*15:sting 飞刀
	+武器类型
	*1: sword 剑(单手)
	*2: dagger 匕首(单手)
	*3: tohandsword 双手剑(双手)
	*4: bow 弓(双手)
	*5: spear 矛(双手)
	*6: blunt 斧(单手)
	*7: staff 魔杖(单手)
	*8: throwingknife 飞刀
	*9: arrow 箭
	*10: gauntlet 铁手甲
	*11: claw 钢爪(双手)
	*12: edoryu 双刀(双手)
	*13: singlebow 弓(单手)
	*14: singlespear 矛(单手)
	*15: tohandblunt 双手斧(双手)
	*16: tohandstaff 魔杖(双手)
	*17: kiringku 奇古兽(单手)
	*18: chainsword 锁链剑(单手)
	+防具类型
	*1: helm 头盔
	*2: armor 盔甲
	*3: T 内衣
	*4: cloak 斗篷
	*5: glove 手套
	*6: boots 靴子
	*7: shield 盾
	*8: amulet 项链
	*9: ring 戒指
	*10: belt 腰带
	*11: ring2 戒指2
	*12: earring 耳环
	*13: guarder 臂甲
	*14: tattoo_r 辅助装备 (右)
	*15: tattoo_l 辅助装备 (左)
	*16: tattoo_m 辅助装备 (中)
	*/
	int type;
	/**道具的种类(武器).
	+武器类型
	*4 sword: 长剑
	*46 dagger: 匕首
	*50 tohandsword: 双手剑
	*20 bow: 弓
	*11 blunt: 斧(单手)
	*24 spear: 矛(双手)
	*40 staff: 魔杖
	*2922 throwingknife: 飞刀
	*66 arrow: 箭
	*62 gauntlet: 铁手甲
	*58 claw: 钢爪
	*54 edoryu: 双刀
	*20 singlebow: 弓(单手)
	*24 singlespear: 矛(单手)
	*11 tohandblunt: 双手斧
	*40 tohandstaff: 魔杖(双手)
	*58 kiringku: 奇古兽
	*24 chainsword: 锁链剑
	*/
	int type1;
	/**
	* 道具的材质.
	*0 none: 无
	*1 liquid: 液体
	*2 web: 蜡
	*3 vegetation: 植物性
	*4 animalmatter: 动物性
	*5 paper: 纸
	*6 cloth: 布
	*7 leather: 皮
	*8 wood: 木
	*9 bone: 骨头
	*10 dragonscale: 龙鳞
	*11 iron: 铁
	*12 steel: 金属
	*13 copper: 铜
	*14 silver: 银
	*15 gold: 金
	*16 platinum: 白金
	*17 mithril: 米索莉
	*18 blackmithril: 黑色米索莉
	*19 glass: 玻璃
	*20 gemstone: 宝石
	*21 mineral: 矿石
	*22 oriharukon: 奥里哈鲁根
	*/
	int material;
	/** 重量. */
	int weight;
	/** 清单内的图形ＩＤ. */
	int gfxId;
	/** 道具放到地面上的图形ＩＤ. */
	int groundGfxId;
	/** 道具的ItemDesc.tbl信息. */
	int itemDescId;
	/** 能使用装备的最低ＬＶ. */
	int minLevel;
	/** 能使用装备的最高ＬＶ. */
	int maxLevel;
	/** 取得属性. */
	int bless;
	/** 是否可交易. */
	bool isTradable;
	/** 是否删除. */
	bool isCantDelete;
	/** 是否将道具的数量变化写入数据库. */
	bool saveAtOnce;
	/** 最低伤害. */
	int dmgSmall;
	/** 最高伤害. */
	int dmgLarge;
	/** 安定值. */
	int safeEnchant;
	/** 是否为王族可用装备. */
	bool isUseRoyal;
	/** 是否为骑士可用装备. */
	bool isUseKnight;
	/** 是否为精灵可用装备. */
	bool isUseElf;
	/** 是否为法师可用装备. */
	bool isUseMage;
	/** 是否为黑暗妖精可用装备. */
	bool isUseDarkelf;
	/** 是否为龙骑士可用装备. */
	bool isUseDragonknight;
	/** 是否为幻术师可用装备. */
	bool isUseIllusionist;
	/** 增加ＳＴＲ. */
	unsigned char addStr;
	/** 增加ＤＥＸ. */
	unsigned char addDex;
	/** 增加ＣＯＮ. */
	unsigned char addCon;
	/** 增加ＩＮＴ. */
	unsigned char addInt;
	/** 增加ＷＩＳ. */
	unsigned char addWis;
	/** 增加ＣＨＡ. */
	unsigned char addCha;
	/** 增加ＨＰ. */
	int addHp;
	/** 增加ＭＰ. */
	int addMp;
	/** 增加ＨＰＲ. */
	int addHpr;
	/** 增加ＭＰＲ. */
	int addMpr;
	/** 增加ＳＰ. */
	int addSp;
	/** 抗魔(MR). */
	int mdef;
	/** 是否具有加速效果. */
	bool isHasteItem;
	/** 道具可使用时间(能持有的时间). */
	int maxUseTime;
	/**物品使用类型(共通).
 *-15 polyItem: 直接变身类
 *-14 treasure_box: 宝箱类
 *-13 arrow: 箭
 *-12 sting: 飞刀
 *-11 magic_stone_9: 9阶附魔石
 *-10 magic_stone_1_4: 1-4阶附魔石
 *-9 magic_stone_5_6: 5-6阶附魔石
 *-8 magic_stone_7: 7阶附魔石
 *-7 magic_stone_8: 8阶附魔石
 *-6 cooking_books: 料理书
 *-5 potion: 药水类道具
 *-4 none: 无法使用 (材料等)
 *-3 cooking: 料理
 *-2 spellbook: 技能书
 *-1 other: 其他类道具
 *0 normal: 一般物品
 *1 weapon: 武器
 *2 armor: 盔甲
 *5 spell_long: 魔杖类型 (须选取目标/坐标)
 *6 ntele: 瞬间移动卷轴
 *7 identify: 鉴定卷轴
 *8 res: 复活卷轴
 *12 letter: 信纸
 *13 letter_card: 信纸(寄出)
 *14 choice: 请选择一个物品 (道具栏位)
 *15 instrument: 哨子
 *16 sosc: 变形卷轴
 *17 spell_short: 选取目标 (近距离)
 *18 T: T恤
 *19 cloak: 斗篷
 *20 glove: 手套
 *21 boots: 长靴
 *22 helm: 头盔
 *23 ring: 戒指
 *24 amulet: 项链
 *25 shield: 盾牌
 *25 guarder: 臂甲
 *26 dai: 对武器施法的卷轴
 *27 zel: 对盔甲施法的卷轴
 *28 blank: 空的魔法卷轴
 *29 btele: 瞬间移动卷轴 (祝福)
 *30 spell_buff: 选取目标 (对NPC需要Ctrl 远距离 无XY坐标传回)
 *31 ccard: 圣诞卡片
 *32 ccard_w: 圣诞卡片 (寄出)
 *33 vcard: 情人节卡片
 *34 vcard_w: 情人节卡片 (寄出)
 *35 wcard: 白色情人节卡片
 *36 wcard_w: 白色情人节卡片 (寄出)
 *37 belt: 腰带
 *40 earring: 耳环
 *42 fishing_rod: 钓鱼杆
 *43 tattoo_r: 辅助装备 (右)
 *44 tattoo_l: 辅助装备 (左)
 *45 tattoo_m: 辅助装备 (中)
 *46 del: 饰品强化卷轴
 */
	int useType;
	/** 食品类道具饱食度. */
	int foodVolume;
	/** 变身编号:装备武器. */
	int polyIdByWeapon;
};

#endif // L1ITEM_H
