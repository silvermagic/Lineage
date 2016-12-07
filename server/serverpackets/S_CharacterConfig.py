# -*- coding: utf-8 -*-

import logging
from Datatables import Session,Character_Config
from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CharacterConfig(ServerBasePacket):
    def __init__(self, objectId):
        ServerBasePacket.__init__(self)
        length = 0
        data = bytearray()
        try:
            with Session() as session:
                rs = session.query(Character_Config).filter(Character_Config.object_id == objectId).one()
                length = rs.Length
                data = rs.Data
        except Exception as e:
            logging.error(e)

        if length != 0:
            self.writeC(Opcodes.S_OPCODE_SKILLICONGFX)
            self.writeC(41)
            self.writeD(length)
            self.writeByte(data)
