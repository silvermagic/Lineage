# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from server.MapReader import MapReader
from server.utils.Singleton import Singleton

class WorldMap():
    __metaclass__ = Singleton
    def __init__(self):
        logging.info("loading map...")
        start = datetime.now()
        fd = MapReader.getDefaultReader()
        try:
            self._maps = fd.read()
        except Exception as e:
            logging.error(e)
        end = datetime.now()
        logging.info('OK! ' + str(int((end - start).total_seconds() * 1000)) + 'ms')
