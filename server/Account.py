# -*- coding: utf-8 -*-

import base64,hashlib,logging
from datetime import datetime
from Datatables import Session,accounts,characters

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
        '''
        对原始密码进行加密,先使用SHA加密然后使用Base64加密
        :param rawPassword:客户登入输入的原始密码(str)
        :return:加密后的密码
        '''
        return base64.b64encode(hashlib.sha1(rawPassword.encode('utf8')).digest())

    @classmethod
    def create(cls, name, rawPassword, ip, host):
        '''
        创建新账户
        :param name:用户名(str)
        :param rawPassword:密码(str)
        :param ip:登入IP(str)
        :param host:登入HOST(str)
        :return:新账户(Account/None)
        '''
        try:
            account = Account()
            account._name = name
            account._password = Account.encodePassword(rawPassword)
            account._ip = ip
            account._host = host
            account._banned = False
            account._lastActive = datetime.now()

            item = accounts(login=account._name,
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
        '''
        从数据库加载对应账户信息到内存中
        :param name:用户名(str)
        :return:账户信息(Account/None)
        '''
        account = None
        try:
            with Session() as session:
                item = session.query(accounts).filter(accounts.login == name).one_or_none()
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
        '''
        更新账户的登入信息
        :param account:登入账户信息(Account)
        :param ip:登入IP(str)
        :return:None
        '''
        try:
            with Session() as session:
                session.query(accounts).filter(accounts.login == account._name).update({accounts.lastactive : datetime.now(), accounts.ip : ip})

            logging.info("update lastactive for %s", account._name)
        except Exception as e:
            logging.error(e)

    @classmethod
    def updateCharacterSlot(cls, account):
        '''
        更新账户的角色槽即可创建的最大角色数目
        :param account:登入账户信息(Account)
        :return:None
        '''
        try:
            with Session() as session:
                session.query(accounts).filter(accounts.login == account._name).update({accounts.character_slot : account._characterSlot})

            logging.info("update characterslot for %s", account._name)
        except Exception as e:
            logging.error(e)

    def countCharacters(self):
        '''
        返回账户所拥有的角色数目
        :return:角色数目(int)
        '''
        ret = 0
        try:
            with Session() as session:
                    ret = session.query(characters).filter(characters.account_name == self._name).count()
        except Exception as e:
            logging.error(e)

        return ret

    @classmethod
    def ban(cls, name):
        '''
        禁用账户
        :param name:被禁用的用户名(str)
        :return:None
        '''
        try:
            with Session() as session:
                session.query(accounts).filter(accounts.login == name).one_or_none().update({accounts.banned : 1})
        except Exception as e:
            logging.error(e)

    def validatePassword(self, rawPassword):
        '''
        验证登入密码是否正确
        :param rawPassword:用户登入密码(str)
        :return:True/False
        '''
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
        '''
        当前账户是否为游戏管理员
        :return:True/False
        '''
        return self._accessLevel > 0