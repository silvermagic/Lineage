# -*- coding: utf-8 -*-

import logging
from server.utils.Singleton import Singleton
from Datatables import Session

class SkillsTable():
    __metaclass__ = Singleton
    def __init__(self):
        return

    def spellCheck(self, playerobjid, skillid):
        return