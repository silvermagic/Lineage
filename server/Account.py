# -*- coding: utf-8 -*-

import base64,hashlib,logging
from datetime import datetime
from Datatables import Session,Accounts,Characters

class Account:
    def __init__(self):
        self._name = None
        self._ip = None
        self._password = None
        self._lastActive = None
        self._accessLevel = 0
        self._host = None
        self._banned = None
        self._characterSlot = 0
        self._isValid = False

    @classmethod
    def encodePassword(cls, rawPassword):
        return base64.b64encode(hashlib.sha1(rawPassword.encode('utf8')).digest())

    @classmethod
    def create(cls, name, rawPassword, ip, host):
        try:
            account = Account()
            account._name = name
            account._password = Account.encodePassword(rawPassword)
            account._ip = ip
            account._host = host
            account._banned = False
            account._lastActive = datetime.now()

            item = Accounts(login=account._name,
                            password=account._password,
                            lastactive=account._lastActive,
                            access_level=account._accessLevel,
                            ip=account._ip,
                            host=account._host,
                            banned=account._banned,
                            character_slot=account._characterSlot)
            with Session() as session:
                session.add(item)

            logging.info("产生新账号: %s", account._name)
            return account
        except Exception as e:
            logging.error(e)

        return None

    @classmethod
    def load(cls, name):
        account = None
        try:
            with Session() as session:
                item = session.query(Accounts).filter(Accounts.login == name).one_or_none()
                if not item:
                    return account
                account = Account()
                account._name = item.login
                account._password = item.password
                account._lastActive = item.lastactive
                account._accessLevel = item.access_level
                account._ip = item.ip
                account._host = item.host
                account._banned = item.banned
                account._characterSlot = item.character_slot

            logging.info("account exists")
        except Exception as e:
            logging.error(e)

        return account


    @classmethod
    def updateLastActive(cls, account, ip):
        try:
            with Session() as session:
                session.query(Accounts).filter(Accounts.login == account._name).update({Accounts.lastactive : datetime.now(), Accounts.ip : ip})

            logging.info("update lastactive for %s", account._name)
        except Exception as e:
            logging.error(e)

    @classmethod
    def updateCharacterSlot(cls, account):
        try:
            with Session() as session:
                session.query(Accounts).filter(Accounts.login == account._name).update({Accounts.character_slot : account._characterSlot})

            logging.info("update characterslot for %s", account._name)
        except Exception as e:
            logging.error(e)

    def countCharacters(self):
        ret = 0
        try:
            with Session() as session:
                    ret = session.query(Characters).filter(Characters.account_name == self._name).count()
        except Exception as e:
            logging.error(e)

        return ret

    @classmethod
    def ban(cls, name):
        try:
            with Session() as session:
                session.query(Accounts).filter(Accounts.login == name).one_or_none().update({Accounts.banned : 1})
        except Exception as e:
            logging.error(e)

    def validatePassword(self, rawPassword):
        if self._isValid:
            return False

        try:
            self._isValid = self._password == Account.encodePassword(rawPassword)
            if self._isValid:
                self._password = None
            return self._isValid
        except Exception as e:
            logging.error(e)

        return False

    def isGameMaster(self):
        return self._accessLevel > 0