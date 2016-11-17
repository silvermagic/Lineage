# -*- coding: utf-8 -*-

from server.serverpackets.S_ServerVersion import S_ServerVersion
from ClientBasePacket import ClientBasePacket

class C_ServerVersion(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)
        client.sendPacket(S_ServerVersion())
