# -*- coding: utf-8 -*-

import time,thread,threading
from serverpackets import S_ServerMessage
from utils.Singleton import Singleton

class LoginController():
    __metaclass__ = Singleton
    def __init__(self):
        self._lock = threading.Lock()
        self._accounts = {}
        self._maxAllowedOnlinePlayers = None

    def getAllAccounts(self):
        return self._accounts.viewvalues()

    def getOnlinePlayerCount(self):
        return len(self._accounts)

    def getMaxAllowedOnlinePlayers(self):
        return self._maxAllowedOnlinePlayers

    def setMaxAllowedOnlinePlayers(self, maxAllowedOnlinePlayers):
        self._maxAllowedOnlinePlayers = maxAllowedOnlinePlayers

    def kickClient(self, client):
        if not client:
            return
        def kick():
            if client._activeChar:
                client._activeChar.sendPackets(S_ServerMessage(357))
            time.sleep(1000)
            client.kick()
        thread.start_new_thread(kick)

    def login(self, client, account):
        with self._lock:
            if not account._isValid:
                raise Exception("Illegal Account")

            if self.getMaxAllowedOnlinePlayers() <= self.getOnlinePlayerCount() and not account.isGameMaster():
                raise Exception("Game Server Full")

            if self._accounts.has_key(account._name):
                self.kickClient(self._accounts.pop(account._name))
                raise Exception("Account Already Login")

            self._accounts[account._name] = client

    def logout(self, client):
        with self._lock:
            if not client._account._name:
                return False

            if not self._accounts.pop(client._account._name):
                return False

            return True