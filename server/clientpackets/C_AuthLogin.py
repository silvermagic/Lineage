# -*- coding: utf-8 -*-

import logging
from Config import Config
from ..Account import Account
from ..LoginController import LoginController
from ..serverpackets.S_LoginResult import S_LoginResult
from ..serverpackets.S_CommonNews import S_CommonNews
from ClientBasePacket import ClientBasePacket

class C_AuthLogin(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)
        accountName = self.readS().lower()
        password = self.readS()

        ip = client._ip
        host = client._hostname

        logging.debug("Request AuthLogin from user : %s", accountName)

        if not Config.getboolean('server', 'Allow2PC'):
            for item in LoginController()._accounts:
                if item._ip == ip:
                    logging.info("Refused to 2PC log in.Account %s Ip %s", accountName, ip)
                    client.sendPacket(S_LoginResult(S_LoginResult.REASON_USER_OR_PASS_WRONG))
                    return

        account = Account.load(accountName)
        if not account:
            if Config.getboolean('server', 'AutoCreateAccounts'):
                account = Account.create(accountName, password, ip, host)
            else:
                logging.warning("account missing for user %s", accountName)

        if not account or not account.validatePassword(password):
            client.sendPacket(S_LoginResult(S_LoginResult.REASON_USER_OR_PASS_WRONG))
            return

        if account._banned:
            logging.info("Refused to log in.Account %s Ip %s", accountName, ip)
            client.sendPacket(S_LoginResult(S_LoginResult.REASON_USER_OR_PASS_WRONG))
            return

        try:
            LoginController().login(client, account)
            Account.updateLastActive(account, ip)
            client._account = account
            client.sendPacket(S_LoginResult(S_LoginResult.REASON_LOGIN_OK))
            client.sendPacket(S_CommonNews())
        except Exception as e:
            logging.error(e)
            client.kick()
            logging.error(e)

        return
