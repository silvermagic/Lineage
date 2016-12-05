# -*- coding: utf-8 -*-

import struct,logging,ctypes
from Config import Config

class ServerBasePacket:
    def __init__(self):
        self._bao = bytearray()

    def writeD(self, value):
        self._bao += struct.pack('<I', value)

    def writeH(self, value):
        self._bao += struct.pack('<H', value)

    def writeC(self, value):
        self._bao += struct.pack('<B', value & 0xFF)

    def writeL(self, value):
        self._bao += struct.pack('<L', int(value & 0xFF))

    def writeF(self, value):
        self._bao += struct.pack('<Q', value)

    def writeS(self, value):
        try:
            if len(value) > 0:
                self._bao += value.encode(Config.get('server', 'ClientLanguageCode'))
            self._bao += b'\0'
        except Exception as e:
            logging.error(e)

    def writeByte(self, value):
        self._bao += value

    def getLength(self):
        return len(self._bao) + 2

    def getBytes(self):
        length = len(self._bao)
        if  length == 0:
            self.writeByte(b'\0' * 4)
        else:
            padding = length % 4
            if padding != 0:
                self.writeByte(b'\0' * (4 - padding))

        return self._bao

    def getContent(self):
        return self._bao

    def getType(self):
        return self.__class__.__name__