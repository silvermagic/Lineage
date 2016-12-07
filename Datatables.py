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
        if not exc_type:
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
accounts                 = Base.classes.accounts
area                     = Base.classes.area
armor                    = Base.classes.armor
armor_Set                = Base.classes.armor_set
ban_Ip                   = Base.classes.ban_ip
beginner                 = Base.classes.beginner
board                    = Base.classes.board
board_auction            = Base.classes.board_auction
castle                   = Base.classes.castle
character_buddys         = Base.classes.character_buddys
character_buff           = Base.classes.character_buff
character_config         = Base.classes.character_config
character_elf_warehouse  = Base.classes.character_elf_warehouse
character_items          = Base.classes.character_items
character_quests         = Base.classes.character_quests
character_skills         = Base.classes.character_skills
character_teleport       = Base.classes.character_teleport
character_warehouse      = Base.classes.character_warehouse
characters               = Base.classes.characters
clan_data                = Base.classes.clan_data
clan_warehouse           = Base.classes.clan_warehouse
commands                 = Base.classes.commands
drop_item                = Base.classes.drop_item
droplist                 = Base.classes.droplist
dungeon                  = Base.classes.dungeon
dungeon_random           = Base.classes.dungeon_random
eric_random_mob          = Base.classes.eric_random_mob
eric_startcheckwartime   = Base.classes.eric_startcheckwartime
etcitem                  = Base.classes.etcitem
getback                 = Base.classes.getback
getback_restart          = Base.classes.getback_restart
house                    = Base.classes.house
inn                      = Base.classes.inn
inn_key                  = Base.classes.inn_key
letter                   = Base.classes.letter
log_Chat                 = Base.classes.log_chat
log_enchant              = Base.classes.log_enchant
magic_doll               = Base.classes.magic_doll
mail                     = Base.classes.mail
mapids                   = Base.classes.mapids
mobgroup                 = Base.classes.mobgroup
mobskill                 = Base.classes.mobskill
monster_enhance          = Base.classes.monster_enhance
npc                      = Base.classes.npc
npcaction                = Base.classes.npcaction
npcchat                  = Base.classes.npcchat
petitem                  = Base.classes.petitem
pets                     = Base.classes.pets
pettypes                 = Base.classes.pettypes
polymorphs               = Base.classes.polymorphs
race_ticket              = Base.classes.race_ticket
resolvent                = Base.classes.resolvent
shop                     = Base.classes.shop
shop_sell_price          = Base.classes.shop_sell_price
skills                   = Base.classes.skills
skills_copy              = Base.classes.skills_copy
spawnlist                = Base.classes.spawnlist
spawnlist_boss           = Base.classes.spawnlist_boss
spawnlist_door           = Base.classes.spawnlist_door
spawnlist_furniture      = Base.classes.spawnlist_furniture
spawnlist_light          = Base.classes.spawnlist_light
spawnlist_npc            = Base.classes.spawnlist_npc
spawnlist_time           = Base.classes.spawnlist_time
spawnlist_trap           = Base.classes.spawnlist_trap
spawnlist_ub             = Base.classes.spawnlist_ub
spr_action               = Base.classes.spr_action
town                     = Base.classes.town
trap                     = Base.classes.trap
ub_managers              = Base.classes.ub_managers
ub_settings              = Base.classes.ub_settings
ub_supplies              = Base.classes.ub_supplies
ub_times                 = Base.classes.ub_times
weapon                   = Base.classes.weapon
weapon_skill             = Base.classes.weapon_skill
william_auto_add_skill   = Base.classes.william_auto_add_skill
william_bad_names        = Base.classes.william_bad_names
william_item_magic       = Base.classes.william_item_magic
william_item_summon      = Base.classes.william_item_summon
william_mob_talk         = Base.classes.william_mob_talk
william_npc_action       = Base.classes.william_npc_action
william_npc_quest        = Base.classes.william_npc_quest
william_npc_spawn        = Base.classes.william_npc_spawn
william_npc_talk         = Base.classes.william_npc_talk
william_reward           = Base.classes.william_reward
william_system_message   = Base.classes.william_system_message
william_teleport_scroll  = Base.classes.william_teleport_scroll