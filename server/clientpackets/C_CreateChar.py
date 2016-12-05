# -*- coding: utf-8 -*-

import logging
from Config import Config
from server.Account import Account
from server.BadNamesList import BadNamesList
from server.IdFactory import IdFactory
from server.datatables.CharacterTable import CharacterTable
from server.model.Instance.PcInstance import PcInstance
from server.serverpackets.S_CharCreateStatus import S_CharCreateStatus
from server.serverpackets.S_NewCharPacket import S_NewCharPacket
from server.utils.CalcInitHpMp import CalcInitHpMp
from ClientBasePacket import ClientBasePacket

ORIGINAL_STR = (13, 16, 11, 8, 12, 13, 11)
ORIGINAL_DEX = (10, 12, 12, 7, 15, 11, 10)
ORIGINAL_CON = (10, 14, 12, 12, 8, 14, 12)
ORIGINAL_WIS = (11, 9, 12, 12, 10, 12, 12)
ORIGINAL_CHA = (13, 12, 9, 8, 9, 8, 8)
ORIGINAL_INT = (10, 8, 12, 12, 11, 11, 12)
ORIGINAL_AMOUNT = (8, 4, 7, 16, 10, 6, 10)

MALE_LIST = (0, 61, 138, 734, 2786, 6658, 6671)
FEMALE_LIST = (1, 48, 37, 1186, 2796, 6661, 6650)
# XXX 各職業出生地改回台版
LOCX_LIST = (32780, 32714, 33043, 32780, 32925, 32780, 32714)
LOCY_LIST = (32781, 32877, 32336, 32781, 32801, 32781, 32877)
MAPID_LIST = (68, 69, 4, 68, 304, 68, 69)

class C_CreateChar(ClientBasePacket):
    def __init__(self, decrypt, client):
        ClientBasePacket.__init__(self, decrypt)
        name = self.readS()
        account = Account.load(client._account._name)
        maxAmount = Config.getint('altsettings', 'DefaultCharacterSlot') + account._characterSlot

        name = name.replace('\\s', '')
        name = name.replace('', '')
        if len(name) == 0:
            client.sendPacket(S_CharCreateStatus(S_CharCreateStatus.REASON_INVALID_NAME))
            return
        # todo:
        #if self.isInvalidName(name):
        #    client.sendPacket(S_CharCreateStatus(S_CharCreateStatus.REASON_INVALID_NAME))
        #    return

        if CharacterTable().doesCharNameExist(name):
            logging.info('charname: ' + name + ' already exists. creation failed.')
            client.sendPacket(S_CharCreateStatus(S_CharCreateStatus.REASON_ALREADY_EXSISTS))
            return

        if client._account._characterSlot >= maxAmount:
            logging.info('帐号: ' + client._account._name + '建立超过' + maxAmount + '个人物角色.')
            client.sendPacket(S_CharCreateStatus(S_CharCreateStatus.REASON_ALREADY_EXSISTS))
            return

        pc = PcInstance()
        pc._name = name
        pc._type = self.readC()
        pc._sex = self.readC()
        pc.addBaseStr(self.readC())
        pc.addBaseDex(self.readC())
        pc.addBaseCon(self.readC())
        pc.addBaseWis(self.readC())
        pc.addBaseCha(self.readC())
        pc.addBaseInt(self.readC())

        isStatusError = False
        originalStr = ORIGINAL_STR[pc._type]
        originalDex = ORIGINAL_DEX[pc._type]
        originalCon = ORIGINAL_CON[pc._type]
        originalWis = ORIGINAL_WIS[pc._type]
        originalCha = ORIGINAL_CHA[pc._type]
        originalInt = ORIGINAL_INT[pc._type]
        originalAmount = ORIGINAL_AMOUNT[pc._type]

        if ((pc._baseStr < originalStr or pc._baseDex < originalDex
             or pc._baseCon < originalCon
             or pc._baseWis < originalWis
             or pc._baseCha < originalCha
             or pc._baseInt < originalInt)
            or (pc._baseStr > originalStr + originalAmount
                or pc._baseDex > originalDex + originalAmount
                or pc._baseCon > originalCon + originalAmount
                or pc._baseWis > originalWis + originalAmount
                or pc._baseCha > originalCha + originalAmount
                or pc._baseInt > originalInt + originalAmount)):
            isStatusError = True

        statusAmount = pc._str + pc._con + pc._dex + pc._cha + pc._int + pc._wis + pc._sex
        if statusAmount != 75 or isStatusError:
            logging.info('Character have wrong value')
            client.sendPacket(S_CharCreateStatus(S_CharCreateStatus.REASON_WRONG_AMOUNT))
            return

        client.sendPacket(S_CharCreateStatus(S_CharCreateStatus.REASON_OK))
        self.initNewChar(client, pc)

    def initNewChar(self, client, pc):
        pc._id = IdFactory().nextId()
        if pc._sex == 0:
            pc._classId = MALE_LIST[pc._type]
        else:
            pc._classId = FEMALE_LIST[pc._type]

        logging.info('charname: ' + pc._name + ' classId: ' + str(pc._classId))

        pc._loc._x = LOCX_LIST[pc._type]
        pc._loc._y = LOCY_LIST[pc._type]
        pc.setMap(MAPID_LIST[pc._type])
        pc._heading = 0
        pc._lawful = 0
        initHp = CalcInitHpMp.calcInitHp(pc)
        initMp = CalcInitHpMp.calcInitMp(pc)
        pc.addBaseMaxHp(initHp)
        pc.setCurrentHp(initHp)
        pc.addBaseMaxMp(initMp)
        pc.setCurrentMp(initMp)
        pc._accountName = client._account._name
        # todo:
        #   1.角色创建广播
        #   2.pc.isWizard
        #   3.Beginner
        CharacterTable().storeNewCharacter(pc)
        client.sendPacket(S_NewCharPacket(pc))
        CharacterTable().saveCharStatus(pc)
        # todo:
        #   1.pc.refresh()

    @classmethod
    def isInvalidName(cls, name):
        try:
            numOfNameBytes = len(name.encode(Config.get('server', 'ClientLanguageCode')))
        except Exception as e:
            logging.error(e)
            return False

        if 5 < len(name) or 12 < numOfNameBytes:
            return False

        if BadNamesList().isBadName(name):
            return False

        return True


