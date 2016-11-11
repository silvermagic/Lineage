# -*- coding: utf-8 -*-

import os
from ..codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CommonNews(ServerBasePacket):
    def __init__(self, message = None):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_COMMONNEWS)
        if not message:
            message = ''
            try:
                with open('data/announcements.txt', 'r') as fd:
                    for line in fd:
                        message += line
            except:
                pass
            self.writeS(message)
        else:
            self.writeS(message)


    def getContent(self):
        return self.getBytes()