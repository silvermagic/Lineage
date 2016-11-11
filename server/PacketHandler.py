# -*- coding: utf-8 -*-

from clientpackets.C_AuthLogin import C_AuthLogin
from clientpackets.C_ServerVersion import C_ServerVersion
from clientpackets.C_CommonClick import C_CommonClick
from server.codes import Opcodes

class PacketHandler:
    def __init__(self, client):
        self._client = client

    def handlePacket(self, abytes, pc):
        opcode = abytes[0]
        if opcode == Opcodes.C_OPCODE_CLIENTVERSION:
            C_ServerVersion(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_LOGINPACKET:
            C_AuthLogin(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_COMMONCLICK:
            C_CommonClick(abytes, self._client)
        else:
            pass

