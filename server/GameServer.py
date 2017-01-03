# -*- coding: utf-8 -*-

import logging,SocketServer
from Config import Config
from ClientThread import ClientThread
from LoginController import LoginController
from server.datatables.MapsTable import MapsTable
from server.datatables.SkillsTable import SkillsTable
from server.model.map.WorldMap import WorldMap
from server.model.gametime.GameTimeClock import GameTimeClock

class ClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        '''
        处理来自客户端的连接
        :return:None
        '''
        t = ClientThread(self.request)
        t.start()
        t.join()

    def finish(self):
        self.request.close()

class GameServer():
    def __init__(self):
        MapsTable()
        WorldMap()
        GameTimeClock()
        SkillsTable()

    def start(self):
        '''
        等待客户端的连接并启动并为连接创建新的处理线程
        :return:None
        '''
        logging.info("Wait for players to connect in ...")
        LoginController()._maxAllowedOnlinePlayers = Config.getint('server', 'MaximumOnlineUsers')
        self.server = SocketServer.TCPServer((Config.get('server', 'GameserverHostname'), Config.getint('server', 'GameserverPort')), ClientHandler)
        self.server.serve_forever()

    def shutdown(self):
        pass