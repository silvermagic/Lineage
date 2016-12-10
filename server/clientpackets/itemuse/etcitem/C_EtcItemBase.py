# -*- coding: utf-8 -*-

from server.serverpackets.S_ServerMessage import S_ServerMessage

class C_EtcItemBase():
    item_ids = []  # 需要处理的道具模板标识集合
    def __init__(self, fd, item_inst):
        '''
        处理材料道具的使用
        :param fd:数据包操作句柄(ClientBasePacket)
        :param item_inst:使用的道具(ItemInstance)
        '''
        self._fd = fd
        self._client = fd._client
        self._pc = fd._client._activeChar
        self._item_inst = item_inst

    def handle(self):
        return self._handle(self._fd, self._item_inst)

    def _handle(self, fd, item_inst):
        '''
        处理道具的使用
        :param item_inst:使用的道具(ItemInstance)
        :return:None
        '''
        raise NotImplementedError

    def Banned(self):
        '''
        使用道具失败
        :return:False
        '''
        self._pc.sendPackets(S_ServerMessage(79))
        return False