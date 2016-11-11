# -*- coding: utf-8 -*-

import ConfigParser,logging

Config = ConfigParser.SafeConfigParser()

def init():
    Config.read(["config/server.conf", "config/configrates.conf", "config/pack.conf", "config/fights.conf", "config/charsettings.conf", "config/altsettings.conf", "config/additional.conf"])
    Codes = ('UTF8', 'EUCKR', 'UTF8','BIG5', 'SJIS', 'GBK')
    index = Config.getint('server', 'ClientLanguage')
    if 0 <= index and index < 5:
        Config.set('server', 'ClientLanguageCode', Codes[index])
    else:
        Config.set('server', 'ClientLanguageCode', 'GBK')
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)