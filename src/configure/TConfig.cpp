#include <fstream>
#include <sstream>
#include "Poco/Util/PropertyFileConfiguration.h"
#include "utils/TIntRange.h"
#include "configure/TConfig.h"

using Poco::Util::PropertyFileConfiguration;

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
  std::ifstream ifs_server(TConfig::SERVER);
  std::ifstream ifs_sql(TConfig::SQL);
  std::ifstream ifs_rates(TConfig::RATES);
  std::ifstream ifs_alt(TConfig::ALT);
  std::ifstream ifs_char(TConfig::CHAR);
  std::ifstream ifs_fight(TConfig::FIGHT);
  std::ifstream ifs_record(TConfig::RECORD);
  std::ifstream ifs_other(TConfig::OTHER);
  std::ifstream ifs_check(TConfig::CHECK);
  std::stringstream buf;
  buf << ifs_server.rdbuf() << ifs_sql.rdbuf() << ifs_rates.rdbuf() << ifs_alt.rdbuf() << ifs_char.rdbuf() << ifs_fight.rdbuf() << ifs_record.rdbuf() << ifs_other.rdbuf() << ifs_check.rdbuf();

  Poco::AutoPtr<PropertyFileConfiguration> pcfg =  new PropertyFileConfiguration(buf);
  CHECK_LOCK = pcfg->getBool("Lock", false); //调试:是否开启检测回溯
  PACKETS = pcfg->getBool("Packets", false); //调试:是否开启封包发送错误提示
  BUG_BEAR_RACE = pcfg->getBool("isBugBearRace", false); //调试:是否开启奇岩 食人妖精竞赛
  DEBUG = pcfg->getBool("DebugMode", false); //调试/侦错模式
  PACKET = pcfg->getBool("PrintPacket", false); //控制台是否显示封包
  THREAD_P_TYPE_GENERAL = pcfg->getInt("GeneralThreadPoolType", 0); //控制台是否显示封包
  THREAD_P_SIZE_GENERAL = pcfg->getInt("GeneralThreadPoolSize", 0); //控制台是否显示封包
  GAME_SERVER_HOST_NAME = pcfg->getString("GameserverHostname", "*"); //服务器主机(IP)
  GAME_SERVER_PORT = pcfg->getInt("GameserverPort", 2000); //服务器端口
  TIME_ZONE = pcfg->getString("TimeZone", "Etc/GMT+8"); //时区设置
  CLIENT_LANGUAGE = pcfg->getInt("ClientLanguage", 5); //客户端语系
  HOSTNAME_LOOKUPS = pcfg->getBool("HostnameLookups", false); //DNS反向验证
  AUTOMATIC_KICK = pcfg->getInt("AutomaticKick", 10); //客户端无动作时自动断线时间
  AUTO_CREATE_ACCOUNTS = pcfg->getBool("AutoCreateAccounts", false); //自动创建帐号
  MAX_ONLINE_USERS = pcfg->getInt("MaximumOnlineUsers", 30); //最高在线玩家数量
  CACHE_MAP_FILES = pcfg->getBool("CacheMapFiles", false); //生成地图快取档案
  LOAD_V2_MAP_FILES = pcfg->getBool("LoadV2MapFiles", false); //V2地图 (测试用)
  CHECK_MOVE_INTERVAL = pcfg->getBool("CheckMoveInterval", false); //加速器侦测 (移动间隔)
  CHECK_ATTACK_INTERVAL = pcfg->getBool("CheckAttackInterval", false); //加速器侦测 (攻击间隔)
  CHECK_SPELL_INTERVAL = pcfg->getBool("CheckSpellInterval", false); //加速器侦测 (技能使用间隔)
  INJUSTICE_COUNT = pcfg->getInt("InjusticeCount", 10); //设定不正常封包数值,满足条件则切断连线
  JUSTICE_COUNT = pcfg->getInt("JusticeCount", 4); //设定如果参杂正常封包在不正常封包中,数值满足时InjusticeCount归0
  CHECK_STRICTNESS = pcfg->getInt("CheckStrictness", 102); //加速器检查严密度
  ILLEGAL_SPEEDUP_PUNISHMENT = pcfg->getInt("Punishment", 0); //加速处罚机制
  AUTOSAVE_INTERVAL = pcfg->getInt("AutosaveInterval", 1200); //伺服器自动存档时间间隔 (单位: 秒)
  AUTOSAVE_INTERVAL_INVENTORY = pcfg->getInt("AutosaveIntervalOfInventory", 300); //定时自动储存角色装备资料时间间隔 (单位: 秒)
  SKILLTIMER_IMPLTYPE = pcfg->getInt("SkillTimerImplType", 1); //技能计数器实施类型
  NPCAI_IMPLTYPE = pcfg->getInt("NpcAIImplType", 1); //NpcAI的实施类型
  TELNET_SERVER = pcfg->getBool("TelnetServer", false); //远程登录控制伺服器
  TELNET_SERVER_PORT = pcfg->getInt("TelnetServerPort", 23); //远程控制的Port号码
  PC_RECOGNIZE_RANGE = pcfg->getInt("PcRecognizeRange", 20); //发送到一个范围的信息给客户端对像
  CHARACTER_CONFIG_IN_SERVER_SIDE = pcfg->getBool("CharacterConfigInServerSide", false); //人物资讯统一管理(F5~12快捷键和人物血条位置等)
  ALLOW_2PC = pcfg->getBool("Allow2PC", false); //双开(同IP同时连线)
  LEVEL_DOWN_RANGE = pcfg->getInt("LevelDownRange", 0); //允许降等的水平范围（检测死亡降等范围）
  SEND_PACKET_BEFORE_TELEPORT = pcfg->getBool("SendPacketBeforeTeleport", false); //瞬移控制
  CMD_ACTIVE = pcfg->getBool("CmdActive", false); //CMD互动指令
  Announcements_Cycle_Time = pcfg->getInt("AnnouncementsCycleTime", 30); //循环时间设置 (单位:分钟)
  Announcements_Cycle_Modify_Time = pcfg->getBool("AnnounceTimeDisplay", false); //自动显示公告修改时间
  DB_DRIVER = pcfg->getString("Driver", "com.mysql.jdbc.Driver"); //数据库驱动程序
  DB_URL = pcfg->getString("URL", "jdbc:mysql://localhost/l1jdb?useUnicode=true&characterEncoding=utf8"); //数据库路径
  DB_LOGIN = pcfg->getString("Login", "root"); //数据库账号
  DB_PASSWORD = pcfg->getString("Password", "root"); //数据库密码
  DETECT_DB_RESOURCE_LEAKS = pcfg->getBool("EnableDatabaseResourceLeaksDetection", false); //数据库资源泄漏检测
  MYSQL_AUTO_BACKUP = pcfg->getInt("MysqlAutoBackup", 0); //MySQL定时自动备份
  COMPRESS_G_ZIP = pcfg->getBool("CompressGzip", false); //备份的输出SQL是否启用GZip压缩
  RATE_XP = pcfg->getDouble("RateXp", 1.0); //经验值倍率
  RATE_LA = pcfg->getDouble("RateLawful", 1.0); //正义值倍率
  RATE_KARMA = pcfg->getDouble("RateKarma", 1.0); //友好度倍率
  RATE_DROP_ADENA = pcfg->getDouble("RateDropAdena", 1.0); //掉落金钱倍率
  RATE_DROP_ITEMS = pcfg->getDouble("RateDropItems", 1.0); //掉落物品倍率
  ENCHANT_CHANCE_WEAPON = pcfg->getDouble("EnchantChanceWeapon", 1.0); //冲武器成功率
  ENCHANT_CHANCE_ARMOR = pcfg->getDouble("EnchantChanceArmor", 1.0); //冲防具成功率
  ATTR_ENCHANT_CHANCE = pcfg->getDouble("AttrEnchantChance", 1.0); //属性强化成功率
  RATE_WEIGHT_LIMIT = pcfg->getDouble("RateWeightLimit", 1.0); //角色负重倍率
  RATE_WEIGHT_LIMIT_PET = pcfg->getDouble("RateWeightLimitforPet", 1.0); //宠物负重倍率
  RATE_SHOP_SELLING_PRICE = pcfg->getDouble("RateShopSellingPrice", 1.0); //商店贩卖价格倍率
  RATE_SHOP_PURCHASING_PRICE = pcfg->getDouble("RateShopPurchasingPrice", 1.0); //商店收购价格倍率
  CREATE_CHANCE_DIARY = pcfg->getInt("CreateChanceDiary", 33); //航海日志合成几率
  CREATE_CHANCE_RECOLLECTION = pcfg->getInt("CreateChanceRecollection", 90); //净化的部分
  CREATE_CHANCE_MYSTERIOUS = pcfg->getInt("CreateChanceMysterious", 90); //神秘药水
  CREATE_CHANCE_PROCESSING = pcfg->getInt("CreateChanceProcessing", 90); //被加工了的宝石
  CREATE_CHANCE_PROCESSING_DIAMOND = pcfg->getInt("CreateChanceProcessingDiamond", 90); //被加工了的钻石
  CREATE_CHANCE_DANTES = pcfg->getInt("CreateChanceDantes", 50); //完整的召唤球
  CREATE_CHANCE_ANCIENT_AMULET = pcfg->getInt("CreateChanceAncientAmulet", 90); //不起眼的古老项链
  CREATE_CHANCE_HISTORY_BOOK = pcfg->getInt("CreateChanceHistory", 50); //封印的历史书
  MAGIC_STONE_TYPE = pcfg->getInt("MagicStoneAttr", 50); //附魔石类型
  MAGIC_STONE_LEVEL = pcfg->getInt("MagicStoneLevel", 50); //附魔石阶级
  GLOBAL_CHAT_LEVEL = pcfg->getInt("GlobalChatLevel", 30); //全体聊天最低等级限制
  WHISPER_CHAT_LEVEL = pcfg->getInt("WhisperChatLevel", 5); //密语最低等级限制
  AUTO_LOOT = pcfg->getInt("AutoLoot", 2); //自动取得道具的方式
  LOOTING_RANGE = pcfg->getInt("LootingRange", 3); //道具掉落的范围大小
  ALT_NONPVP = pcfg->getBool("NonPvP", false); //Non-PvP设定
  ALT_ATKMSG = pcfg->getBool("AttackMessageOn", false); //GM是否显示伤害讯息
  CHANGE_TITLE_BY_ONESELF = pcfg->getBool("ChangeTitleByOneself", false); //自己更改称号
  CLAN_ALLIANCE = pcfg->getBool("ClanAlliance", false); //血盟联盟系统
  MAX_PT = pcfg->getInt("MaxPT", 8); //组队人数上限
  MAX_CHAT_PT = pcfg->getInt("MaxChatPT", 8); //组队聊天人数上限
  SIM_WAR_PENALTY = pcfg->getBool("SimWarPenalty", false); //攻城战中红人死亡后是否会受到处罚
  GET_BACK = pcfg->getBool("GetBack", false); //重新登入时是否在出生地
  ALT_ITEM_DELETION_TYPE = pcfg->getString("ItemDeletionType", "auto"); //地图上地面道具删除设置
  ALT_ITEM_DELETION_TIME = pcfg->getInt("ItemDeletionTime", 30); //物品在地面自动清除掉的时间
  ALT_ITEM_DELETION_RANGE = pcfg->getInt("ItemDeletionRange", 5); //人物周围不清除物品范围大小
  ALT_GMSHOP = pcfg->getBool("GMshop", false); //是否开启GM商店
  ALT_GMSHOP_MIN_ID = pcfg->getInt("GMshopMinID", 0xffffffff); //GM商店编号最小值
  ALT_GMSHOP_MAX_ID = pcfg->getInt("GMshopMaxID", 0xffffffff); //GM商店编号最大值
  ALT_HALLOWEENIVENT = pcfg->getBool("HalloweenIvent", false); //南瓜怪任务开关
  ALT_TALKINGSCROLLQUEST = pcfg->getBool("TalkingScrollQuest", false); //日本特典道具NPC开关

  ALT_JPPRIVILEGED = pcfg->getBool("JpPrivileged", false); //说话卷轴任务开关
  ALT_WHO_COMMAND = pcfg->getBool("WhoCommand", false); //who 指令是否可以使用
  ALT_REVIVAL_POTION = pcfg->getBool("RevivalPotion", false); //99级是否可以获得返生药水
  //("WarTime", value<int>()->default_value(2), "攻城战时间")
  //("WarTime", value<int>()->default_value(2), "攻城战时间单位")
  //("WarInterval", value<int>()->default_value(4), "攻城日的间隔")
  //("WarInterval", value<int>()->default_value(4), "攻城日的间隔单位")
  SPAWN_HOME_POINT = pcfg->getBool("SpawnHomePoint", false); //范围性怪物刷新
  SPAWN_HOME_POINT_RANGE = pcfg->getInt("SpawnHomePointRange", 8); //怪物刷新的范围大小
  SPAWN_HOME_POINT_COUNT = pcfg->getInt("SpawnHomePointCount", 2); //怪物出生点设定最小
  SPAWN_HOME_POINT_DELAY = pcfg->getInt("SpawnHomePointDelay", 100); //怪物出生点设定的最大
  INIT_BOSS_SPAWN = pcfg->getBool("InitBossSpawn", false); //服务器启动时Boss是否出现
  ELEMENTAL_STONE_AMOUNT = pcfg->getInt("ElementalStoneAmount", 300); //妖精森林元素石的数量
  HOUSE_TAX_INTERVAL = pcfg->getInt("HouseTaxInterval", 10); //盟屋税金的支付期限(日)
  MAX_DOLL_COUNT = pcfg->getInt("MaxDollCount", 1); //魔法娃娃召唤数量上限
  RETURN_TO_NATURE = pcfg->getBool("ReturnToNature", false); //释放元素技能的使用
  MAX_NPC_ITEM = pcfg->getInt("MaxNpcItem", 8); //NPC(召唤, 宠物)身上可以持有的最大物品数量
  MAX_PERSONAL_WAREHOUSE_ITEM = pcfg->getInt("MaxPersonalWarehouseItem", 150); //个人仓库物品上限数量
  MAX_CLAN_WAREHOUSE_ITEM = pcfg->getInt("MaxClanWarehouseItem", 200); //血盟仓库物品上限数量
  DELETE_CHARACTER_AFTER_7DAYS = pcfg->getBool("DeleteCharacterAfter7Days", false); //角色等级30以上，删除角色是否要等待7天
  NPC_DELETION_TIME = pcfg->getInt("NpcDeletionTime", 10); //NPC死亡后尸体消失时间（秒）
  DEFAULT_CHARACTER_SLOT = pcfg->getInt("DefaultCharacterSlot", 6); //预设角色数量
  GDROPITEM_TIME = pcfg->getInt("GDropItemTime", 10); //妖精森林NPC道具重置时间
  PRINCE_MAX_HP = pcfg->getInt("PrinceMaxHP", 1000); //王族HP上限
  PRINCE_MAX_MP = pcfg->getInt("PrinceMaxMP", 800); //王族MP上限
  KNIGHT_MAX_HP = pcfg->getInt("KnightMaxHP", 1400); //骑士HP上限
  KNIGHT_MAX_MP = pcfg->getInt("KnightMaxMP", 600); //骑士MP上限
  ELF_MAX_HP = pcfg->getInt("ElfMaxHP", 1000); //精灵HP上限
  ELF_MAX_MP = pcfg->getInt("ElfMaxMP", 900); //精灵MP上限
  WIZARD_MAX_HP = pcfg->getInt("WizardMaxHP", 800); //法师HP上限
  WIZARD_MAX_MP = pcfg->getInt("WizardMaxMP", 1200); //法师MP上限
  PRINCE_MAX_HP = pcfg->getInt("PrinceMaxHP", 1000); //王族HP上限
  PRINCE_MAX_MP = pcfg->getInt("PrinceMaxMP", 800); //王族MP上限
  DARKELF_MAX_HP = pcfg->getInt("DarkelfMaxHP", 1000); //黑暗精灵HP上限
  DARKELF_MAX_MP = pcfg->getInt("DarkelfMaxMP", 900); //黑暗精灵MP上限
  DRAGONKNIGHT_MAX_HP = pcfg->getInt("DragonKnightMaxHP", 1400); //龙骑士HP上限
  DRAGONKNIGHT_MAX_MP = pcfg->getInt("DragonKnightMaxMP", 600); //龙骑士MP上限
  ILLUSIONIST_MAX_HP = pcfg->getInt("IllusionistMaxHP", 900); //幻术师HP上限
  ILLUSIONIST_MAX_MP = pcfg->getInt("IllusionistMaxMP", 1100); //幻术师MP上限
  LV50_EXP = pcfg->getInt("Lv50Exp", 1);
  LV51_EXP = pcfg->getInt("Lv51Exp", 1);
  LV52_EXP = pcfg->getInt("Lv52Exp", 1);
  LV53_EXP = pcfg->getInt("Lv53Exp", 1);
  LV54_EXP = pcfg->getInt("Lv54Exp", 1);
  LV55_EXP = pcfg->getInt("Lv55Exp", 1);
  LV56_EXP = pcfg->getInt("Lv56Exp", 1);
  LV57_EXP = pcfg->getInt("Lv57Exp", 1);
  LV58_EXP = pcfg->getInt("Lv58Exp", 1);
  LV59_EXP = pcfg->getInt("Lv59Exp", 1);
  LV60_EXP = pcfg->getInt("Lv60Exp", 1);
  LV61_EXP = pcfg->getInt("Lv61Exp", 1);
  LV62_EXP = pcfg->getInt("Lv62Exp", 1);
  LV63_EXP = pcfg->getInt("Lv63Exp", 1);
  LV64_EXP = pcfg->getInt("Lv64Exp", 1);
  LV65_EXP = pcfg->getInt("Lv65Exp", 1);
  LV66_EXP = pcfg->getInt("Lv66Exp", 1);
  LV67_EXP = pcfg->getInt("Lv67Exp", 1);
  LV68_EXP = pcfg->getInt("Lv68Exp", 1);
  LV69_EXP = pcfg->getInt("Lv69Exp", 1);
  LV70_EXP = pcfg->getInt("Lv70Exp", 1);
  LV71_EXP = pcfg->getInt("Lv71Exp", 1);
  LV72_EXP = pcfg->getInt("Lv72Exp", 1);
  LV73_EXP = pcfg->getInt("Lv73Exp", 1);
  LV74_EXP = pcfg->getInt("Lv74Exp", 1);
  LV75_EXP = pcfg->getInt("Lv75Exp", 1);
  LV76_EXP = pcfg->getInt("Lv76Exp", 1);
  LV77_EXP = pcfg->getInt("Lv77Exp", 1);
  LV78_EXP = pcfg->getInt("Lv78Exp", 1);
  LV79_EXP = pcfg->getInt("Lv79Exp", 1);
  LV80_EXP = pcfg->getInt("Lv80Exp", 1);
  LV81_EXP = pcfg->getInt("Lv81Exp", 1);
  LV82_EXP = pcfg->getInt("Lv82Exp", 1);
  LV83_EXP = pcfg->getInt("Lv83Exp", 1);
  LV84_EXP = pcfg->getInt("Lv84Exp", 1);
  LV85_EXP = pcfg->getInt("Lv85Exp", 1);
  LV86_EXP = pcfg->getInt("Lv86Exp", 1);
  LV87_EXP = pcfg->getInt("Lv87Exp", 1);
  LV88_EXP = pcfg->getInt("Lv88Exp", 1);
  LV89_EXP = pcfg->getInt("Lv89Exp", 1);
  LV90_EXP = pcfg->getInt("Lv90Exp", 1);
  LV91_EXP = pcfg->getInt("Lv91Exp", 1);
  LV92_EXP = pcfg->getInt("Lv92Exp", 1);
  LV93_EXP = pcfg->getInt("Lv93Exp", 1);
  LV94_EXP = pcfg->getInt("Lv94Exp", 1);
  LV95_EXP = pcfg->getInt("Lv95Exp", 1);
  LV96_EXP = pcfg->getInt("Lv96Exp", 1);
  LV97_EXP = pcfg->getInt("Lv97Exp", 1);
  LV98_EXP = pcfg->getInt("Lv98Exp", 1);
  LV99_EXP = pcfg->getInt("Lv99Exp", 1);
  LV100_EXP = pcfg->getInt("Lv100Exp", 1);
  LV101_EXP = pcfg->getInt("Lv101Exp", 1);
  LV102_EXP = pcfg->getInt("Lv102Exp", 1);
  LV103_EXP = pcfg->getInt("Lv103Exp", 1);
  LV104_EXP = pcfg->getInt("Lv104Exp", 1);
  LV105_EXP = pcfg->getInt("Lv105Exp", 1);
  LV106_EXP = pcfg->getInt("Lv106Exp", 1);
  LV107_EXP = pcfg->getInt("Lv107Exp", 1);
  LV108_EXP = pcfg->getInt("Lv108Exp", 1);
  LV109_EXP = pcfg->getInt("Lv109Exp", 1);
  LV110_EXP = pcfg->getInt("Lv110Exp", 1);
  FIGHT_IS_ACTIVE = pcfg->getBool("FightIsActive", false); //启动战斗特化系统
  NOVICE_PROTECTION_IS_ACTIVE = pcfg->getBool("NoviceProtectionIsActive", false); //新手保护系统(遭遇的守护)
  NOVICE_MAX_LEVEL = pcfg->getInt("NoviceMaxLevel", 20); //被归类为新手的等级上限
  NOVICE_PROTECTION_LEVEL_RANGE0 = pcfg->getInt("ProtectionLevelRange", 10); //启动新手保护机制

  LOGGING_WEAPON_ENCHANT = pcfg->getInt("LoggingWeaponEnchant", 0); //武器强化
  LOGGING_ARMOR_ENCHANT = pcfg->getInt("LoggingArmorEnchant", 0); //防具强化
  LOGGING_CHAT_NORMAL = pcfg->getBool("LoggingChatNormal", false); //一般频道

  LOGGING_CHAT_WHISPER = pcfg->getBool("LoggingChatWhisper", false); //密语频道
  LOGGING_CHAT_SHOUT = pcfg->getBool("LoggingChatShout", false); //大喊频道
  LOGGING_CHAT_WORLD = pcfg->getBool("LoggingChatWorld", false); //广播频道
  LOGGING_CHAT_CLAN = pcfg->getBool("LoggingChatClan", false); //血盟频道
  LOGGING_CHAT_PARTY = pcfg->getBool("LoggingChatParty", false); //组队频道
  LOGGING_CHAT_COMBINED = pcfg->getBool("LoggingChatCombined", false); //联盟频道
  LOGGING_CHAT_CHAT_PARTY = pcfg->getBool("LoggingChatChatParty", false); //聊天队伍频道
  writeTradeLog = pcfg->getBool("writeTradeLog", false); //交易纪录
  writeRobotsLog = pcfg->getBool("writeRobotsLog", false); //记录加速器讯息
  writeDropLog = pcfg->getBool("writeDropLog", false); //丢弃物品纪录
  NEW_CREATE_ROLE_SET_GM = pcfg->getBool("NewCreateRoleSetGM", false); //是否新建角色即为GM
  SHOW_NPC_ID = pcfg->getBool("ShowNpcId", false); //是否显示NpcId
  LV_UP_HP_MP_FULL = pcfg->getBool("LvUpHpMpFull", false); //升级血魔满
  REST_TIME = pcfg->getInt("RestartTime", 720); //伺服器重启时间
  HOURLY_CHIME = pcfg->getBool("HourlyChime", false); //整点报时

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
    throw std::out_of_range("ItemDeletionRange的设定值超出( 0 ~ 5 )范围");
  }

  if(!TIntRange::includes(ALT_ITEM_DELETION_TIME, 1, 35791))
  {
    throw std::out_of_range("ItemDeletionTime的设定值超出( 1 ~ 35791 )范围");
  }
}
