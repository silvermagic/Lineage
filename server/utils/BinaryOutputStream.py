# -*- coding: utf-8 -*-

import struct,logging
from Config import Config

class BinaryOutputStream():
    '''
    转化数据成二进制流
    '''
    def __init__(self):
        self._bao = bytearray()

    def writeD(self, value):
        self._bao += struct.pack('<I', value)

    def writeH(self, value):
        self._bao += struct.pack('<H', value)

    def writeC(self, value):
        self._bao += struct.pack('<B', value)

    def writeL(self, value):
        self._bao += struct.pack('<L', value & 0xFF)

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
        return self._bao