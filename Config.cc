//
// Created by 范炜东 on 2019/4/23.
//

#include <exception>
#include <vector>
#include <fstream>
#include <boost/program_options.hpp>
#include <boost/log/core.hpp>
#include <boost/log/trivial.hpp>
#include <boost/log/utility/setup/console.hpp>
#include <boost/log/utility/setup/file.hpp>
#include <boost/log/utility/setup/common_attributes.hpp>
#include "Config.h"

static std::string LANGUAGE_CODE_ARRAY[] = {"UTF8", "EUCKR", "UTF8", "BIG5", "SJIS", "GBK"};

/** 服务配置 */
bool Config::DEBUG = true;
int Config::SERVER_PORT = 2000;
std::string Config::MAP_DIR = "../maps";
std::string Config::DB_USER = "postgres";
std::string Config::DB_PASSWORD = "123456";
std::string Config::DB_NAME = "l1jdb";
std::string Config::DB_HOST = "localhost";
unsigned int Config::DB_PORT = 3306;
int Config::CLIENT_LANGUAGE = 5;
std::string Config::CLIENT_LANGUAGE_CODE = LANGUAGE_CODE_ARRAY[CLIENT_LANGUAGE];
std::string Config::TIME_ZONE = "JST";
int Config::AUTOMATIC_KICK = 10;
bool Config::AUTO_CREATE_ACCOUNTS = true;
short Config::MAX_ONLINE_USERS = 30;
bool Config::CACHE_MAP_FILES = false;
bool Config::LOAD_V2_MAP_FILES = false;
bool Config::CHECK_MOVE_INTERVAL = false;
bool Config::CHECK_ATTACK_INTERVAL = false;
bool Config::CHECK_SPELL_INTERVAL = false;
short Config::INJUSTICE_COUNT = 10;
int Config::JUSTICE_COUNT = 4;
int Config::CHECK_STRICTNESS = 102;
unsigned char Config::LOGGING_WEAPON_ENCHANT = 0;
unsigned char Config::LOGGING_ARMOR_ENCHANT = 0;
bool Config::LOGGING_CHAT_NORMAL = false;
bool Config::LOGGING_CHAT_WHISPER = false;
bool Config::LOGGING_CHAT_SHOUT = false;
bool Config::LOGGING_CHAT_WORLD = false;
bool Config::LOGGING_CHAT_CLAN = false;
bool Config::LOGGING_CHAT_PARTY = false;
bool Config::LOGGING_CHAT_COMBINED = false;
bool Config::LOGGING_CHAT_CHAT_PARTY = false;
int Config::AUTOSAVE_INTERVAL = 1200;
int Config::AUTOSAVE_INTERVAL_INVENTORY = 300;
int Config::SKILLTIMER_IMPLTYPE = 1;
int Config::NPCAI_IMPLTYPE = 1;
bool Config::TELNET_SERVER = false;
int Config::TELNET_SERVER_PORT = 23;
int Config::PC_RECOGNIZE_RANGE = 20;
bool Config::CHARACTER_CONFIG_IN_SERVER_SIDE = true;
bool Config::ALLOW_2PC = true;
int Config::LEVEL_DOWN_RANGE = 0;
bool Config::SEND_PACKET_BEFORE_TELEPORT = false;
bool Config::DETECT_DB_RESOURCE_LEAKS = false;
/** 倍率配置 */
double Config::RATE_XP = 1.0;
double Config::RATE_LA = 1.0;
double Config::RATE_KARMA = 1.0;
double Config::RATE_DROP_ADENA = 1.0;
double Config::RATE_DROP_ITEMS = 1.0;
int Config::ENCHANT_CHANCE_WEAPON = 68;
int Config::ENCHANT_CHANCE_ARMOR = 52;
int Config::ATTR_ENCHANT_CHANCE = 10;
double Config::RATE_WEIGHT_LIMIT = 1.0;
double Config::RATE_WEIGHT_LIMIT_PET = 1.0;
double Config::RATE_SHOP_SELLING_PRICE = 1.0;
double Config::RATE_SHOP_PURCHASING_PRICE = 1.0;
int Config::CREATE_CHANCE_DIARY = 33;
int Config::CREATE_CHANCE_RECOLLECTION = 90;
int Config::CREATE_CHANCE_MYSTERIOUS = 90;
int Config::CREATE_CHANCE_PROCESSING = 90;
int Config::CREATE_CHANCE_PROCESSING_DIAMOND = 90;
int Config::CREATE_CHANCE_DANTES = 50;
int Config::CREATE_CHANCE_ANCIENT_AMULET = 90;
int Config::CREATE_CHANCE_HISTORY_BOOK = 50;
/** 游戏配置 */
int Config::GLOBAL_CHAT_LEVEL = 30;
int Config::WHISPER_CHAT_LEVEL = 5;
int Config::AUTO_LOOT = 2;
int Config::LOOTING_RANGE = 3;
bool Config::ALT_NONPVP = true;
bool Config::ALT_ATKMSG = true;
bool Config::CHANGE_TITLE_BY_ONESELF = false;
int Config::MAX_CLAN_MEMBER = 0;
bool Config::CLAN_ALLIANCE = true;
int Config::MAX_PT = 8;
int Config::MAX_CHAT_PT = 8;
bool Config::GITorF = false;
long Config::GI = 41159;
int Config::GIC = 1;
int Config::GIT = 3;
bool Config::GUI = true;
bool Config::WHO_ONLINE_MSG_ON = false;
int Config::REST_TIME = 60;
int Config::RATE_AIN_TIME = 30;
int Config::RATE_AIN_OUTTIME = 30;
int Config::RATE_MAX_CHARGE_PERCENT = 200;
bool Config::Use_Show_Announcecycle = true;
int Config::SHOW_ANNOUNCECYCLE_TIME = 30;
bool Config::GM_TALK_SHOW_NAME = true;
bool Config::All_SELL = true;
bool Config::SIM_WAR_PENALTY = true;
bool Config::GET_BACK = false;
std::string Config::ALT_ITEM_DELETION_TYPE = "auto";
int Config::ALT_ITEM_DELETION_TIME = 10;
int Config::ALT_ITEM_DELETION_RANGE = 5;
bool Config::ALT_GMSHOP = false;
int Config::ALT_GMSHOP_MIN_ID = 0;
int Config::ALT_GMSHOP_MAX_ID = 0;
bool Config::ALT_HALLOWEENIVENT = true;
bool Config::ALT_JPPRIVILEGED = false;
bool Config::ALT_TALKINGSCROLLQUEST = false;
bool Config::ALT_WHO_COMMAND = false;
bool Config::ALT_REVIVAL_POTION = false;
int Config::ALT_WAR_TIME = 120;
int Config::ALT_WAR_INTERVAL = 7;
bool Config::DEAD_LOST_ITEM = false;
bool Config::SPAWN_HOME_POINT = true;
int Config::SPAWN_HOME_POINT_RANGE = 8;
int Config::SPAWN_HOME_POINT_COUNT = 2;
int Config::SPAWN_HOME_POINT_DELAY = 100;
bool Config::INIT_BOSS_SPAWN = true;
int Config::ELEMENTAL_STONE_AMOUNT = 30;
int Config::HOUSE_TAX_INTERVAL = 10;
int Config::MAX_DOLL_COUNT = 1;
bool Config::RETURN_TO_NATURE = false;
int Config::MAX_NPC_ITEM = 8;
int Config::MAX_PERSONAL_WAREHOUSE_ITEM = 100;
int Config::MAX_CLAN_WAREHOUSE_ITEM = 200;
bool Config::DELETE_CHARACTER_AFTER_7DAYS = false;
int Config::NPC_DELETION_TIME = 10;
int Config::DEFAULT_CHARACTER_SLOT = 6;
/** 角色配置 */
int Config::PET_LEVEL = 51;
int Config::REVIVAL_POTION = 5;
int Config::PRINCE_MAX_HP = 1000;
int Config::PRINCE_MAX_MP = 800;
int Config::KNIGHT_MAX_HP = 1400;
int Config::KNIGHT_MAX_MP = 600;
int Config::ELF_MAX_HP = 1000;
int Config::ELF_MAX_MP = 900;
int Config::WIZARD_MAX_HP = 800;
int Config::WIZARD_MAX_MP = 1200;
int Config::DARKELF_MAX_HP = 1000;
int Config::DARKELF_MAX_MP = 900;
int Config::DRAGONKNIGHT_MAX_HP = 1400;
int Config::DRAGONKNIGHT_MAX_MP = 600;
int Config::ILLUSIONIST_MAX_HP = 900;
int Config::ILLUSIONIST_MAX_MP = 1100;
int Config::LV50_EXP = 1;
int Config::LV51_EXP = 1;
int Config::LV52_EXP = 1;
int Config::LV53_EXP = 1;
int Config::LV54_EXP = 1;
int Config::LV55_EXP = 1;
int Config::LV56_EXP = 1;
int Config::LV57_EXP = 1;
int Config::LV58_EXP = 1;
int Config::LV59_EXP = 1;
int Config::LV60_EXP = 1;
int Config::LV61_EXP = 1;
int Config::LV62_EXP = 1;
int Config::LV63_EXP = 1;
int Config::LV64_EXP = 1;
int Config::LV65_EXP = 2;
int Config::LV66_EXP = 2;
int Config::LV67_EXP = 2;
int Config::LV68_EXP = 2;
int Config::LV69_EXP = 2;
int Config::LV70_EXP = 4;
int Config::LV71_EXP = 4;
int Config::LV72_EXP = 4;
int Config::LV73_EXP = 4;
int Config::LV74_EXP = 4;
int Config::LV75_EXP = 8;
int Config::LV76_EXP = 8;
int Config::LV77_EXP = 8;
int Config::LV78_EXP = 8;
int Config::LV79_EXP = 16;
int Config::LV80_EXP = 32;
int Config::LV81_EXP = 64;
int Config::LV82_EXP = 128;
int Config::LV83_EXP = 256;
int Config::LV84_EXP = 512;
int Config::LV85_EXP = 1024;
int Config::LV86_EXP = 2048;
int Config::LV87_EXP = 4096;
int Config::LV88_EXP = 8192;
int Config::LV89_EXP = 16384;
int Config::LV90_EXP = 32768;
int Config::LV91_EXP = 65536;
int Config::LV92_EXP = 131072;
int Config::LV93_EXP = 262144;
int Config::LV94_EXP = 524288;
int Config::LV95_EXP = 1048576;
int Config::LV96_EXP = 2097152;
int Config::LV97_EXP = 4194304;
int Config::LV98_EXP = 8388608;
int Config::LV99_EXP = 16777216;

void Config::load(int argc, char *argv[]) {
  using namespace boost::program_options;

  options_description server_desc("服务器设定");
  server_desc.add_options()
          ("ServerPort", value<int>(&SERVER_PORT), "")
          ("MapDir", value<std::string>(&MAP_DIR), "")
          ("User", value<std::string>(&DB_USER), "")
          ("Password", value<std::string>(&DB_PASSWORD), "")
          ("Name", value<std::string>(&DB_NAME), "")
          ("Host", value<std::string>(&DB_HOST), "")
          ("Port", value<unsigned int>(&DB_PORT), "")
          ("ClientLanguage", value<int>(&CLIENT_LANGUAGE), "")
          ("TimeZone", value<std::string>(&TIME_ZONE), "")
          ("AutomaticKick", value<int>(&AUTOMATIC_KICK), "")
          ("AutoCreateAccounts", value<bool>(&AUTO_CREATE_ACCOUNTS), "")
          ("MaximumOnlineUsers", value<short>(&MAX_ONLINE_USERS), "")
          ("CacheMapFiles", value<bool>(&CACHE_MAP_FILES), "")
          ("LoadV2MapFiles", value<bool>(&LOAD_V2_MAP_FILES), "")
          ("CheckMoveInterval", value<bool>(&CHECK_MOVE_INTERVAL), "")
          ("CheckAttackInterval", value<bool>(&CHECK_ATTACK_INTERVAL), "")
          ("CheckSpellInterval", value<bool>(&CHECK_SPELL_INTERVAL), "")
          ("InjusticeCount", value<short>(&INJUSTICE_COUNT), "")
          ("JusticeCount", value<int>(&JUSTICE_COUNT), "")
          ("CheckStrictness", value<int>(&CHECK_STRICTNESS), "")
          ("LoggingWeaponEnchant", value<unsigned char>(&LOGGING_WEAPON_ENCHANT), "")
          ("LoggingArmorEnchant", value<unsigned char>(&LOGGING_ARMOR_ENCHANT), "")
          ("LoggingChatNormal", value<bool>(&LOGGING_CHAT_NORMAL), "")
          ("LoggingChatWhisper", value<bool>(&LOGGING_CHAT_WHISPER), "")
          ("LoggingChatShout", value<bool>(&LOGGING_CHAT_SHOUT), "")
          ("LoggingChatWorld", value<bool>(&LOGGING_CHAT_WORLD), "")
          ("LoggingChatClan", value<bool>(&LOGGING_CHAT_CLAN), "")
          ("LoggingChatParty", value<bool>(&LOGGING_CHAT_PARTY), "")
          ("LoggingChatCombined", value<bool>(&LOGGING_CHAT_COMBINED), "")
          ("LoggingChatChatParty", value<bool>(&LOGGING_CHAT_CHAT_PARTY), "")
          ("AutosaveInterval", value<int>(&AUTOSAVE_INTERVAL), "")
          ("AutosaveIntervalOfInventory", value<int>(&AUTOSAVE_INTERVAL_INVENTORY), "")
          ("SkillTimerImplType", value<int>(&SKILLTIMER_IMPLTYPE), "")
          ("NpcAIImplType", value<int>(&NPCAI_IMPLTYPE), "")
          ("TelnetServer", value<bool>(&TELNET_SERVER), "")
          ("TelnetServerPort", value<int>(&TELNET_SERVER_PORT), "")
          ("PcRecognizeRange", value<int>(&PC_RECOGNIZE_RANGE), "")
          ("CharacterConfigInServerSide", value<bool>(&CHARACTER_CONFIG_IN_SERVER_SIDE), "")
          ("Allow2PC", value<bool>(&ALLOW_2PC), "")
          ("LevelDownRange", value<int>(&LEVEL_DOWN_RANGE), "")
          ("SendPacketBeforeTeleport", value<bool>(&SEND_PACKET_BEFORE_TELEPORT), "")
          ("EnableDatabaseResourceLeaksDetection", value<bool>(&DETECT_DB_RESOURCE_LEAKS), "");

  options_description rate_desc("游戏倍率设定");
  rate_desc.add_options()
          ("RateXp", value<double>(&RATE_XP), "")
          ("RateLawful", value<double>(&RATE_LA), "")
          ("RateKarma", value<double>(&RATE_KARMA), "")
          ("RateDropAdena", value<double>(&RATE_DROP_ADENA), "")
          ("RateDropItems", value<double>(&RATE_DROP_ITEMS), "")
          ("EnchantChanceWeapon", value<int>(&ENCHANT_CHANCE_WEAPON), "")
          ("EnchantChanceArmor", value<int>(&ENCHANT_CHANCE_ARMOR), "")
          ("AttrEnchantChance", value<int>(&ATTR_ENCHANT_CHANCE), "")
          ("RateWeightLimit", value<double>(&RATE_WEIGHT_LIMIT), "")
          ("RateWeightLimitforPet", value<double>(&RATE_WEIGHT_LIMIT_PET), "")
          ("RateShopSellingPrice", value<double>(&RATE_SHOP_SELLING_PRICE), "")
          ("RateShopPurchasingPrice", value<double>(&RATE_SHOP_PURCHASING_PRICE), "")
          ("CreateChanceDiary", value<int>(&CREATE_CHANCE_DIARY), "")
          ("CreateChanceRecollection", value<int>(&CREATE_CHANCE_RECOLLECTION), "")
          ("CreateChanceMysterious", value<int>(&CREATE_CHANCE_MYSTERIOUS), "")
          ("CreateChanceProcessing", value<int>(&CREATE_CHANCE_PROCESSING), "")
          ("CreateChanceProcessingDiamond", value<int>(&CREATE_CHANCE_PROCESSING_DIAMOND), "")
          ("CreateChanceDantes", value<int>(&CREATE_CHANCE_DANTES), "")
          ("CreateChanceAncientAmulet", value<int>(&CREATE_CHANCE_ANCIENT_AMULET), "")
          ("CreateChanceHistoryBook", value<int>(&CREATE_CHANCE_HISTORY_BOOK), "");

  options_description alt_desc("游戏内容设定");
  alt_desc.add_options()
          ("GlobalChatLevel", value<int>(&GLOBAL_CHAT_LEVEL), "设置使用公共频道的最低等级限制")
          ("WhisperChatLevel", value<int>(&WHISPER_CHAT_LEVEL), "设置使用密语频道的最低等级限制")
          ("AutoLoot", value<int>(&AUTO_LOOT), "设定自动取得道具的方式 0-掉落地上 1-掉落宠物身上 2-掉落角色身上")
          ("LootingRange", value<int>(&LOOTING_RANGE), "设置道具掉落范围")
          ("NonPvP", value<bool>(&ALT_NONPVP), "设置是否为PVP模式(默认是)")
          ("AttackMessageOn", value<bool>(&ALT_ATKMSG), "设置是否显示伤害信息(默认不显示)")
          ("ChangeTitleByOneself", value<bool>(&CHANGE_TITLE_BY_ONESELF), "设置加入血盟后能否自己变更封号(默认允许)")
          ("MaxClanMember", value<int>(&MAX_CLAN_MEMBER), "设置血盟人数上限 0-取决于魅力值")
          ("ClanAlliance", value<bool>(&CLAN_ALLIANCE), "设置是否能够组建联盟，允许其他王族加入(默认允许)")
          ("MaxPT", value<int>(&MAX_PT), "设置组队人数上限")
          ("MaxChatPT", value<int>(&MAX_CHAT_PT), "设置组队聊天人数上限")
          ("GITorF", value<bool>(&GITorF), "设置是否开启在线道具赠送系统(默认开启)")
          ("GI", value<long>(&GI), "设置在线道具赠送的道具编号")
          ("GIC", value<int>(&GIC), "设置单次在线道具赠送的道具数目")
          ("GIT", value<int>(&GIT), "设置在线赠送时间间隔(分钟)")
          ("GUI", value<bool>(&GUI), "")
          ("WhoOnlineMessageOn", value<bool>(&WHO_ONLINE_MSG_ON), "设置玩家上限是否通知在线GM(默认通知)")
          ("RestartTime", value<int>(&REST_TIME), "")
          ("RateAinTime", value<int>(&RATE_AIN_TIME), "设置在安全区登入多少时间取得1%殷海萨的祝福(分钟, 上限15)")
          ("RateAinOutTime", value<int>(&RATE_AIN_OUTTIME), "设置在安全区登出多少时间取得1%殷海萨的祝福(分钟, 上限15)")
          ("RateMaxChargePercent", value<int>(&RATE_MAX_CHARGE_PERCENT), "设置殷海萨的祝福最高百分比")
          ("UseShowAnnouncecycle", value<bool>(&Use_Show_Announcecycle), "设置是否允许使用循环公告(data/announcecycle.txt, 默认允许)")
          ("ShowAnnouncecycleTime", value<int>(&SHOW_ANNOUNCECYCLE_TIME), "设置循环公告显示间隔(分钟)")
          ("GMTalkShowName", value<bool>(&GM_TALK_SHOW_NAME), "设置GM使用公共频道时是否显示角色ID")
          ("AllSell", value<bool>(&All_SELL), "设置是否允许使用循环公告(data/announcecycle.txt, 默认允许)")
          ("SimWarPenalty", value<bool>(&SIM_WAR_PENALTY), "设置攻城战中红名死亡是否会受到惩罚(默认受到惩罚)")
          ("GetBack", value<bool>(&GET_BACK), "设置重新登入后是否回到出生地")
          ("ItemDeletionType", value<std::string>(&ALT_ITEM_DELETION_TYPE), "设置地面道具删除方法 none-不删除 std-一段时间后删除 auto-定时删除")
          ("ItemDeletionTime", value<int>(&ALT_ITEM_DELETION_TIME), "设置地面道具自动删除间隔")
          ("ItemDeletionRange", value<int>(&ALT_ITEM_DELETION_RANGE), "设置人物(0-5格)范围内不清除道具(std类型无视此设定)")
          ("GMshop", value<bool>(&ALT_GMSHOP), "设置是否开启GM商店(默认开启)")
          ("GMshopMinID", value<int>(&ALT_GMSHOP_MIN_ID), "设置GM商店编号的最小值，可查看在spawnlist_npc内的编号进行设置")
          ("GMshopMaxID", value<int>(&ALT_GMSHOP_MAX_ID), "设置GM商店编号的最大值，可查看在spawnlist_npc内的编号进行设置")
          ("HalloweenIvent", value<bool>(&ALT_HALLOWEENIVENT), "设置万圣节时是否有南瓜怪活动(默认没有)")
          ("JpPrivileged", value<bool>(&ALT_JPPRIVILEGED), "设置是否存在日本独有的NPC(默认不存在)")
          ("TalkingScrollQuest", value<bool>(&ALT_TALKINGSCROLLQUEST), "设置是否开启新手村的说话卷轴任务(默认不开启)")
          ("WhoCommand", value<bool>(&ALT_WHO_COMMAND), "设置/who指令是否可以查看名单(默认可以)")
          ("RevivalPotion", value<bool>(&ALT_REVIVAL_POTION), "设置99级是否获得返生药水(默认获得)")
          ("WarTime", value<int>(&ALT_WAR_TIME), "设置攻城战持续时间(分钟)")
          ("WarInterval", value<int>(&ALT_WAR_INTERVAL), "设置攻城日间隔(分钟)")
          ("DeadLostItem", value<bool>(&DEAD_LOST_ITEM), "设置角色死亡掉落的物品是否由系统回收(默认不回收，掉落地面)")
          ("SpawnHomePoint", value<bool>(&SPAWN_HOME_POINT), "设置是否记录初期配置的刷怪地点(spawnlist内的locx1、locy1、locx2、locy2)")
          ("SpawnHomePointRange", value<int>(&SPAWN_HOME_POINT_RANGE), "设置随机出现范围")
          ("SpawnHomePointCount", value<int>(&SPAWN_HOME_POINT_COUNT), "设置范围内怪物刷新最小数目")
          ("SpawnHomePointDelay", value<int>(&SPAWN_HOME_POINT_DELAY), "设置范围内怪物刷新间隔")
          ("InitBossSpawn", value<bool>(&INIT_BOSS_SPAWN), "设置服务器启动时是否刷新Boss(相当于Boss刷新时间重置)")
          ("ElementalStoneAmount", value<int>(&ELEMENTAL_STONE_AMOUNT), "设置妖精森林地上的元素石总数")
          ("HouseTaxInterval", value<int>(&HOUSE_TAX_INTERVAL), "设置村庄的税金纳库间隔(天)")
          ("MaxDollCount", value<int>(&MAX_DOLL_COUNT), "设置魔法娃娃最大持有数目")
          ("ReturnToNature", value<bool>(&RETURN_TO_NATURE), "设置是否允许使用妖精的释放元素魔法(默认不允许)")
          ("MaxNpcItem", value<int>(&MAX_NPC_ITEM), "设置允许携带的NPC(召唤和宠物)数目")
          ("MaxPersonalWarehouseItem", value<int>(&MAX_PERSONAL_WAREHOUSE_ITEM), "设置个人仓库可存储的道具数目")
          ("MaxClanWarehouseItem", value<int>(&MAX_CLAN_WAREHOUSE_ITEM), "设置血盟仓库可存储的道具数目")
          ("DeleteCharacterAfter7Days", value<bool>(&DELETE_CHARACTER_AFTER_7DAYS), "设置30级以上角色删除是否要等待7天")
          ("NpcDeletionTime", value<int>(&NPC_DELETION_TIME), "设置NPC从死亡到消失的时间(秒)")
          ("DefaultCharacterSlot", value<int>(&DEFAULT_CHARACTER_SLOT), "设置账户角色槽数目");

  options_description char_desc("游戏角色设定");
  char_desc.add_options()
          ("PetLevel", value<int>(&PET_LEVEL), "")
          ("RevivalPotion", value<int>(&REVIVAL_POTION), "")
          ("PrinceMaxHP", value<int>(&PRINCE_MAX_HP), "")
          ("PrinceMaxMP", value<int>(&PRINCE_MAX_MP), "")
          ("KnightMaxHP", value<int>(&KNIGHT_MAX_HP), "")
          ("KnightMaxMP", value<int>(&KNIGHT_MAX_MP), "")
          ("ElfMaxHP", value<int>(&ELF_MAX_HP), "")
          ("ElfMaxMP", value<int>(&ELF_MAX_MP), "")
          ("WizardMaxHP", value<int>(&WIZARD_MAX_HP), "")
          ("WizardMaxMP", value<int>(&WIZARD_MAX_MP), "")
          ("DarkelfMaxHP", value<int>(&DARKELF_MAX_HP), "")
          ("DarkelfMaxMP", value<int>(&DARKELF_MAX_MP), "")
          ("DragonKnightMaxHP", value<int>(&DRAGONKNIGHT_MAX_HP), "")
          ("DragonKnightMaxMP", value<int>(&DRAGONKNIGHT_MAX_MP), "")
          ("IllusionistMaxHP", value<int>(&ILLUSIONIST_MAX_HP), "")
          ("IllusionistMaxMP", value<int>(&ILLUSIONIST_MAX_MP), "")
          ("Lv50Exp", value<int>(&LV50_EXP), "")
          ("Lv51Exp", value<int>(&LV51_EXP), "")
          ("Lv52Exp", value<int>(&LV52_EXP), "")
          ("Lv53Exp", value<int>(&LV53_EXP), "")
          ("Lv54Exp", value<int>(&LV54_EXP), "")
          ("Lv55Exp", value<int>(&LV55_EXP), "")
          ("Lv56Exp", value<int>(&LV56_EXP), "")
          ("Lv57Exp", value<int>(&LV57_EXP), "")
          ("Lv58Exp", value<int>(&LV58_EXP), "")
          ("Lv59Exp", value<int>(&LV59_EXP), "")
          ("Lv60Exp", value<int>(&LV60_EXP), "")
          ("Lv61Exp", value<int>(&LV61_EXP), "")
          ("Lv62Exp", value<int>(&LV62_EXP), "")
          ("Lv63Exp", value<int>(&LV63_EXP), "")
          ("Lv64Exp", value<int>(&LV64_EXP), "")
          ("Lv65Exp", value<int>(&LV65_EXP), "")
          ("Lv66Exp", value<int>(&LV66_EXP), "")
          ("Lv67Exp", value<int>(&LV67_EXP), "")
          ("Lv68Exp", value<int>(&LV68_EXP), "")
          ("Lv69Exp", value<int>(&LV69_EXP), "")
          ("Lv70Exp", value<int>(&LV70_EXP), "")
          ("Lv71Exp", value<int>(&LV71_EXP), "")
          ("Lv72Exp", value<int>(&LV72_EXP), "")
          ("Lv73Exp", value<int>(&LV73_EXP), "")
          ("Lv74Exp", value<int>(&LV74_EXP), "")
          ("Lv75Exp", value<int>(&LV75_EXP), "")
          ("Lv76Exp", value<int>(&LV76_EXP), "")
          ("Lv77Exp", value<int>(&LV77_EXP), "")
          ("Lv78Exp", value<int>(&LV78_EXP), "")
          ("Lv79Exp", value<int>(&LV79_EXP), "")
          ("Lv80Exp", value<int>(&LV80_EXP), "")
          ("Lv81Exp", value<int>(&LV81_EXP), "")
          ("Lv82Exp", value<int>(&LV82_EXP), "")
          ("Lv83Exp", value<int>(&LV83_EXP), "")
          ("Lv84Exp", value<int>(&LV84_EXP), "")
          ("Lv85Exp", value<int>(&LV85_EXP), "")
          ("Lv86Exp", value<int>(&LV86_EXP), "")
          ("Lv87Exp", value<int>(&LV87_EXP), "")
          ("Lv88Exp", value<int>(&LV88_EXP), "")
          ("Lv89Exp", value<int>(&LV89_EXP), "")
          ("Lv90Exp", value<int>(&LV80_EXP), "")
          ("Lv91Exp", value<int>(&LV91_EXP), "")
          ("Lv92Exp", value<int>(&LV92_EXP), "")
          ("Lv93Exp", value<int>(&LV93_EXP), "")
          ("Lv94Exp", value<int>(&LV94_EXP), "")
          ("Lv95Exp", value<int>(&LV95_EXP), "")
          ("Lv96Exp", value<int>(&LV96_EXP), "")
          ("Lv97Exp", value<int>(&LV97_EXP), "")
          ("Lv98Exp", value<int>(&LV98_EXP), "")
          ("Lv99Exp", value<int>(&LV99_EXP), "");

  // 参数解析
  options_description cfgfile_options("配置文件参数");
  cfgfile_options.add(alt_desc).add(char_desc).add(rate_desc).add(server_desc);

  options_description cmdline_options("命令行参数");
  cmdline_options.add_options()
          ("config-file", value<std::vector<std::string>>(), "相关配置文件");

  variables_map vm;
  store(parse_command_line(argc, argv, cmdline_options), vm);
  if (vm.count("config-file")) {
    auto files = vm["config-file"].as<std::vector<std::string>>();
    for (auto file : files) {
      std::ifstream ifs(file.c_str());
      store(parse_config_file(ifs, cfgfile_options), vm);
    }
  }
  notify(vm);

  // 日志初始化
  boost::log::register_simple_formatter_factory<boost::log::trivial::severity_level, char>("Severity");
  boost::log::add_console_log(std::cout, boost::log::keywords::format = "[%TimeStamp%] [%Severity%] %Message%");
  boost::log::add_file_log(
          boost::log::keywords::file_name = "sample_%N.log",
          boost::log::keywords::rotation_size = 10 * 1024 * 1024,
          boost::log::keywords::format = "[%TimeStamp%] [%Severity%] %Message%"
  );
  boost::log::add_common_attributes();
  if (DEBUG)
    boost::log::core::get()->set_filter(boost::log::trivial::severity >= boost::log::trivial::debug);
  else
    boost::log::core::get()->set_filter(boost::log::trivial::severity >= boost::log::trivial::info);

  // 手动更新
  CLIENT_LANGUAGE_CODE = LANGUAGE_CODE_ARRAY[CLIENT_LANGUAGE];
}
