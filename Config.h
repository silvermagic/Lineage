//
// Created by 范炜东 on 2019/4/23.
//

#ifndef PROJECT_CONFIG_H
#define PROJECT_CONFIG_H

#include <string>

class Config {
public:
  /* 加载配置文件 */
  static void load(int argc, char *argv[]);

public:
  /** 服务器配置 */
  static bool DEBUG;
  static int SERVER_PORT;
  static std::string MAP_DIR;
  static std::string DB_USER;
  static std::string DB_PASSWORD;
  static std::string DB_NAME;
  static std::string DB_HOST;
  static unsigned int DB_PORT;
  static unsigned int DB_POOL_SIZE;
  static int CLIENT_LANGUAGE;
  static std::string CLIENT_LANGUAGE_CODE;
  static std::string TIME_ZONE;
  static int AUTOMATIC_KICK;
  static bool AUTO_CREATE_ACCOUNTS;
  static short MAX_ONLINE_USERS;
  static bool CACHE_MAP_FILES;
  static bool LOAD_V2_MAP_FILES;
  static bool CHECK_MOVE_INTERVAL;
  static bool CHECK_ATTACK_INTERVAL;
  static bool CHECK_SPELL_INTERVAL;
  static short INJUSTICE_COUNT;
  static int JUSTICE_COUNT;
  static int CHECK_STRICTNESS;
  static unsigned char LOGGING_WEAPON_ENCHANT;
  static unsigned char LOGGING_ARMOR_ENCHANT;
  static bool LOGGING_CHAT_NORMAL;
  static bool LOGGING_CHAT_WHISPER;
  static bool LOGGING_CHAT_SHOUT;
  static bool LOGGING_CHAT_WORLD;
  static bool LOGGING_CHAT_CLAN;
  static bool LOGGING_CHAT_PARTY;
  static bool LOGGING_CHAT_COMBINED;
  static bool LOGGING_CHAT_CHAT_PARTY;
  static int AUTOSAVE_INTERVAL;
  static int AUTOSAVE_INTERVAL_INVENTORY;
  static int SKILLTIMER_IMPLTYPE;
  static int NPCAI_IMPLTYPE;
  static bool TELNET_SERVER;
  static int TELNET_SERVER_PORT;
  static int PC_RECOGNIZE_RANGE;
  static bool CHARACTER_CONFIG_IN_SERVER_SIDE;
  static bool ALLOW_2PC;
  static int LEVEL_DOWN_RANGE;
  static bool SEND_PACKET_BEFORE_TELEPORT;
  static bool DETECT_DB_RESOURCE_LEAKS;
  /** 倍率配置 */
  static double RATE_XP;
  static double RATE_LA;
  static double RATE_KARMA;
  static double RATE_DROP_ADENA;
  static double RATE_DROP_ITEMS;
  static int ENCHANT_CHANCE_WEAPON;
  static int ENCHANT_CHANCE_ARMOR;
  static int ATTR_ENCHANT_CHANCE;
  static double RATE_WEIGHT_LIMIT;
  static double RATE_WEIGHT_LIMIT_PET;
  static double RATE_SHOP_SELLING_PRICE;
  static double RATE_SHOP_PURCHASING_PRICE;
  static int CREATE_CHANCE_DIARY;
  static int CREATE_CHANCE_RECOLLECTION;
  static int CREATE_CHANCE_MYSTERIOUS;
  static int CREATE_CHANCE_PROCESSING;
  static int CREATE_CHANCE_PROCESSING_DIAMOND;
  static int CREATE_CHANCE_DANTES;
  static int CREATE_CHANCE_ANCIENT_AMULET;
  static int CREATE_CHANCE_HISTORY_BOOK;
  /** 游戏配置 */
  static int GLOBAL_CHAT_LEVEL;
  static int WHISPER_CHAT_LEVEL;
  static int AUTO_LOOT;
  static int LOOTING_RANGE;
  static bool ALT_NONPVP;
  static bool ALT_ATKMSG;
  static bool CHANGE_TITLE_BY_ONESELF;
  static int MAX_CLAN_MEMBER;
  static bool CLAN_ALLIANCE;
  static int MAX_PT;
  static int MAX_CHAT_PT;
  static bool GITorF;
  static long GI;
  static int GIC;
  static int GIT;
  static bool GUI;
  static bool WHO_ONLINE_MSG_ON;
  static int REST_TIME;
  static int RATE_AIN_TIME;
  static int RATE_AIN_OUTTIME;
  static int RATE_MAX_CHARGE_PERCENT;
  static bool Use_Show_Announcecycle;
  static int SHOW_ANNOUNCECYCLE_TIME;
  static bool GM_TALK_SHOW_NAME;
  static bool All_SELL;
  static bool SIM_WAR_PENALTY;
  static bool GET_BACK;
  static std::string ALT_ITEM_DELETION_TYPE;
  static int ALT_ITEM_DELETION_TIME;
  static int ALT_ITEM_DELETION_RANGE;
  static bool ALT_GMSHOP;
  static int ALT_GMSHOP_MIN_ID;
  static int ALT_GMSHOP_MAX_ID;
  static bool ALT_HALLOWEENIVENT;
  static bool ALT_JPPRIVILEGED;
  static bool ALT_TALKINGSCROLLQUEST;
  static bool ALT_WHO_COMMAND;
  static bool ALT_REVIVAL_POTION;
  static int ALT_WAR_TIME;
  static int ALT_WAR_INTERVAL;
  static bool DEAD_LOST_ITEM;
  static bool SPAWN_HOME_POINT;
  static int SPAWN_HOME_POINT_RANGE;
  static int SPAWN_HOME_POINT_COUNT;
  static int SPAWN_HOME_POINT_DELAY;
  static bool INIT_BOSS_SPAWN;
  static int ELEMENTAL_STONE_AMOUNT;
  static int HOUSE_TAX_INTERVAL;
  static int MAX_DOLL_COUNT;
  static bool RETURN_TO_NATURE;
  static int MAX_NPC_ITEM;
  static int MAX_PERSONAL_WAREHOUSE_ITEM;
  static int MAX_CLAN_WAREHOUSE_ITEM;
  static bool DELETE_CHARACTER_AFTER_7DAYS;
  static int NPC_DELETION_TIME;
  static int DEFAULT_CHARACTER_SLOT;
  /** 角色配置 */
  static int PET_LEVEL;
  static int REVIVAL_POTION;
  static int PRINCE_MAX_HP;
  static int PRINCE_MAX_MP;
  static int KNIGHT_MAX_HP;
  static int KNIGHT_MAX_MP;
  static int ELF_MAX_HP;
  static int ELF_MAX_MP;
  static int WIZARD_MAX_HP;
  static int WIZARD_MAX_MP;
  static int DARKELF_MAX_HP;
  static int DARKELF_MAX_MP;
  static int DRAGONKNIGHT_MAX_HP;
  static int DRAGONKNIGHT_MAX_MP;
  static int ILLUSIONIST_MAX_HP;
  static int ILLUSIONIST_MAX_MP;
  static int LV50_EXP;
  static int LV51_EXP;
  static int LV52_EXP;
  static int LV53_EXP;
  static int LV54_EXP;
  static int LV55_EXP;
  static int LV56_EXP;
  static int LV57_EXP;
  static int LV58_EXP;
  static int LV59_EXP;
  static int LV60_EXP;
  static int LV61_EXP;
  static int LV62_EXP;
  static int LV63_EXP;
  static int LV64_EXP;
  static int LV65_EXP;
  static int LV66_EXP;
  static int LV67_EXP;
  static int LV68_EXP;
  static int LV69_EXP;
  static int LV70_EXP;
  static int LV71_EXP;
  static int LV72_EXP;
  static int LV73_EXP;
  static int LV74_EXP;
  static int LV75_EXP;
  static int LV76_EXP;
  static int LV77_EXP;
  static int LV78_EXP;
  static int LV79_EXP;
  static int LV80_EXP;
  static int LV81_EXP;
  static int LV82_EXP;
  static int LV83_EXP;
  static int LV84_EXP;
  static int LV85_EXP;
  static int LV86_EXP;
  static int LV87_EXP;
  static int LV88_EXP;
  static int LV89_EXP;
  static int LV90_EXP;
  static int LV91_EXP;
  static int LV92_EXP;
  static int LV93_EXP;
  static int LV94_EXP;
  static int LV95_EXP;
  static int LV96_EXP;
  static int LV97_EXP;
  static int LV98_EXP;
  static int LV99_EXP;
};

#endif //PROJECT_CONFIG_H
