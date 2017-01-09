# -*- coding: utf-8 -*-

import logging
from server.model.Instance.ItemInstance import ItemInstance
from server.model.World import World
from server.templates.EtcItem import EtcItem
from server.templates.Weapon import Weapon
from server.templates.Armor import Armor
from server.utils.Singleton import Singleton
from server.IdFactory import IdFactory
from Datatables import Session,etcitem,weapon,armor

_etcItemTypes = {'arrow': 0, 'wand': 1, 'light': 2, 'gem': 3, 'totem': 4, 'firecracker': 5, 'potion': 6, 'food': 7,
                 'scroll': 8, 'questitem': 9, 'spellbook': 10, 'petitem': 11, 'other': 12, 'material': 13, 'event': 14,
                 'sting': 15, 'treasure_box': 16, 'magic_doll': 17, 'scrollshop': 18, 'TeleportScroll': 19}

_useTypes = {'none': -1, 'normal': 0, 'weapon': 1, 'armor': 2, 'spell_long': 5, 'ntele': 6, 'identify': 7, 'res': 8,
             'letter': 12, 'letter_w': 13, 'choice': 14, 'instrument': 15, 'sosc': 16, 'spell_short': 17, 'T': 18,
             'cloak': 19, 'glove': 20, 'boots': 21, 'helm': 22, 'ring': 23, 'amulet': 24, 'shield': 25, 'guarder': 25,
             'dai': 26, 'zel': 27, 'blank': 28, 'btele': 29, 'spell_buff': 30, 'ccard': 31, 'ccard_w': 32, 'vcard': 33,
             'vcard_w': 34, 'wcard': 35, 'wcard_w': 36, 'belt': 37, 'earring': 40, 'fishing_rod': 42, 'del': 46}

_armorTypes = {'none': 0, 'helm': 1, 'armor': 2, 'T': 3, 'cloak': 4, 'glove': 5, 'boots': 6, 'shield': 7,
               'amulet': 8, 'ring': 9, 'belt': 10, 'ring2': 11, 'earring': 12, 'guarder': 13}

_weaponTypes = {'sword': 1, 'dagger': 2, 'tohandsword': 3, 'bow': 4, 'spear': 5, 'blunt': 6, 'staff': 7,
               'throwingknife': 8, 'arrow': 9, 'gauntlet': 10, 'claw': 11, 'edoryu': 12, 'singlebow': 13,
               'singlespear': 14, 'tohandblunt': 15, 'tohandstaff': 16, 'kiringku': 17, 'chainsword': 18}

_weaponId = {'sword': 4, 'dagger': 46, 'tohandsword': 50, 'bow': 20, 'blunt': 11, 'spear': 24, 'staff': 40,
             'throwingknife': 2922, 'arrow': 66, 'gauntlet': 62, 'claw': 58, 'edoryu': 54, 'singlebow': 20,
             'singlespear': 24, 'tohandblunt': 11, 'tohandstaff': 40, 'kiringku': 58, 'chainsword': 24}

_materialTypes = {'none': 0, 'liquid': 1, 'web': 2, 'vegetation': 3, 'animalmatter': 4, 'paper': 5, 'cloth': 6,
                  'leather': 7, 'wood': 8, 'bone': 9, 'dragonscale': 10, 'iron': 11, 'steel': 12, 'copper': 13,
                  'silver': 14, 'gold': 15, 'platinum': 16, 'mithril': 17, 'blackmithril': 18, 'glass': 19,
                  'gemstone': 20, 'mineral': 21, 'oriharukon': 22}

class ItemTable():
    __metaclass__ = Singleton
    def __init__(self):
        self._etcitems = {}
        self._weapons = {}
        self._armors = {}
        self._loadEtcItem()
        self._loadWeapon()
        self._loadArmor()
        self._allTemplates = {}
        self._allTemplates.update(self._etcitems)
        self._allTemplates.update(self._weapons)
        self._allTemplates.update(self._armors)

    def _loadEtcItem(self):
        '''
        加载材料道具模板到内存
        :return:None
        '''
        try:
            with Session() as session:
                for rs in session.query(etcitem).all():
                    item = EtcItem()
                    item._itemId = rs.item_id
                    item._name = rs.name
                    item._unidentifiedNameId = rs.unidentified_name_id
                    item._identifiedNameId = rs.identified_name_id
                    item._type = _etcItemTypes[rs.item_type]
                    item._useType = _useTypes[rs.use_type]
                    item._clsType = 0
                    item._material = _materialTypes[rs.material]
                    item._weight = rs.weight
                    item._gfxId = rs.invgfx
                    item._groundGfxId = rs.grdgfx
                    item._itemDescId = rs.itemdesc_id
                    item._minLevel = rs.min_lvl
                    item._maxLevel = rs.max_lvl
                    item._bless = rs.bless
                    item._tradable = rs.trade == 0
                    item._cantDelete = rs.cant_delete == 1
                    item._isCanSeal = rs.can_seal == 1
                    item._dmgSmall = rs.dmg_small
                    item._dmgLarge = rs.dmg_large
                    item._stackable = rs.stackable == 1
                    item._maxChargeCount = rs.max_charge_count
                    item._locx = rs.locx
                    item._locy = rs.locy
                    item._mapid = rs.mapid
                    item._delay_id = rs.delay_id
                    item._delay_time = rs.delay_time
                    item._delay_effect = rs.delay_effect
                    item._foodVolume = rs.food_volume
                    item._save_at_once = rs.save_at_once == 1

                    self._etcitems[item._itemId] = item
        except Exception as e:
            logging.error(e)

    def _loadWeapon(self):
        '''
        加载武器道具模板到内存
        :return:None
        '''
        try:
            with Session() as session:
                for rs in session.query(weapon).all():
                    item = Weapon()
                    item._itemId = rs.item_id
                    item._name = rs.name
                    item._unidentifiedNameId = rs.unidentified_name_id
                    item._identifiedNameId = rs.identified_name_id
                    item._type = _weaponTypes[rs.type]
                    item._weaponType = _weaponId[rs.type]
                    item._useType = 1
                    item._clsType = 1
                    item._material = _materialTypes[rs.material]
                    item._weight = rs.weight
                    item._gfxId = rs.invgfx
                    item._groundGfxId = rs.grdgfx
                    item._itemDescId = rs.itemdesc_id
                    item._dmgSmall = rs.dmg_small
                    item._dmgLarge = rs.dmg_large
                    item._range = rs.range
                    item._safeEnchant = rs.safenchant
                    item._useRoyal = rs.use_royal != 0
                    item._useKnight = rs.use_knight != 0
                    item._useElf = rs.use_elf != 0
                    item._useMage = rs.use_mage != 0
                    item._useDarkelf = rs.use_darkelf != 0
                    item._useDragonknight = rs.use_dragonknight != 0
                    item._useIllusionist = rs.use_illusionist != 0
                    item._hitModifier = rs.hitmodifier
                    item._dmgModifier = rs.dmgmodifier
                    item._addstr = rs.add_str
                    item._adddex = rs.add_dex
                    item._addcon = rs.add_con
                    item._addwis = rs.add_int
                    item._addint = rs.add_wis
                    item._addcha = rs.add_cha
                    item._addhp = rs.add_hp
                    item._addmp = rs.add_mp
                    item._addhpr = rs.add_hpr
                    item._addmpr = rs.add_mpr
                    item._addsp = rs.add_sp
                    item._mdef = rs.m_def
                    item._doubleDmgChance = rs.double_dmg_chance
                    item._magicDmgModifier = rs.magicdmgmodifier
                    item._canbedmg = rs.canbedmg
                    item._minLevel = rs.min_lvl
                    item._maxLevel = rs.max_lvl
                    item._bless = rs.bless
                    item._tradable = rs.trade == 0
                    item._cantDelete = rs.cant_delete == 1
                    item._isHasteItem = rs.haste_item != 0
                    item._maxUseTime = rs.max_use_time

                    self._weapons[item._itemId] = item
        except Exception as e:
            logging.error(e)

    def _loadArmor(self):
        '''
        加载防具道具模板到内存
        :return:None
        '''
        try:
            with Session() as session:
                for rs in session.query(armor).all():
                    item = Armor()
                    item._itemId = rs.item_id
                    item._name = rs.name
                    item._unidentifiedNameId = rs.unidentified_name_id
                    item._identifiedNameId = rs.identified_name_id
                    item._type = _armorTypes[rs.type]
                    item._useType = _useTypes[rs.type]
                    item._clsType = 2
                    item._material = _materialTypes[rs.material]
                    item._weight = rs.weight
                    item._gfxId = rs.invgfx
                    item._groundGfxId = rs.grdgfx
                    item._itemDescId = rs.itemdesc_id
                    item._ac = rs.ac
                    item._safeEnchant = rs.safenchant
                    item._useRoyal = rs.use_royal != 0
                    item._useKnight = rs.use_knight != 0
                    item._useElf = rs.use_elf != 0
                    item._useMage = rs.use_mage != 0
                    item._useDarkelf = rs.use_darkelf != 0
                    item._useDragonknight = rs.use_dragonknight != 0
                    item._useIllusionist = rs.use_illusionist != 0
                    item._addstr = rs.add_str
                    item._adddex = rs.add_dex
                    item._addcon = rs.add_con
                    item._addwis = rs.add_wis
                    item._addint = rs.add_int
                    item._addcha = rs.add_cha
                    item._addhp = rs.add_hp
                    item._addmp = rs.add_mp
                    item._addhpr = rs.add_hpr
                    item._addmpr = rs.add_mpr
                    item._addsp = rs.add_sp
                    item._minLevel = rs.min_lvl
                    item._maxLevel = rs.max_lvl
                    item._mdef = rs.m_def
                    item._damageReduction = rs.damage_reduction
                    item._weightReduction = rs.weight_reduction
                    item._hitModifierByArmor = rs.hit_modifier
                    item._dmgModifierByArmor = rs.dmg_modifier
                    item._bowHitModifierByArmor = rs.bow_hit_modifier
                    item._bowDmgModifierByArmor = rs.bow_dmg_modifier
                    item._isHasteItem = rs.haste_item != 0
                    item._bless = rs.bless
                    item._tradable = rs.trade == 0
                    item._cantDelete = rs.cant_delete == 1
                    item._defense_earth = rs.defense_earth
                    item._defense_water = rs.defense_water
                    item._defense_wind = rs.defense_wind
                    item._defense_fire = rs.defense_fire
                    item._regist_stun = rs.regist_stun
                    item._regist_stone = rs.regist_stone
                    item._regist_sleep = rs.regist_sleep
                    item._regist_freeze = rs.regist_freeze
                    item._regist_sustain = rs.regist_sustain
                    item._regist_blind = rs.regist_blind
                    item._maxUseTime = rs.max_use_time

                    self._armors[item._itemId] = item
        except Exception as e:
            logging.error(e)

    def createItem(self, itemId):
        '''
        实例化一个道具模板,并保存到游戏世界
        :param itemId:道具模板ID(int)
        :return:道具实例(ItemInstance)
        '''
        if not self._allTemplates.has_key(itemId):
            return None

        itemInst = ItemInstance(self._allTemplates[itemId])
        itemInst._id = IdFactory().nextId()
        World().storeObject(itemInst)
        return itemInst

    def findItemIdByName(self, name):
        '''
        根据道具名称获取道具模板ID
        :param name:道具名称(str)
        :return:道具模板ID(int)
        '''
        itemId = 0
        for item in self._allTemplates:
            if item._name == name:
                itemId = item._itemId
                break

        return itemId

    def findItemIdByNameWithoutSpace(self, name):
        '''
        根据道具名称获取道具模板ID,匹配名称时忽略空格
        :param name:道具名称(str)
        :return:道具模板ID(int)
        '''
        itemId = 0
        for item in self._allTemplates:
            if item._name.replace(' ','') == name:
                itemId = item._itemId
                break

        return itemId

