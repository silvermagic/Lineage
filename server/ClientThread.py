# -*- coding: utf-8 -*-

import random,logging,struct
from Queue import Queue
from threading import Thread
from Config import Config
from codes import Opcodes
from Cipher import Cipher
from PacketHandler import PacketHandler
from serverpackets.S_Disconnect import S_Disconnect
from utils.ByteArrayUtil import ByteArrayUtil

# 3.5C Taiwan Server
_FIRST_PACKET = bytearray([0xf4, 0x0a, 0x8d, 0x23, 0x6f, 0x7f, 0x04, 0x00, 0x05, 0x08, 0x00])
M_CAPACITY = 3
H_CAPACITY = 2

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
        self._active = True

    def readPacket(self):
        '''
        读取客户端发送的数据包并解密
        :return:解密后的客户端数据包(bytes)
        '''
        data = bytearray(self._csocket.recv(2))
        if not data:
            raise Exception('Recv Error')

        length, = struct.unpack('<h', data)
        length -= 2
        if length <=0 or length > 65533:
            raise Exception('No content')

        buf = bytearray()
        while len(buf) < length:
            # 移动数据包比较特殊,一个数据包里面包含三个移动封包,所以要按长度来读取,不能一次性读将数据包取完
            data = bytearray(self._csocket.recv(length - len(buf)))
            if not data:
                break
            buf += data
        if len(buf) != length:
            raise Exception("Length Error")

        logging.debug('[Recv Encrypt C]' + '\n' + ByteArrayUtil.dumpToString(bytearray(buf)))
        return self._cipher.decrypt(buf)

    def sendPacket(self, packet):
        '''
        加密并发送数据包到客户端
        :param packet:未加密的数据包(bytes)
        :return:None
        '''
        try:
            data = bytearray(packet.getContent())
            if len(data) == 0:
                return
            logging.debug('[Send C]' + '\n' + ByteArrayUtil.dumpToString(data))
            data = self._cipher.encrypt(data)
            logging.debug('[Send Encrypt C]' + '\n' + ByteArrayUtil.dumpToString(data))
            data = struct.pack('<H', len(data) + 2) + data
            self._csocket.sendall(data)
        except:
            pass

    def run(self):
        '''
        接受并处理客户端发送的数据包
        :return:None
        '''
        # 移动封包和行为封包另起线程处理
        movePacket = HcPacket(self, M_CAPACITY)
        hcPacket = HcPacket(self, H_CAPACITY)
        movePacket.start()
        hcPacket.start()
        try:
            # 初始包格式:长度+操作码+密钥+数据
            bogus = len(_FIRST_PACKET) + 7
            # key = random.randrange(2147483647) + 1
            key = 2147483647
            data = struct.pack('<HBI', bogus, Opcodes.S_OPCODE_INITPACKET, key) + _FIRST_PACKET
            self._csocket.sendall(data)

            # 密钥初始化
            self._cipher = Cipher(key)

            # 处理客户端数据包
            while self._active:
                data = self.readPacket()
                logging.debug('[Recv C]' + '\n' + ByteArrayUtil.dumpToString(bytearray(data)))
                opcode = data[0] & 0xFF

                if opcode == Opcodes.C_OPCODE_COMMONCLICK or opcode == Opcodes.C_OPCODE_CHANGECHAR:
                    self._loginStatus = 1
                if opcode == Opcodes.C_OPCODE_LOGINTOSERVER and self._loginStatus != 1:
                    continue
                if opcode == Opcodes.C_OPCODE_LOGINTOSERVEROK or opcode == Opcodes.C_OPCODE_RETURNTOLOGIN:
                    self._loginStatus = 0

                if opcode != Opcodes.C_OPCODE_KEEPALIVE:
                    pass
                if opcode == Opcodes.C_OPCODE_QUITGAME:
                    break

                if not self._activeChar:
                    self._handler.handlePacket(data, self._activeChar)
                    continue

                if opcode in (Opcodes.C_OPCODE_CHANGECHAR, Opcodes.C_OPCODE_DROPITEM, Opcodes.C_OPCODE_DELETEINVENTORYITEM):
                    self._handler.handlePacket(data, self._activeChar)
                elif opcode == Opcodes.C_OPCODE_MOVECHAR:
                    movePacket.requestWork(data)
                else:
                    hcPacket.requestWork(data)

        except Exception as e:
            logging.error(e)
        finally:
            try:
                if self._activeChar:
                    self.quitGame()
                    self._activeChar.logout()
                    self._activeChar = None
                self.sendPacket(S_Disconnect())
                self._active = False
            except Exception as e:
                logging.error(e)

        movePacket.join()
        hcPacket.join()

    def kick(self):
        '''
        断开当前连接
        :return:None
        '''
        self.sendPacket(S_Disconnect())
        self._active = False

    def quitGame(self):
        '''
        退出游戏
        :return:None
        '''
        self._active = False

class HcPacket(Thread):
    def __init__(self, client, capacity = None):
        Thread.__init__(self)
        self._client = client
        if not capacity:
            self._queue = Queue()
        else:
            self._queue = Queue(capacity)

    def run(self):
        '''
        获取并处理队列中的数据包
        :return:None
        '''
        while self._client._active:
            try:
                data = self._queue.get(True, 10)
                self._client._handler.handlePacket(data, self._client._activeChar)
                self._queue.task_done()
            except Exception as e:
                logging.error(e)
        return

    def requestWork(self, data):
        '''
        添加数据包到待处理队列中
        :param data:待处理的数据包(bytes)
        :return:None
        '''
        try:
            self._queue.put(data)
        except Exception as e:
            logging.error(e)