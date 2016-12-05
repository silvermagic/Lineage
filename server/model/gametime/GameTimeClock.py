# -*- coding: utf-8 -*-

import logging,time
from threading import Thread
from server.utils.Singleton import Singleton
from GameTime import GameTime

class TimeUpdater(Thread):
    def __init__(self, gc):
        Thread.__init__(self)
        self._gc = gc

    def run(self):
        while (True):
            self._gc._previousTime = self._gc._currentTime
            self._gc._currentTime = GameTime.fromSystemCurrentTime()
            self._gc.notifyChanged()

            try:
                time.sleep(1)
            except Exception as e:
                logging.error(e)

class GameTimeClock():
    __metaclass__ = Singleton
    def __init__(self):
        self._currentTime = GameTime.fromSystemCurrentTime()
        self._previousTime = self._currentTime
        self._listeners = []
        self._t = TimeUpdater(self)
        self._t.start()

    def notifyChanged(self):
        if self._previousTime._datetime.month != self._currentTime._datetime.month:
            for listener in self._listeners:
                listener.onMonthChanged(self._currentTime)

        if self._previousTime._datetime.day != self._currentTime._datetime.day:
            for listener in self._listeners:
                listener.onDayChanged(self._currentTime)

        if self._previousTime._datetime.hour != self._currentTime._datetime.hour:
            for listener in self._listeners:
                listener.onHourChanged(self._currentTime)

        if self._previousTime._datetime.minute != self._currentTime._datetime.minute:
            for listener in self._listeners:
                listener.onMinuteChanged(self._currentTime)

    def addListener(self, listener):
        self._listeners += listener

    def removeListener(self, listener):
        self._listeners.remove(listener)