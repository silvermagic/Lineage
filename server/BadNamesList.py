# -*- coding: utf-8 -*-

import logging
from utils.Singleton import Singleton

class BadNamesList():
    __metaclass__ =  Singleton
    def __init__(self):
        self._nameList = []
        try:
            with open('data/badnames.txt', 'r') as fd:
                for line in fd:
                    if len(line.strip()) == 0 or line.startswith('#'):
                        continue

                    self._nameList += line.split(';')
        except Exception as e:
            logging.error(e)

    def isBadName(self, name):
        '''
        检测用户注册的用户名的有效性
        :param name:用户名(str)
        :return:True/False
        '''
        for item in self._nameList:
            if name.lower() == item.lower():
                return True
        return False
