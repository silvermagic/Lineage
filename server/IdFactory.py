# -*- coding: utf-8 -*-

import threading
from sqlalchemy import func
from Datatables import Session,characters,character_items,character_teleport,character_warehouse,character_elf_warehouse,clan_data,clan_warehouse,pets
from utils.Singleton import Singleton

class IdFactory():
    __metaclass__ = Singleton
    def __init__(self):
        with Session() as session:
            self._curId = max(session.query(func.max(characters.objid)).scalar(),
                     session.query(func.max(character_items.id)).scalar(),
                     session.query(func.max(character_teleport.id)).scalar(),
                     session.query(func.max(character_warehouse.id)).scalar(),
                     session.query(func.max(character_elf_warehouse.id)).scalar(),
                     session.query(func.max(clan_data.clan_id)).scalar(),
                     session.query(func.max(clan_warehouse.id)).scalar(),
                     session.query(func.max(pets.objid)).scalar(),
                     0x10000000)
        self._lock = threading.Lock()

    def nextId(self):
        '''
        产生新的天堂对象ID
        :return:对象ID
        '''
        with self._lock:
            self._curId += 1
            return self._curId


