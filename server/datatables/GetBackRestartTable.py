# -*- coding: utf-8 -*-

import logging
from Datatables import Session,getback_restart
from server.templates.GetBackRestart import GetBackRestart
from server.utils.Singleton import Singleton

class GetBackRestartTable():
    __metaclass__ = Singleton
    def __init__(self):
        self._getbackrestart = {}
        try:
            with Session() as session:
                for rs in session.query(getback_restart).all():
                    item = GetBackRestart()
                    item._area = rs.area
                    item._locX = rs.locx
                    item._locY = rs.locy
                    item._mapId = rs.mapid
        except Exception as e:
            logging.error(e)