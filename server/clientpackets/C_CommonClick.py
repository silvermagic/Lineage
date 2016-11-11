# -*- coding: utf-8 -*-

import logging
from Config import Config
from Datatables import Session,Characters
from ..serverpackets.S_CharAmount import S_CharAmount
from ..serverpackets.S_CharPacks import S_CharPacks
from ClientBasePacket import ClientBasePacket

class C_CommonClick(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)
        self.deleteCharacter(client)
        amountOfChars = client._account.countCharacters()
        client.sendPacket(S_CharAmount(amountOfChars, client))
        if amountOfChars > 0:
            self.sendCharPacks(client)
            client._loginStatus = 1

    def deleteCharacter(self, client):
        pass

    def sendCharPacks(self, client):
        try:
            with Session() as session:
                items = session.query(Characters).filter(Characters.account_name == client._account._name).order_by(Characters.objid).all()
                for item in items:
                    name = item.char_name
                    clanname = item.Clanname
                    type = item.Type
                    sex = item.Sex
                    lawful = item.Lawful

                    currenthp = item.CurHp
                    if currenthp < 1:
                        currenthp = 1
                    elif currenthp > 32767:
                        currenthp = 32767

                    currentmp = item.CurMp
                    if currentmp < 1:
                        currentmp = 1
                    elif currentmp > 32767:
                        currentmp = 32767

                    lvl = 1
                    if Config.getboolean('altsettings', 'CharacterConfigInServerSide'):
                        lvl = item.level
                        if lvl < 1:
                            lvl = 1
                        elif lvl > 127:
                            lvl = 127

                        ac = item.Ac
                        str = item.Str
                        dex = item.Dex
                        con = item.Con
                        wis = item.Wis
                        cha = item.Cha
                        intel = item.Intel
                        accessLevel = item.AccessLevel
                        birthday = item.birthday
                        client.sendPacket(S_CharPacks(name, clanname, type, sex, lawful, currenthp, currentmp, ac, lvl, str, dex, con, wis, cha, intel, accessLevel, birthday.date().timestamp()))
        except Exception as e:
            logging.error(e)