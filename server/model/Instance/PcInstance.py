# -*- coding: utf-8 -*-

import logging

class PcInstance:
    def __init__(self):
        self._out = None

    def sendPackets(self, serverbasepacket):
        try:
            self._out.sendPacket(serverbasepacket)
        except Exception as e:
            logging.error(e)
