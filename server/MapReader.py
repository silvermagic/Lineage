# -*- coding: utf-8 -*-

from Config import Config
from TextMapReader import TextMapReader

class MapReader():
    @classmethod
    def getDefaultReader(cls):
        if Config.getboolean('server', 'LoadV2MapFiles'):
            return None
        if Config.getboolean('server', 'LoadV2MapFiles'):
            return None

        return TextMapReader()
