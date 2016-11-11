# -*- coding: utf-8 -*-

import random,logging,struct
from threading import Thread
from Config import Config
from codes import Opcodes
from Cipher import Cipher
from PacketHandler import PacketHandler
from serverpackets.S_Disconnect import S_Disconnect
from utils.ByteArrayUtil import ByteArrayUtil

# 3.5C Taiwan Server
_FIRST_PACKET = bytearray([0xf4, 0x0a, 0x8d, 0x23, 0x6f, 0x7f, 0x04, 0x00, 0x05, 0x08, 0x00])

class ClientThread(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self._csocket = socket
        self._ip = socket.getpeername()[0]
        if Config.getboolean('server', 'HostnameLookups'):
            self._hostname = socket.gethostbyaddr(self._ip)[0]
        else:
            self._hostname = self._ip

        self._handler = PacketHandler(self)
        self._account = None
        self._activeChar = None
        self._loginStatus = 0

    def readPacket(self):
        data = bytearray(self._csocket.recv(1024))
        if not data:
            raise Exception("Recv Error")

        length, = struct.unpack('<h', data[0:2])
        length -= 2
        if length <=0 or length > 65533:
            raise RuntimeError()

        buf = data[2:]
        while len(buf) < length:
            data = bytearray(self._csocket.recv(1024))
            if not data:
                break
            buf += data
        if len(buf) != length:
            raise RuntimeError()

        return self._cipher.decrypt(buf)

    def sendPacket(self, packet):
        data = bytearray(packet.getContent())
        logging.debug('Send Packet:' + '\n' + ByteArrayUtil.dumpToString(data))
        data = self._cipher.encrypt(data)
        data = struct.pack('<H', len(data) + 2) + data
        self._csocket.sendall(data)

    def run(self):
        try:
            # 初始包格式:长度+操作码+密钥+数据
            bogus = len(_FIRST_PACKET) + 7
            key = random.randrange(2147483647) + 1
            data = struct.pack('<HBI', bogus, Opcodes.S_OPCODE_INITPACKET, key) + _FIRST_PACKET
            self._csocket.sendall(data)
            logging.debug('\n' + ByteArrayUtil.dumpToString(bytearray(data)))

            # 密钥初始化
            self._cipher = Cipher(key)

            # 处理客户端数据包
            while True:
                data = self.readPacket()
                logging.debug('Receive Packet:' + '\n' + ByteArrayUtil.dumpToString(bytearray(data)))
                opcode = data[0] & 0xFF

                if opcode == Opcodes.C_OPCODE_COMMONCLICK or opcode == Opcodes.C_OPCODE_CHANGECHAR:
                    self._loginStatus = 1
                if opcode == Opcodes.C_OPCODE_LOGINTOSERVER and self._loginStatus != 1:
                    continue
                if opcode == Opcodes.C_OPCODE_LOGINTOSERVEROK or opcode == Opcodes.C_OPCODE_RETURNTOLOGIN:
                    self._loginStatus = 0

                if opcode == Opcodes.C_OPCODE_KEEPALIVE:
                    pass
                if opcode == Opcodes.C_OPCODE_QUITGAME:
                    break

                if not self._activeChar:
                    self._handler.handlePacket(data, self._activeChar)
                    continue

        except Exception as e:
            logging.error(e)
        finally:
            if self._activeChar:
                pass
            self.sendPacket(S_Disconnect())

    def kick(self):
        self.sendPacket(S_Disconnect())