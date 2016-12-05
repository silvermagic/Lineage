# -*- coding: utf-8 -*-

from ClientBasePacket import ClientBasePacket

class C_LoginToServerOK(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)
        type = self.readC()
        button = self.readC()
        pc = client._activeChar

        if type == 255:
            if button == 95 or button == 127:
                pc._isShowWorldChat = True
                pc._isCanWhisper = True
            elif button == 91 or button == 123:
                pc._isShowWorldChat = True
                pc._isCanWhisper = False
            elif button == 94 or button == 126:
                pc._isShowWorldChat = False
                pc._isCanWhisper = True
            elif button == 90 or button == 122:
                pc._isShowWorldChat = False
                pc._isCanWhisper = False
        elif type == 0:
            if button == 0:
                pc._isShowWorldChat = False
            elif button == 1:
                pc._isShowWorldChat = True
        elif type == 6:
            if button == 0:
                pc._isShowWorldChat = False
            elif button == 1:
                pc._isShowWorldChat = True
