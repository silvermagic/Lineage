#include <iostream>
#include <fstream>
#include <boost/program_options.hpp>
#include "utils/TIntRange.h"
#include "configure/TConfig.h"

using namespace boost::program_options;

/** 服务器配置文件路径. */
std::string TConfig::SERVER = "./config/服务器设置.properties";
/** 数据库配置文件路径. */
std::string TConfig::SQL = "./config/sql.properties";
/** 倍率配置文件路径. */
std::string TConfig::RATES = "./config/倍率设置.properties";
/** 进阶配置文件路径. */
std::string TConfig::ALT = "./config/进阶设置.properties";
/** 角色配置文件路径. */
std::string TConfig::CHAR = "./config/角色设置.properties";
/** 战斗特化配置文件路径. */
std::string TConfig::FIGHT = "./config/战斗特化设置.properties";
/** 纪录配置文件路径. */
std::string TConfig::RECORD = "./config/记录设置.properties";
/** 其他配置文件路径. */
std::string TConfig::OTHER = "./config/其他设置.properties";
/** 调整测试配置文件路径. */
std::string TConfig::CHECK = "./config/调整测试设置.properties";
/** 字符编码格式 */
const std::string TConfig::LANGUAGE_CODE_ARRAY[] = {"UTF8", "EUCKR", "UTF8", "BIG5", "SJIS", "GBK"};

TConfig::TConfig() : MANA_DRAIN_LIMIT_PER_NPC(40), MANA_DRAIN_LIMIT_PER_SOM_ATTACK(9)
{
}

TConfig::~TConfig()
{
}

void TConfig::load()
{
  options_description opts;
  opts.add_options()
  ("Lock", value<bool>(&CHECK_LOCK)->default_value(false), "调试:是否开启检测回溯")
  ("Packets", value<bool>(&PACKETS)->default_value(false), "调试:是否开启封包发送错误提示")
  ("isBugBearRace", value<bool>(&BUG_BEAR_RACE)->default_value(false), "调试:是否开启奇岩 食人妖精竞赛")
  ("DebugMode", value<bool>(&DEBUG)->default_value(false), "调试/侦错模式")
  ("PrintPacket", value<bool>(&PACKET)->default_value(false), "控制台是否显示封包")
  ("GeneralThreadPoolType", value<int>(&THREAD_P_TYPE_GENERAL)->default_value(0))
  ("GeneralThreadPoolSize", value<int>(&THREAD_P_SIZE_GENERAL)->default_value(0))
  ("GameserverHostname", value<std::string>(&GAME_SERVER_HOST_NAME)->default_value("*"), "服务器主机(IP)")
  ("GameserverPort", value<int>(&GAME_SERVER_PORT)->default_value(2000), "服务器端口")
  ("TimeZone", value<std::string>(&TIME_ZONE)->default_value("Etc/GMT+8"), "时区设置")
  ("ClientLanguage", value<int>(&CLIENT_LANGUAGE)->default_value(5), "客户端语系")
  ("HostnameLookups", value<bool>(&HOSTNAME_LOOKUPS)->default_value(false), "DNS反向验证")
  ("AutomaticKick", value<int>(&AUTOMATIC_KICK)->default_value(10), "客户端无动作时自动断线时间")
  ("AutoCreateAccounts", value<bool>(&AUTO_CREATE_ACCOUNTS)->default_value(false), "自动创建帐号")
  ("MaximumOnlineUsers", value<int>(&MAX_ONLINE_USERS)->default_value(30), "最高在线玩家数量")
  ("CacheMapFiles", value<bool>(&CACHE_MAP_FILES)->default_value(false), "生成地图快取档案")
  ("LoadV2MapFiles", value<bool>(&LOAD_V2_MAP_FILES)->default_value(false), "V2地图 (测试用)")
  ("CheckMoveInterval", value<bool>(&CHECK_MOVE_INTERVAL)->default_value(false), "加速器侦测 (移动间隔)")
  ("CheckAttackInterval", value<bool>(&CHECK_ATTACK_INTERVAL)->default_value(false), "加速器侦测 (攻击间隔)")
  ("CheckSpellInterval", value<bool>(&CHECK_SPELL_INTERVAL)->default_value(false), "加速器侦测 (技能使用间隔)")
  ("InjusticeCount", value<int>(&INJUSTICE_COUNT)->default_value(10), "设定不正常封包数值,满足条件则切断连线")
  ("JusticeCount", value<int>(&JUSTICE_COUNT)->default_value(4), "设定如果参杂正常封包在不正常封包中,数值满足时InjusticeCount归0")
  ("CheckStrictness", value<int>(&CHECK_STRICTNESS)->default_value(102), "加速器检查严密度")
  ("Punishment", value<int>(&ILLEGAL_SPEEDUP_PUNISHMENT)->default_value(0), "加速处罚机制")
  ("AutosaveInterval", value<int>(&AUTOSAVE_INTERVAL)->default_value(1200), "伺服器自动存档时间间隔 (单位: 秒)")
  ("AutosaveIntervalOfInventory", value<int>(&AUTOSAVE_INTERVAL_INVENTORY)->default_value(300), "定时自动储存角色装备资料时间间隔 (单位: 秒)")
  ("SkillTimerImplType", value<int>(&SKILLTIMER_IMPLTYPE)->default_value(1), "技能计数器实施类型")
  ("NpcAIImplType", value<int>(&NPCAI_IMPLTYPE)->default_value(1), "NpcAI的实施类型")
  ("TelnetServer", value<bool>(&TELNET_SERVER)->default_value(false), "远程登录控制伺服器")
  ("TelnetServerPort", value<int>(&TELNET_SERVER_PORT)->default_value(23), "远程控制的Port号码")
  ("PcRecognizeRange", value<int>(&PC_RECOGNIZE_RANGE)->default_value(20), "发送到一个范围的信息给客户端对像")
  ("CharacterConfigInServerSide", value<bool>(&CHARACTER_CONFIG_IN_SERVER_SIDE)->default_value(false), "人物资讯统一管理(F5~12快捷键和人物血条位置等)")
  ("Allow2PC", value<bool>(&ALLOW_2PC)->default_value(false), "双开(同IP同时连线)")
  ("LevelDownRange", value<int>(&LEVEL_DOWN_RANGE)->default_value(0), "允许降等的水平范围（检测死亡降等范围）")
  ("SendPacketBeforeTeleport", value<bool>(&SEND_PACKET_BEFORE_TELEPORT)->default_value(false), "瞬移控制")
  ("CmdActive", value<bool>(&CMD_ACTIVE)->default_value(false), "CMD互动指令")
  ("AnnouncementsCycleTime", value<int>(&Announcements_Cycle_Time)->default_value(30), "循环时间设置 (单位:分钟)")
  ("AnnounceTimeDisplay", value<bool>(&Announcements_Cycle_Modify_Time)->default_value(false), "自动显示公告修改时间")
  ("Driver", value<std::string>(&DB_DRIVER)->default_value("com.mysql.jdbc.Driver"), "数据库驱动程序")
  ("URL", value<std::string>(&DB_URL)->default_value("jdbc:mysql://localhost/l1jdb?useUnicode=true&characterEncoding=utf8"), "数据库路径")
  ("Login", value<std::string>(&DB_LOGIN)->default_value("root"), "数据库账号")
  ("Password", value<std::string>(&DB_PASSWORD)->default_value("root"), "数据库密码")
  ("EnableDatabaseResourceLeaksDetection", value<bool>(&DETECT_DB_RESOURCE_LEAKS)->default_value(false), "数据库资源泄漏检测")
  ("MysqlAutoBackup", value<int>(&MYSQL_AUTO_BACKUP)->default_value(0), "MySQL定时自动备份")
  ("CompressGzip", value<bool>(&COMPRESS_G_ZIP)->default_value(false), "备份的输出SQL是否启用GZip压缩")
  ("RateXp", value<double>(&RATE_XP)->default_value(1.0), "经验值倍率")
  ("RateLawful", value<double>(&RATE_LA)->default_value(1.0), "正义值倍率")
  ("RateKarma", value<double>(&RATE_KARMA)->default_value(1.0), "友好度倍率")
  ("RateDropAdena", value<double>(&RATE_DROP_ADENA)->default_value(1.0), "掉落金钱倍率")
  ("RateDropItems", value<double>(&RATE_DROP_ITEMS)->default_value(1.0), "掉落物品倍率")
  ("EnchantChanceWeapon", value<int>(&ENCHANT_CHANCE_WEAPON)->default_value(1.0), "冲武器成功率")
  ("EnchantChanceArmor", value<int>(&ENCHANT_CHANCE_ARMOR)->default_value(1.0), "冲防具成功率")
  ("AttrEnchantChance", value<int>(&ATTR_ENCHANT_CHANCE)->default_value(1.0), "属性强化成功率")
  ("RateWeightLimit", value<double>(&RATE_WEIGHT_LIMIT)->default_value(1.0), "角色负重倍率")
  ("RateWeightLimitforPet", value<double>(&RATE_WEIGHT_LIMIT_PET)->default_value(1.0), "宠物负重倍率")
  ("RateShopSellingPrice", value<double>(&RATE_SHOP_SELLING_PRICE)->default_value(1.0), "商店贩卖价格倍率")
  ("RateShopPurchasingPrice", value<double>(&RATE_SHOP_PURCHASING_PRICE)->default_value(1.0), "商店收购价格倍率")
  ("CreateChanceDiary", value<int>(&CREATE_CHANCE_DIARY)->default_value(33), "航海日志合成几率")
  ("CreateChanceRecollection", value<int>(&CREATE_CHANCE_RECOLLECTION)->default_value(90), "净化的部分")
  ("CreateChanceMysterious", value<int>(&CREATE_CHANCE_MYSTERIOUS)->default_value(90), "神秘药水")
  ("CreateChanceProcessing", value<int>(&CREATE_CHANCE_PROCESSING)->default_value(90), "被加工了的宝石")
  ("CreateChanceProcessingDiamond", value<int>(&CREATE_CHANCE_PROCESSING_DIAMOND)->default_value(90), "被加工了的钻石")
  ("CreateChanceDantes", value<int>(&CREATE_CHANCE_DANTES)->default_value(50), "完整的召唤球")
  ("CreateChanceAncientAmulet", value<int>(&CREATE_CHANCE_ANCIENT_AMULET)->default_value(90), "不起眼的古老项链")
  ("CreateChanceHistory", value<int>(&CREATE_CHANCE_HISTORY_BOOK)->default_value(50), "封印的历史书")
  ("MagicStoneAttr", value<int>(&MAGIC_STONE_TYPE)->default_value(50), "附魔石类型")
  ("MagicStoneLevel", value<int>(&MAGIC_STONE_LEVEL)->default_value(50), "附魔石阶级")
  ("GlobalChatLevel", value<int>(&GLOBAL_CHAT_LEVEL)->default_value(30), "全体聊天最低等级限制")
  ("WhisperChatLevel", value<int>(&WHISPER_CHAT_LEVEL)->default_value(5), "密语最低等级限制")
  ("AutoLoot", value<int>(&AUTO_LOOT)->default_value(2), "自动取得道具的方式")
  ("LootingRange", value<int>(&LOOTING_RANGE)->default_value(3), "道具掉落的范围大小")
  ("NonPvP", value<bool>(&ALT_NONPVP)->default_value(false), "Non-PvP设定")
  ("AttackMessageOn", value<bool>(&ALT_ATKMSG)->default_value(false), "GM是否显示伤害讯息")
  ("ChangeTitleByOneself", value<bool>(&CHANGE_TITLE_BY_ONESELF)->default_value(false), "自己更改称号")
  ("MaxClanMember", value<int>(&MAX_CLAN_MEMBER)->default_value(0), "血盟人数上限")
  ("ClanAlliance", value<bool>(&CLAN_ALLIANCE)->default_value(false), "血盟联盟系统")
  ("MaxPT", value<int>(&MAX_PT)->default_value(8), "组队人数上限")
  ("MaxChatPT", value<int>(&MAX_CHAT_PT)->default_value(8), "组队聊天人数上限")
  ("SimWarPenalty", value<bool>(&SIM_WAR_PENALTY)->default_value(false), "攻城战中红人死亡后是否会受到处罚")
  ("GetBack", value<bool>(&GET_BACK)->default_value(false), "重新登入时是否在出生地")
  ("ItemDeletionType", value<std::string>(&ALT_ITEM_DELETION_TYPE)->default_value("auto"), "地图上地面道具删除设置")
  ("ItemDeletionTime", value<int>(&ALT_ITEM_DELETION_TIME)->default_value(30), "物品在地面自动清除掉的时间")
  ("ItemDeletionRange", value<int>(&ALT_ITEM_DELETION_RANGE)->default_value(5), "人物周围不清除物品范围大小")
  ("GMshop", value<bool>(&ALT_GMSHOP)->default_value(false), "是否开启GM商店")
  ("GMshopMinID", value<int>(&ALT_GMSHOP_MIN_ID)->default_value(0xffffffff), "GM商店编号最小值")
  ("GMshopMaxID", value<int>(&ALT_GMSHOP_MAX_ID)->default_value(0xffffffff), "GM商店编号最大值")
  ("HalloweenIvent", value<bool>(&ALT_HALLOWEENIVENT)->default_value(false), "南瓜怪任务开关")
  ("TalkingScrollQuest", value<bool>(&ALT_TALKINGSCROLLQUEST)->default_value(false), "日本特典道具NPC开关")
  ("JpPrivileged", value<bool>(&ALT_JPPRIVILEGED)->default_value(false), "说话卷轴任务开关")
  ("WhoCommand", value<bool>(&ALT_WHO_COMMAND)->default_value(false), "/who 指令是否可以使用")
  ("RevivalPotion", value<bool>(&ALT_REVIVAL_POTION)->default_value(false), "99级是否可以获得返生药水")
  //("WarTime", value<int>()->default_value(2), "攻城战时间")
  //("WarTime", value<int>()->default_value(2), "攻城战时间单位")
  //("WarInterval", value<int>()->default_value(4), "攻城日的间隔")
  //("WarInterval", value<int>()->default_value(4), "攻城日的间隔单位")
  ("SpawnHomePoint", value<bool>(&SPAWN_HOME_POINT)->default_value(false), "范围性怪物刷新")
  ("SpawnHomePointRange", value<int>(&SPAWN_HOME_POINT_RANGE)->default_value(8), "怪物刷新的范围大小")
  ("SpawnHomePointCount", value<int>(&SPAWN_HOME_POINT_COUNT)->default_value(2), "怪物出生点设定最小")
  ("SpawnHomePointDelay", value<int>(&SPAWN_HOME_POINT_DELAY)->default_value(100), "怪物出生点设定的最大")
  ("InitBossSpawn", value<bool>(&INIT_BOSS_SPAWN)->default_value(false), "服务器启动时Boss是否出现")
  ("ElementalStoneAmount", value<int>(&ELEMENTAL_STONE_AMOUNT)->default_value(300), "妖精森林元素石的数量")
  ("HouseTaxInterval", value<int>(&HOUSE_TAX_INTERVAL)->default_value(10), "盟屋税金的支付期限(日)")
  ("MaxDollCount", value<int>(&MAX_DOLL_COUNT)->default_value(1), "魔法娃娃召唤数量上限")
  ("ReturnToNature", value<bool>(&RETURN_TO_NATURE)->default_value(false), "释放元素技能的使用")
  ("MaxNpcItem", value<int>(&MAX_NPC_ITEM)->default_value(8), "NPC(召唤, 宠物)身上可以持有的最大物品数量")
  ("MaxPersonalWarehouseItem", value<int>(&MAX_PERSONAL_WAREHOUSE_ITEM)->default_value(150), "个人仓库物品上限数量")
  ("MaxClanWarehouseItem", value<int>(&MAX_CLAN_WAREHOUSE_ITEM)->default_value(200), "血盟仓库物品上限数量")
  ("DeleteCharacterAfter7Days", value<bool>(&DELETE_CHARACTER_AFTER_7DAYS)->default_value(false), "角色等级30以上，删除角色是否要等待7天")
  ("NpcDeletionTime", value<int>(&NPC_DELETION_TIME)->default_value(10), "NPC死亡后尸体消失时间（秒）")
  ("DefaultCharacterSlot", value<int>(&DEFAULT_CHARACTER_SLOT)->default_value(false), "预设角色数量")
  ("GDropItemTime", value<int>(&GDROPITEM_TIME)->default_value(10), "妖精森林NPC道具重置时间")
  ("PrinceMaxHP", value<int>(&PRINCE_MAX_HP)->default_value(1000), "王族HP上限")
  ("PrinceMaxMP", value<int>(&PRINCE_MAX_MP)->default_value(800), "王族MP上限")
  ("KnightMaxHP", value<int>(&KNIGHT_MAX_HP)->default_value(1400), "骑士HP上限")
  ("KnightMaxMP", value<int>(&KNIGHT_MAX_MP)->default_value(600), "骑士MP上限")
  ("ElfMaxHP", value<int>(&ELF_MAX_HP)->default_value(1000), "精灵HP上限")
  ("ElfMaxMP", value<int>(&ELF_MAX_MP)->default_value(900), "精灵MP上限")
  ("WizardMaxHP", value<int>(&WIZARD_MAX_HP)->default_value(800), "法师HP上限")
  ("WizardMaxMP", value<int>(&WIZARD_MAX_MP)->default_value(1200), "法师MP上限")
  ("DarkelfMaxHP", value<int>(&DARKELF_MAX_HP)->default_value(1000), "黑暗精灵HP上限")
  ("DarkelfMaxMP", value<int>(&DARKELF_MAX_MP)->default_value(900), "黑暗精灵MP上限")
  ("DragonKnightMaxHP", value<int>(&DRAGONKNIGHT_MAX_HP)->default_value(1400), "龙骑士HP上限")
  ("DragonKnightMaxMP", value<int>(&DRAGONKNIGHT_MAX_MP)->default_value(600), "龙骑士MP上限")
  ("IllusionistMaxHP", value<int>(&ILLUSIONIST_MAX_HP)->default_value(900), "幻术师HP上限")
  ("IllusionistMaxMP", value<int>(&ILLUSIONIST_MAX_MP)->default_value(1100), "幻术师MP上限")
  ("Lv50Exp", value<int>(&LV50_EXP)->default_value(1))
  ("Lv51Exp", value<int>(&LV51_EXP)->default_value(1))
  ("Lv52Exp", value<int>(&LV52_EXP)->default_value(1))
  ("Lv53Exp", value<int>(&LV53_EXP)->default_value(1))
  ("Lv54Exp", value<int>(&LV54_EXP)->default_value(1))
  ("Lv55Exp", value<int>(&LV55_EXP)->default_value(1))
  ("Lv56Exp", value<int>(&LV56_EXP)->default_value(1))
  ("Lv57Exp", value<int>(&LV57_EXP)->default_value(1))
  ("Lv58Exp", value<int>(&LV58_EXP)->default_value(1))
  ("Lv59Exp", value<int>(&LV59_EXP)->default_value(1))
  ("Lv60Exp", value<int>(&LV60_EXP)->default_value(1))
  ("Lv61Exp", value<int>(&LV61_EXP)->default_value(1))
  ("Lv62Exp", value<int>(&LV62_EXP)->default_value(1))
  ("Lv63Exp", value<int>(&LV63_EXP)->default_value(1))
  ("Lv64Exp", value<int>(&LV64_EXP)->default_value(1))
  ("Lv65Exp", value<int>(&LV65_EXP)->default_value(1))
  ("Lv66Exp", value<int>(&LV66_EXP)->default_value(1))
  ("Lv67Exp", value<int>(&LV67_EXP)->default_value(1))
  ("Lv68Exp", value<int>(&LV68_EXP)->default_value(1))
  ("Lv69Exp", value<int>(&LV69_EXP)->default_value(1))
  ("Lv70Exp", value<int>(&LV70_EXP)->default_value(1))
  ("Lv71Exp", value<int>(&LV71_EXP)->default_value(1))
  ("Lv72Exp", value<int>(&LV72_EXP)->default_value(1))
  ("Lv73Exp", value<int>(&LV73_EXP)->default_value(1))
  ("Lv74Exp", value<int>(&LV74_EXP)->default_value(1))
  ("Lv75Exp", value<int>(&LV75_EXP)->default_value(1))
  ("Lv76Exp", value<int>(&LV76_EXP)->default_value(1))
  ("Lv77Exp", value<int>(&LV77_EXP)->default_value(1))
  ("Lv78Exp", value<int>(&LV78_EXP)->default_value(1))
  ("Lv79Exp", value<int>(&LV79_EXP)->default_value(1))
  ("Lv80Exp", value<int>(&LV80_EXP)->default_value(1))
  ("Lv81Exp", value<int>(&LV81_EXP)->default_value(1))
  ("Lv82Exp", value<int>(&LV82_EXP)->default_value(1))
  ("Lv83Exp", value<int>(&LV83_EXP)->default_value(1))
  ("Lv84Exp", value<int>(&LV84_EXP)->default_value(1))
  ("Lv85Exp", value<int>(&LV85_EXP)->default_value(1))
  ("Lv86Exp", value<int>(&LV86_EXP)->default_value(1))
  ("Lv87Exp", value<int>(&LV87_EXP)->default_value(1))
  ("Lv88Exp", value<int>(&LV88_EXP)->default_value(1))
  ("Lv89Exp", value<int>(&LV89_EXP)->default_value(1))
  ("Lv90Exp", value<int>(&LV90_EXP)->default_value(1))
  ("Lv91Exp", value<int>(&LV91_EXP)->default_value(1))
  ("Lv92Exp", value<int>(&LV92_EXP)->default_value(1))
  ("Lv93Exp", value<int>(&LV93_EXP)->default_value(1))
  ("Lv94Exp", value<int>(&LV94_EXP)->default_value(1))
  ("Lv95Exp", value<int>(&LV95_EXP)->default_value(1))
  ("Lv96Exp", value<int>(&LV96_EXP)->default_value(1))
  ("Lv97Exp", value<int>(&LV97_EXP)->default_value(1))
  ("Lv98Exp", value<int>(&LV98_EXP)->default_value(1))
  ("Lv99Exp", value<int>(&LV99_EXP)->default_value(1))
  ("Lv100Exp", value<int>(&LV100_EXP)->default_value(1))
  ("Lv101Exp", value<int>(&LV101_EXP)->default_value(1))
  ("Lv102Exp", value<int>(&LV102_EXP)->default_value(1))
  ("Lv103Exp", value<int>(&LV103_EXP)->default_value(1))
  ("Lv104Exp", value<int>(&LV104_EXP)->default_value(1))
  ("Lv105Exp", value<int>(&LV105_EXP)->default_value(1))
  ("Lv106Exp", value<int>(&LV106_EXP)->default_value(1))
  ("Lv107Exp", value<int>(&LV107_EXP)->default_value(1))
  ("Lv108Exp", value<int>(&LV108_EXP)->default_value(1))
  ("Lv109Exp", value<int>(&LV109_EXP)->default_value(1))
  ("Lv110Exp", value<int>(&LV110_EXP)->default_value(1))
  ("FightIsActive", value<bool>(&FIGHT_IS_ACTIVE)->default_value(false), "启动战斗特化系统")
  ("NoviceProtectionIsActive", value<bool>(&NOVICE_PROTECTION_IS_ACTIVE)->default_value(false), "新手保护系统(遭遇的守护)")
  ("NoviceMaxLevel", value<int>(&NOVICE_MAX_LEVEL)->default_value(20), "被归类为新手的等级上限")
  ("ProtectionLevelRange", value<int>(&NOVICE_PROTECTION_LEVEL_RANGE0)->default_value(10), "启动新手保护机制")
  ("LoggingWeaponEnchant", value<int>(&LOGGING_WEAPON_ENCHANT)->default_value(0), "武器强化")
  ("LoggingArmorEnchant", value<int>(&LOGGING_ARMOR_ENCHANT)->default_value(0), "防具强化")
  ("LoggingChatNormal", value<bool>(&LOGGING_CHAT_NORMAL)->default_value(false), "一般频道")
  ("LoggingChatWhisper", value<bool>(&LOGGING_CHAT_WHISPER)->default_value(false), "密语频道")
  ("LoggingChatShout", value<bool>(&LOGGING_CHAT_SHOUT)->default_value(false), "大喊频道")
  ("LoggingChatWorld", value<bool>(&LOGGING_CHAT_WORLD)->default_value(false), "广播频道")
  ("LoggingChatClan", value<bool>(&LOGGING_CHAT_CLAN)->default_value(false), "血盟频道")
  ("LoggingChatParty", value<bool>(&LOGGING_CHAT_PARTY)->default_value(false), "组队频道")
  ("LoggingChatCombined", value<bool>(&LOGGING_CHAT_COMBINED)->default_value(false), "联盟频道")
  ("LoggingChatChatParty", value<bool>(&LOGGING_CHAT_CHAT_PARTY)->default_value(false), "聊天队伍频道")
  ("writeTradeLog", value<bool>(&writeTradeLog)->default_value(false), "交易纪录")
  ("writeRobotsLog", value<bool>(&writeRobotsLog)->default_value(false), "记录加速器讯息")
  ("writeDropLog", value<bool>(&writeDropLog)->default_value(false), "丢弃物品纪录")
  ("NewCreateRoleSetGM", value<bool>(&NEW_CREATE_ROLE_SET_GM)->default_value(false), "是否新建角色即为GM")
  ("ShowNpcId", value<bool>(&SHOW_NPC_ID)->default_value(false), "是否显示NpcId")
  ("LvUpHpMpFull", value<bool>(&LV_UP_HP_MP_FULL)->default_value(false), "升级血魔满")
  ("RestartTime", value<int>(&REST_TIME)->default_value(720), "伺服器重启时间")
  ("HourlyChime", value<bool>(&HOURLY_CHIME)->default_value(false), "整点报时")
  ;
  variables_map vm;
  std::ifstream ifs_server(TConfig::SERVER);
  store(parse_config_file(ifs_server, opts, true), vm);
  std::ifstream ifs_sql(TConfig::SQL);
  store(parse_config_file(ifs_sql, opts, true), vm);
  std::ifstream ifs_rates(TConfig::RATES);
  store(parse_config_file(ifs_rates, opts, true), vm);
  std::ifstream ifs_alt(TConfig::ALT);
  store(parse_config_file(ifs_alt, opts, true), vm);
  std::ifstream ifs_char(TConfig::CHAR);
  store(parse_config_file(ifs_char, opts, true), vm);
  std::ifstream ifs_fight(TConfig::FIGHT);
  store(parse_config_file(ifs_fight, opts, true), vm);
  std::ifstream ifs_record(TConfig::RECORD);
  store(parse_config_file(ifs_record, opts, true), vm);
  std::ifstream ifs_other(TConfig::OTHER);
  store(parse_config_file(ifs_other, opts, true), vm);
  std::ifstream ifs_check(TConfig::CHECK);
  store(parse_config_file(ifs_check, opts, true), vm);
  notify(vm);

  if(vm.empty())
  {
    std::cout << opts << std::endl;
  }

  ClientLanguageCodeLoad();
  Validate();
}

void TConfig::ClientLanguageCodeLoad()
{
  CLIENT_LANGUAGE_CODE = TConfig::LANGUAGE_CODE_ARRAY[CLIENT_LANGUAGE];
}

void TConfig::Validate()
{
  if(!TIntRange::includes(ALT_ITEM_DELETION_RANGE, 0, 5))
  {
    //throw boost::exception() << err_str("ItemDeletionRange 的设定值超出( 0 ~ 5 )范围");
  }

  if(!TIntRange::includes(ALT_ITEM_DELETION_TIME, 1, 35791))
  {
    //throw boost::exception() << err_str("ItemDeletionTime 的设定值超出( 1 ~ 35791 )范围");
  }
}
