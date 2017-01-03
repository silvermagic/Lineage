# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_Unknown2(ServerBasePacket):
    def __init__(self):
        ServerBasePacket.__init__(self)
