import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("mysql+pymysql://root:root@localhost/l1jdb?charset=GBK")
SessionMaker = scoped_session(sessionmaker(bind=engine))

class Session():
    def __init__(self):
        self._s = None

    def __enter__(self):
        self._s = SessionMaker()
        return self._s

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            try:
                self._s.commit()
            except:
                self._s.rollback()
                raise
        else:
            self._s.rollback()

# reflect the tables
reload(sys)
sys.setdefaultencoding('utf-8')
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Accounts                 = Base.classes.accounts
Area                     = Base.classes.area
Armor                    = Base.classes.armor
Armor_Set                = Base.classes.armor_set
Ban_Ip                   = Base.classes.ban_ip
Beginner                 = Base.classes.beginner
Board                    = Base.classes.board
Board_Auction            = Base.classes.board_auction
Castle                   = Base.classes.castle
Character_Buddys         = Base.classes.character_buddys
Character_Buff           = Base.classes.character_buff
Character_Config         = Base.classes.character_config
Character_Elf_Warehouse  = Base.classes.character_elf_warehouse
Character_Items          = Base.classes.character_items
Character_Quests         = Base.classes.character_quests
Character_Skills         = Base.classes.character_skills
Character_Teleport       = Base.classes.character_teleport
Character_Warehouse      = Base.classes.character_warehouse
Characters               = Base.classes.characters
Clan_Data                = Base.classes.clan_data
Clan_Warehouse           = Base.classes.clan_warehouse
Commands                 = Base.classes.commands
Drop_Item                = Base.classes.drop_item
Droplist                 = Base.classes.droplist
Dungeon                  = Base.classes.dungeon
Dungeon_Random           = Base.classes.dungeon_random
Eric_Random_Mob          = Base.classes.eric_random_mob
Eric_Startcheckwartime   = Base.classes.eric_startcheckwartime
Etcitem                  = Base.classes.etcitem
Getback                 = Base.classes.getback
Getback_Restart          = Base.classes.getback_restart
House                    = Base.classes.house
Inn                      = Base.classes.inn
Inn_Key                  = Base.classes.inn_key
Letter                   = Base.classes.letter
Log_Chat                 = Base.classes.log_chat
Log_Enchant              = Base.classes.log_enchant
Magic_Doll               = Base.classes.magic_doll
Mail                     = Base.classes.mail
Mapids                   = Base.classes.mapids
Mobgroup                 = Base.classes.mobgroup
Mobskill                 = Base.classes.mobskill
Monster_Enhance          = Base.classes.monster_enhance
Npc                      = Base.classes.npc
Npcaction                = Base.classes.npcaction
Npcchat                  = Base.classes.npcchat
Petitem                  = Base.classes.petitem
Pets                     = Base.classes.pets
Pettypes                 = Base.classes.pettypes
Polymorphs               = Base.classes.polymorphs
Race_Ticket              = Base.classes.race_ticket
Resolvent                = Base.classes.resolvent
Shop                     = Base.classes.shop
Shop_Sell_Price          = Base.classes.shop_sell_price
Skills                   = Base.classes.skills
Skills_Copy              = Base.classes.skills_copy
Spawnlist                = Base.classes.spawnlist
Spawnlist_Boss           = Base.classes.spawnlist_boss
Spawnlist_Door           = Base.classes.spawnlist_door
Spawnlist_Furniture      = Base.classes.spawnlist_furniture
Spawnlist_Light          = Base.classes.spawnlist_light
Spawnlist_Npc            = Base.classes.spawnlist_npc
Spawnlist_Time           = Base.classes.spawnlist_time
Spawnlist_Trap           = Base.classes.spawnlist_trap
Spawnlist_Ub             = Base.classes.spawnlist_ub
Spr_Action               = Base.classes.spr_action
Town                     = Base.classes.town
Trap                     = Base.classes.trap
Ub_Managers              = Base.classes.ub_managers
Ub_Settings              = Base.classes.ub_settings
Ub_Supplies              = Base.classes.ub_supplies
Ub_Times                 = Base.classes.ub_times
Weapon                   = Base.classes.weapon
Weapon_Skill             = Base.classes.weapon_skill
William_Auto_Add_Skill   = Base.classes.william_auto_add_skill
William_Bad_Names        = Base.classes.william_bad_names
William_Item_Magic       = Base.classes.william_item_magic
William_Item_Summon      = Base.classes.william_item_summon
William_Mob_Talk         = Base.classes.william_mob_talk
William_Npc_Action       = Base.classes.william_npc_action
William_Npc_Quest        = Base.classes.william_npc_quest
William_Npc_Spawn        = Base.classes.william_npc_spawn
William_Npc_Talk         = Base.classes.william_npc_talk
William_Reward           = Base.classes.william_reward
William_System_Message   = Base.classes.william_system_message
William_Teleport_Scroll  = Base.classes.william_teleport_scroll