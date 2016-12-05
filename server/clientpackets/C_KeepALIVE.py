# -*- coding: utf-8 -*-

from server.serverpackets.S_GameTime import S_GameTime
from ClientBasePacket import ClientBasePacket

class C_KeepALIVE(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)

