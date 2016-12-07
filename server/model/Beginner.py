# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from Datatables import Session,beginner,character_items
from server.IdFactory import IdFactory
from server.utils.Singleton import Singleton

class Beginner():
    __metaclass__ = Singleton
    def GiveItem(self, pc):
        try:
            cond = ['A']
            if pc.isCrown():
                cond.append('P')
            elif pc.isKnight():
                cond.append('K')
            elif pc.isElf():
                cond.append('E')
            elif pc.isWizard():
                cond.append('W')
            elif pc.isDarkelf():
                cond.append('D')
            elif pc.isDragonKnight():
                cond.append('R')
            elif pc.isIllusionist():
                cond.append('I')
            else:
                cond.append('A')
            with Session() as session:
                for rs in session.query(beginner).filter(beginner.activate.in_(cond)).all():
                    item = character_items()
                    item.id = IdFactory().nextId()
                    item.item_id = rs.item_id
                    item.char_id = pc._id
                    item.item_name = rs.item_name
                    item.count = rs.count
                    item.is_equipped = 0
                    item.enchantlvl = rs.enchantlvl
                    item.is_id = 0
                    item.durability = 0
                    item.charge_count = rs.charge_count
                    item.remaining_time = 0
                    item.last_used = datetime.now()
                    item.bless = 1
                    session.add(item)
        except Exception as e:
            logging.error(e)