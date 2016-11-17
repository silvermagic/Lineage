# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CommonNews(ServerBasePacket):
    def __init__(self, message = None):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_COMMONNEWS)
        if not message:
            message = ''
            try:
                for line in open('data/announcements.txt', 'rU'):
                    message += line
            except:
                pass
            self.writeS(message)
        else:
            self.writeS(message)


    def getContent(self):
        return self.getBytes()