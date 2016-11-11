# -*- coding: utf-8 -*-

import Config
from server.GameServer import GameServer

def main():
    Config.init()
    srv = GameServer()
    srv.start()

if __name__ == '__main__':
    main()