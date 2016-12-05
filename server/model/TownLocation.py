# -*- coding: utf-8 -*-

import random

TOWNID_TALKING_ISLAND = 1
TOWNID_SILVER_KNIGHT_TOWN = 2
TOWNID_GLUDIO = 3
TOWNID_ORCISH_FOREST = 4
TOWNID_WINDAWOOD = 5
TOWNID_KENT = 6
TOWNID_GIRAN = 7
TOWNID_HEINE = 8
TOWNID_WERLDAN = 9
TOWNID_OREN = 10
TOWNID_ELVEN_FOREST = 11
TOWNID_ADEN = 12
TOWNID_SILENT_CAVERN = 13
TOWNID_OUM_DUNGEON = 14
TOWNID_RESISTANCE = 15
TOWNID_PIRATE_ISLAND = 16
TOWNID_RECLUSE_VILLAGE = 17

GETBACK_MAP_TALKING_ISLAND = 0
GETBACK_LOC_TALKING_ISLAND = [
    (32600, 32942), (32574, 32944),
    (32580, 32923), (32557, 32975),
    (32597, 32914), (32580, 32974)]

GETBACK_MAP_SILVER_KNIGHT_TOWN = 4
GETBACK_LOC_SILVER_KNIGHT_TOWN = [
    (33071, 33402), (33091, 33396),
    (33085, 33402), (33097, 33366),
    (33110, 33365), (33072, 33392)]

GETBACK_MAP_GLUDIO = 4
GETBACK_LOC_GLUDIO = [
    (32601, 32757), (32625, 32809),
    (32611, 32726), (32612, 32781),
    (32605, 32761), (32614, 32739),
    (32612, 32775)]

GETBACK_MAP_ORCISH_FOREST = 4
GETBACK_LOC_ORCISH_FOREST = [
    (32750, 32435), (32745, 32447),
    (32738, 32452), (32741, 32436),
    (32749, 32446)]

GETBACK_MAP_WINDAWOOD = 4
GETBACK_LOC_WINDAWOOD = [
    (32608, 33178), (32626, 33185),
    (32630, 33179), (32625, 33207),
    (32638, 33203), (32621, 33179)]

GETBACK_MAP_KENT = 4
GETBACK_LOC_KENT = [
    (33048, 32750), (33059, 32768),
    (33047, 32761), (33059, 32759),
    (33051, 32775), (33048, 32778),
    (33064, 32773), (33057, 32748)]

GETBACK_MAP_GIRAN = 4
GETBACK_LOC_GIRAN = [
    (33435, 32803), (33439, 32817),
    (33440, 32809), (33419, 32810),
    (33426, 32823), (33418, 32818),
    (33432, 32824)]

GETBACK_MAP_HEINE = 4
GETBACK_LOC_HEINE = [
    (33593, 33242), (33593, 33248),
    (33604, 33236), (33599, 33236),
    (33610, 33247), (33610, 33241),
    (33599, 33252), (33605, 33252)]

GETBACK_MAP_WERLDAN = 4
GETBACK_LOC_WERLDAN = [
    (33702, 32492), (33747, 32508),
    (33696, 32498), (33723, 32512),
    (33710, 32521), (33724, 32488),
    (33693, 32513)]

GETBACK_MAP_OREN = 4
GETBACK_LOC_OREN = [
    (34086, 32280), (34037, 32230),
    (34022, 32254), (34021, 32269),
    (34044, 32290), (34049, 32316),
    (34081, 32249), (34074, 32313),
    (34064, 32230)]

GETBACK_MAP_ELVEN_FOREST = 4
GETBACK_LOC_ELVEN_FOREST = [
    (33065, 32358), (33052, 32313),
    (33030, 32342), (33068, 32320),
    (33071, 32314), (33030, 32370),
    (33076, 32324), (33068, 32336)]

GETBACK_MAP_ADEN = 4
GETBACK_LOC_ADEN = [
    (33915, 33114), (34061, 33115),
    (34090, 33168), (34011, 33136),
    (34093, 33117), (33959, 33156),
    (33992, 33120), (34047, 33156)]

GETBACK_MAP_SILENT_CAVERN = 304
GETBACK_LOC_SILENT_CAVERN = [
    (32856, 32898), (32860, 32916),
    (32868, 32893), (32875, 32903),
    (32855, 32898)]

GETBACK_MAP_OUM_DUNGEON = 310
GETBACK_LOC_OUM_DUNGEON = [
    (32818, 32805), (32800, 32798),
    (32815, 32819), (32823, 32811),
    (32817, 32828)]

GETBACK_MAP_RESISTANCE = 400
GETBACK_LOC_RESISTANCE = [
    (32570, 32667), (32559, 32678),
    (32564, 32683), (32574, 32661),
    (32576, 32669), (32572, 32662)]

GETBACK_MAP_PIRATE_ISLAND = 440
GETBACK_LOC_PIRATE_ISLAND = [
    (32431, 33058), (32407, 33054)]

GETBACK_MAP_RECLUSE_VILLAGE = 400
GETBACK_LOC_RECLUSE_VILLAGE = [
    (32599, 32916), (32599, 32923),
    (32603, 32908), (32595, 32908),
    (32591, 32918)]

class TownLocation():
    @classmethod
    def getGetBackLoc(cls, town_id):
        '''
        获取对应村庄的回城点
        :param town_id: 村庄id
        :return:回城点的游戏坐标
        '''
        ret = [0, 0, 0]
        if town_id == TOWNID_TALKING_ISLAND:
            rnd = random.randrange(len(GETBACK_LOC_TALKING_ISLAND))
            ret[0] = GETBACK_LOC_TALKING_ISLAND[rnd][0]
            ret[1] = GETBACK_LOC_TALKING_ISLAND[rnd][1]
            ret[2] = GETBACK_MAP_TALKING_ISLAND
        elif town_id == TOWNID_SILVER_KNIGHT_TOWN:
            rnd = random.randrange(len(GETBACK_LOC_SILVER_KNIGHT_TOWN))
            ret[0] = GETBACK_LOC_SILVER_KNIGHT_TOWN[rnd][0]
            ret[1] = GETBACK_LOC_SILVER_KNIGHT_TOWN[rnd][1]
            ret[2] = GETBACK_MAP_SILVER_KNIGHT_TOWN
        elif town_id == TOWNID_KENT:
            rnd = random.randrange(len(GETBACK_LOC_KENT))
            ret[0] = GETBACK_LOC_KENT[rnd][0]
            ret[1] = GETBACK_LOC_KENT[rnd][1]
            ret[2] = GETBACK_MAP_KENT
        elif town_id == TOWNID_GLUDIO:
            rnd = random.randrange(len(GETBACK_LOC_GLUDIO))
            ret[0] = GETBACK_LOC_GLUDIO[rnd][0]
            ret[1] = GETBACK_LOC_GLUDIO[rnd][1]
            ret[2] = GETBACK_MAP_GLUDIO
        elif town_id == TOWNID_ORCISH_FOREST:
            rnd = random.randrange(len(GETBACK_LOC_ORCISH_FOREST))
            ret[0] = GETBACK_LOC_ORCISH_FOREST[rnd][0]
            ret[1] = GETBACK_LOC_ORCISH_FOREST[rnd][1]
            ret[2] = GETBACK_MAP_ORCISH_FOREST
        elif town_id == TOWNID_WINDAWOOD:
            rnd = random.randrange(len(GETBACK_LOC_WINDAWOOD))
            ret[0] = GETBACK_LOC_WINDAWOOD[rnd][0]
            ret[1] = GETBACK_LOC_WINDAWOOD[rnd][1]
            ret[2] = GETBACK_MAP_WINDAWOOD
        elif town_id == TOWNID_GIRAN:
            rnd = random.randrange(len(GETBACK_LOC_GIRAN))
            ret[0] = GETBACK_LOC_GIRAN[rnd][0]
            ret[1] = GETBACK_LOC_GIRAN[rnd][1]
            ret[2] = GETBACK_MAP_GIRAN
        elif town_id == TOWNID_HEINE:
            rnd = random.randrange(len(GETBACK_LOC_HEINE))
            ret[0] = GETBACK_LOC_HEINE[rnd][0]
            ret[1] = GETBACK_LOC_HEINE[rnd][1]
            ret[2] = GETBACK_MAP_HEINE
        elif town_id == TOWNID_WERLDAN:
            rnd = random.randrange(len(GETBACK_LOC_WERLDAN))
            ret[0] = GETBACK_LOC_WERLDAN[rnd][0]
            ret[1] = GETBACK_LOC_WERLDAN[rnd][1]
            ret[2] = GETBACK_MAP_WERLDAN
        elif town_id == TOWNID_OREN:
            rnd = random.randrange(len(GETBACK_LOC_OREN))
            ret[0] = GETBACK_LOC_OREN[rnd][0]
            ret[1] = GETBACK_LOC_OREN[rnd][1]
            ret[2] = GETBACK_MAP_OREN
        elif town_id == TOWNID_ELVEN_FOREST:
            rnd = random.randrange(len(GETBACK_LOC_ELVEN_FOREST))
            ret[0] = GETBACK_LOC_ELVEN_FOREST[rnd][0]
            ret[1] = GETBACK_LOC_ELVEN_FOREST[rnd][1]
            ret[2] = GETBACK_MAP_ELVEN_FOREST
        elif town_id == TOWNID_ADEN:
            rnd = random.randrange(len(GETBACK_LOC_ADEN))
            ret[0] = GETBACK_LOC_ADEN[rnd][0]
            ret[1] = GETBACK_LOC_ADEN[rnd][1]
            ret[2] = GETBACK_MAP_ADEN
        elif town_id == TOWNID_SILENT_CAVERN:
            rnd = random.randrange(len(GETBACK_LOC_SILENT_CAVERN))
            ret[0] = GETBACK_LOC_SILENT_CAVERN[rnd][0]
            ret[1] = GETBACK_LOC_SILENT_CAVERN[rnd][1]
            ret[2] = GETBACK_MAP_SILENT_CAVERN
        elif town_id == TOWNID_OUM_DUNGEON:
            rnd = random.randrange(len(GETBACK_LOC_OUM_DUNGEON))
            ret[0] = GETBACK_LOC_OUM_DUNGEON[rnd][0]
            ret[1] = GETBACK_LOC_OUM_DUNGEON[rnd][1]
            ret[2] = GETBACK_MAP_OUM_DUNGEON
        elif town_id == TOWNID_RESISTANCE:
            rnd = random.randrange(len(GETBACK_LOC_RESISTANCE))
            ret[0] = GETBACK_LOC_RESISTANCE[rnd][0]
            ret[1] = GETBACK_LOC_RESISTANCE[rnd][1]
            ret[2] = GETBACK_MAP_RESISTANCE
        elif town_id == TOWNID_PIRATE_ISLAND:
            rnd = random.randrange(len(GETBACK_LOC_PIRATE_ISLAND))
            ret[0] = GETBACK_LOC_PIRATE_ISLAND[rnd][0]
            ret[1] = GETBACK_LOC_PIRATE_ISLAND[rnd][1]
            ret[2] = GETBACK_MAP_PIRATE_ISLAND
        elif town_id == TOWNID_RECLUSE_VILLAGE:
            rnd = random.randrange(len(GETBACK_LOC_RECLUSE_VILLAGE))
            ret[0] = GETBACK_LOC_RECLUSE_VILLAGE[rnd][0]
            ret[1] = GETBACK_LOC_RECLUSE_VILLAGE[rnd][1]
            ret[2] = GETBACK_MAP_RECLUSE_VILLAGE
        else:
            rnd = random.randrange(len(GETBACK_LOC_SILVER_KNIGHT_TOWN))
            ret[0] = GETBACK_LOC_SILVER_KNIGHT_TOWN[rnd][0]
            ret[1] = GETBACK_LOC_SILVER_KNIGHT_TOWN[rnd][1]
            ret[2] = GETBACK_MAP_SILVER_KNIGHT_TOWN

    @classmethod
    def getTownTaxRateByNpcid(cls, npcid):
        pass

    @classmethod
    def getTownIdByNpcid(cls, npcid):
        '''
        获取NPC所在的村庄所在的地图
        :param npcid:NPC标识
        :return:地图ID
        '''
        town_id = 0
        if npcid in (70528, 50015, 70010, 70011, 70012, 70014, 70532, 70536):
            town_id = TOWNID_TALKING_ISLAND
        elif npcid in (70799, 50056, 70073, 70074, 70075):
            town_id = TOWNID_SILVER_KNIGHT_TOWN
        elif npcid in (70546, 50020, 70018, 70016, 70544):
            town_id = TOWNID_KENT
        elif npcid in (70567, 50024, 70019, 70020, 70021, 70022, 70024):
            town_id = TOWNID_GLUDIO
        elif npcid in (70815, 70079, 70836):
            town_id = TOWNID_ORCISH_FOREST
        elif npcid in (70774, 50054, 70070, 70071, 70072, 70773):
            town_id = TOWNID_WINDAWOOD
        elif npcid in (70594, 50036, 70026, 70028, 70029, 70030, 70031, 70032, 70033, 70038, 70039, 70043, 70617, 70632):
            town_id = TOWNID_GIRAN
        elif npcid in (70860, 50066, 70082, 70083, 70084, 70873):
            town_id = TOWNID_HEINE
        elif npcid in (70654, 50039, 70045, 70044, 70664):
            town_id = TOWNID_WERLDAN
        elif npcid in (70748, 50051, 70059, 70060, 70061, 70062, 70063, 70065, 70066, 70067, 70068, 70749):
            town_id = TOWNID_OREN
        elif npcid in (50044, 70057, 70048, 70052, 70053, 70049, 70051, 70047, 70058, 70054, 70055, 70056):
            town_id = TOWNID_ADEN
        elif npcid in (70092, 70093):
            town_id = TOWNID_OUM_DUNGEON

        return town_id