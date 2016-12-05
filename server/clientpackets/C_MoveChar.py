# -*- coding: utf-8 -*-

from ClientBasePacket import ClientBasePacket

class C_MoveChar(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)
        pass

