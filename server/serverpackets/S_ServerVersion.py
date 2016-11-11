# -*- coding: utf-8 -*-

import time
from Config import Config
from ..codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_ServerVersion(ServerBasePacket):
    def __init__(self):
        ServerBasePacket.__init__(self)
        self.writeC(Opcodes.S_OPCODE_SERVERVERSION)
        self.writeC(0x00)
        self.writeC(0x02)
        self.writeD(0x00a8c732)  # server verion 3.5C Taiwan Server
        self.writeD(0x00a8c6a7)  # cache verion 3.5C Taiwan Server
        self.writeD(0x77cf6eba)  # auth verion 3.5C Taiwan Server
        self.writeD(0x00a8cdad)  # npc verion 3.5C Taiwan Server
        self.writeD(int(time.time()))
        self.writeC(0x00)
        self.writeC(0x00)
        self.writeC(Config.getint('server', 'ClientLanguage'))  # Country: 0.US 3.Taiwan 4.Janpan 5.China
        self.writeD(0x00000000)
        self.writeC(0xae)
        self.writeC(0xb2)
