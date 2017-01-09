# -*- coding: utf-8 -*-

import logging
from Datatables import Session,armor_set
from server.templates.ArmorSets import ArmorSets
from server.utils.Singleton import Singleton

class ArmorSetTable:
    __metaclass__ = Singleton
    def __init__(self):
        self._armorSetList = []
        self.loadArmorSet()

    def loadArmorSet(self):
        with Session() as session:
            for rs in session.query(armor_set).all():
                item = ArmorSets()
                item._id = rs.id
                item._sets = rs.sets
                item._polyId = rs.polyid
                item._ac = rs.ac
                item._hp = rs.hp
                item._mp = rs.mp
                item._hpr = rs.hpr
                item._mpr = rs.mpr
                item._mr = rs.mr
                item._str = rs.str
                item._dex = rs.dex
                item._con = rs.con
                item._wis = rs.wis
                item._cha = rs.cha
                item._int = rs.intl
                item._defenseWater = rs.defense_water
                item._defenseWind = rs.defense_wind
                item._defenseFire = rs.defense_fire
                item._defenseEarth = rs.defense_earth
                self._armorSetList.append(item)