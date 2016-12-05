# -*- coding: utf-8 -*-

import threading
from sqlalchemy import func
from Datatables import Session,Characters,Character_Items,Character_Teleport,Character_Warehouse,Character_Elf_Warehouse,Clan_Data, Clan_Warehouse,Pets
from utils.Singleton import Singleton

class IdFactory():
    __metaclass__ = Singleton
    def __init__(self):
        with Session() as session:
            self._curId = max(session.query(func.max(Characters.objid)).scalar(),
                     session.query(func.max(Character_Items.id)).scalar(),
                     session.query(func.max(Character_Teleport.id)).scalar(),
                     session.query(func.max(Character_Warehouse.id)).scalar(),
                     session.query(func.max(Character_Elf_Warehouse.id)).scalar(),
                     session.query(func.max(Clan_Data.clan_id)).scalar(),
                     session.query(func.max(Clan_Warehouse.id)).scalar(),
                     session.query(func.max(Pets.objid)).scalar(),
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


