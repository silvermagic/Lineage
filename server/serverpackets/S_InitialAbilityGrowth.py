# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

class S_InitialAbilityGrowth(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        str = 0
        dex = 0
        con = 0
        wis = 0
        cha = 0
        int = 0
        originStr = pc._originalStr
        originDex = pc._originalDex
        originCon = pc._originalCon
        originWis = pc._originalWis
        originCha = pc._originalCha
        originInt = pc._originalInt

        # 王族
        if pc.isCrown():
            str = originStr - 13
            dex = originDex - 10
            con = originCon - 10
            wis = originWis - 11
            cha = originCha - 13
            int = originInt - 10

        # 法師
        if pc.isWizard():
            str = originStr - 8
            dex = originDex - 7
            con = originCon - 12
            wis = originWis - 12
            cha = originCha - 8
            int = originInt - 12

        # 騎士
        if pc.isKnight():
            str = originStr - 16
            dex = originDex - 12
            con = originCon - 14
            wis = originWis - 9
            cha = originCha - 12
            int = originInt - 8

        # 妖精
        if pc.isElf():
            str = originStr - 11
            dex = originDex - 12
            con = originCon - 12
            wis = originWis - 12
            cha = originCha - 9
            int = originInt - 12

        # 黑妖
        if pc.isDarkelf():
            str = originStr - 12
            dex = originDex - 15
            con = originCon - 8
            wis = originWis - 10
            cha = originCha - 9
            int = originInt - 11

        # 龍騎士
        if pc.isDragonKnight():
            str = originStr - 13
            dex = originDex - 11
            con = originCon - 14
            wis = originWis - 12
            cha = originCha - 8
            int = originInt - 11

        # 幻術師
        if pc.isIllusionist():
            str = originStr - 11
            dex = originDex - 10
            con = originCon - 12
            wis = originWis - 12
            cha = originCha - 8
            int = originInt - 12

        self.writeC(121)
        self.writeC(0x04)
        self.writeC(int * 16 + str)
        self.writeC(dex * 16 + wis)
        self.writeC(cha * 16 + con)
        self.writeC(0x00)

    def getContent(self):
        return self.getBytes()