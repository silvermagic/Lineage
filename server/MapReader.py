# -*- coding: utf-8 -*-

from Config import Config
from TextMapReader import TextMapReader

class MapReader():
    '''
    地图信息读取器管理
    '''
    @classmethod
    def getDefaultReader(cls):
        '''
        获取默认的地图信息读取器
        :return:地图信息读取器
        '''
        if Config.getboolean('server', 'LoadV2MapFiles'):
            return None
        if Config.getboolean('server', 'LoadV2MapFiles'):
            return None

        return TextMapReader()
