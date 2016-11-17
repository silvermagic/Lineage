# -*- coding: utf-8 -*-

from Config import Config
from server.Account import Account
from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_CharAmount(ServerBasePacket):
    def __init__(self, value, client):
        ServerBasePacket.__init__(self)
        account = Account.load(client._account._name)
        maxAmount = Config.getint('altsettings', 'DefaultCharacterSlot') + account._characterSlot
        self.writeC(Opcodes.S_OPCODE_CHARAMOUNT)
        self.writeC(value)
        self.writeC(maxAmount)

    def getContent(self):
        return self.getBytes()