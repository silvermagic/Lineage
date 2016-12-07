# -*- coding: utf-8 -*-

from clientpackets.C_AuthLogin import C_AuthLogin
from clientpackets.C_ServerVersion import C_ServerVersion
from clientpackets.C_CommonClick import C_CommonClick
from clientpackets.C_CreateChar import C_CreateChar
from clientpackets.C_LoginToServer import C_LoginToServer
from clientpackets.C_KeepALIVE import C_KeepALIVE
from clientpackets.C_LoginToServerOK import C_LoginToServerOK
from server.codes import Opcodes

class PacketHandler:
    def __init__(self, client):
        self._client = client

    def handlePacket(self, abytes, pc):
        '''
        处理客户端发送的数据包
        :param abytes:解密后的数据包(bytes)
        :param pc:玩家角色信息(PcInstance)
        :return:None
        '''
        opcode = abytes[0]
        if opcode == Opcodes.C_OPCODE_CLIENTVERSION:
            C_ServerVersion(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_LOGINPACKET:
            C_AuthLogin(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_COMMONCLICK:
            C_CommonClick(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_NEWCHAR:
            C_CreateChar(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_LOGINTOSERVER:
            C_LoginToServer(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_KEEPALIVE:
            C_KeepALIVE(abytes, self._client)
        elif opcode == Opcodes.C_OPCODE_LOGINTOSERVEROK:
            C_LoginToServerOK(abytes, self._client)
        else:
            pass

