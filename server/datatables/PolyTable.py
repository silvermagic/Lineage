# -*- coding: utf-8 -*-

import logging
from Datatables import Session,polymorphs
from server.templates.PolyMorphs import PolyMorphs
from server.utils.Singleton import Singleton

class PolyTable:
    __metaclass__ = Singleton
    def __init__(self):
        self._polymorphs = {}
        self._polyIdIndex = {}
        self.loadPolymorphs()

    def loadPolymorphs(self):
        with Session() as session:
            for rs in session.query(polymorphs).all():
                item = PolyMorphs()
                item._id = rs.id
                item._name = rs.name
                item._polyId = rs.polyid
                item._minLevel = rs.minlevel
                item._weaponEquipFlg = rs.weaponequip
                item._armorEquipFlg = rs.armorequip
                item._canUseSkill = rs.isSkillUse
                item._causeFlg = rs.cause
                self._polymorphs[item._name] = item
                self._polyIdIndex[item._polyId] = item
        logging.info("变身总清单" + str(len(self._polymorphs)) + "件")
