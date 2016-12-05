# -*- coding: utf-8 -*-

import time,thread,threading
from serverpackets.S_ServerMessage import S_ServerMessage
from utils.Singleton import Singleton

class LoginController():
    '''
    登入账户的管理
    '''
    __metaclass__ = Singleton
    def __init__(self):
        self._lock = threading.Lock()
        self._accounts = {}
        self._maxAllowedOnlinePlayers = None

    def getAllAccounts(self):
        return self._accounts.viewvalues()

    def getOnlinePlayerCount(self):
        return len(self._accounts)

    def kickClient(self, client):
        '''
        踢出登入的玩家账户(客户端表现为断线)
        :param client:账户对应的客户端处理线程(ClientThread)
        :return:None
        '''
        if not client:
            return
        def kick():
            if client._activeChar:
                client._activeChar.sendPackets(S_ServerMessage(357))
            time.sleep(1000)
            client.kick()
        thread.start_new_thread(kick, ())

    def login(self, client, account):
        '''
        保存符合条件的登入账户信息
        :param client:账户对应的客户端处理线程(ClientThread)
        :param account:登入账户信息(Account)
        :return:None
        '''
        with self._lock:
            if not account._isValid:
                raise Exception("Illegal Account")

            if self._maxAllowedOnlinePlayers <= self.getOnlinePlayerCount() and not account.isGameMaster():
                raise Exception("Game Server Full")

            if self._accounts.has_key(account._name):
                self.kickClient(self._accounts.pop(account._name))
                raise Exception("Account Already Login")

            self._accounts[account._name] = client

    def logout(self, client):
        '''
        删除保存的登入账户信息
        :param client:账户对应的客户端处理线程(ClientThread)
        :return:删除状态(True/False)
        '''
        with self._lock:
            if not client._account._name:
                return False

            if not self._accounts.pop(client._account._name):
                return False

            return True