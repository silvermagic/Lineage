# -*- coding: utf-8 -*-

import logging,SocketServer
from Config import Config
from ClientThread import ClientThread
from LoginController import LoginController
from server.datatables.MapsTable import MapsTable
from server.model.map.WorldMap import WorldMap


class ClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        t = ClientThread(self.request)
        t.start()
        t.join()

class GameServer():
    def __init__(self):
        MapsTable()
        WorldMap()

    def start(self):
        logging.info("Wait for players to connect in ...")
        LoginController()._maxAllowedOnlinePlayers = Config.getint('server', 'MaximumOnlineUsers')
        self.server = SocketServer.TCPServer((Config.get('server', 'GameserverHostname'), Config.getint('server', 'GameserverPort')), ClientHandler)
        self.server.serve_forever()

    def shutdown(self):
        pass