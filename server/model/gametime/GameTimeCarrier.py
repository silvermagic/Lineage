# -*- coding: utf-8 -*-

from taskthread import TimerTask
from server.serverpackets.S_GameTime import S_GameTime
from GameTimeClock import GameTimeClock

class GameTimeCarrier():
    def __init__(self, pc):
        self._pc = pc
        self._task = TimerTask(self.run, 0.5)

    def run(self):
        try:
            if not self._pc._netConnection:
                self.stop()
                return

            serverTime = GameTimeClock()._currentTime._time
            if serverTime % 300 == 0:
                self._pc.sendPackets(S_GameTime(serverTime))
        except Exception as e:
            pass

    def start(self):
        self._task.start()

    def stop(self):
        self._task.stop()