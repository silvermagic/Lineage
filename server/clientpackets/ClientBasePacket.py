# -*- coding: utf-8 -*-

import struct,logging
from Config import Config

class ClientBasePacket:
    def __init__(self, abyte):
        self._decrypt = abyte
        self._off = 1

    def readD(self):
        ret = struct.unpack_from('<i', self._decrypt, self._off)
        self._off += 4
        return  int(ret[0])

    def readC(self):
        ret = struct.unpack_from('<b', self._decrypt, self._off)
        self._off += 1
        return int(ret[0])

    def readH(self):
        ret = struct.unpack_from('<h', self._decrypt, self._off)
        self._off += 2
        return  int(ret[0])

    def readCH(self):
        ret = struct.unpack_from('<i', self._decrypt, self._off)
        self._off += 3
        return  int(ret[0] & 0x00ffffff)

    def readF(self):
        ret = struct.unpack_from('<d', self._decrypt, self._off)
        self._off += 8
        return  float(ret[0])

    def readS(self):
        ret = None
        try:
            s = self._decrypt[self._off:]
            end = s.index(b'\0')
            ret = s[:end]
            self._off += len(ret) + 1
            ret = str(ret.decode(Config.get('server', 'ClientLanguageCode')))
        except Exception as e:
            logging.error(e)

        return ret

    def readByte(self):
        ret = self._decrypt[self._off:]
        self._off = len(self._decrypt)
        return ret

    def getType(self):
        return self.__class__.__name__
