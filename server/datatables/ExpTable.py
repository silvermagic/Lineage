# -*- coding: utf-8 -*-

from Config import Config

class ExpTable():
    MAX_LEVEL = 99
    MAX_EXP = 0x6ecf16da

    _expTable = (0, 125, 300, 500, 750, 1296, 2401,
                 4096, 6581, 10000, 14661, 20756, 28581, 38436, 50645, 0x10014,
                 0x14655, 0x19a24, 0x1fd25, 0x27114, 0x2f7c5, 0x39324, 0x44535,
                 0x51010, 0x5f5f1, 0x6f920, 0x81c01, 0x96110, 0xacae1, 0xc5c20,
                 0xe1791, 0x100010, 0x121891, 0x146420, 0x16e5e1, 0x19a110,
                 0x1c9901, 0x1fd120, 0x234cf1, 0x271010, 0x2b1e31, 0x2f7b21,
                 0x342ac2, 0x393111, 0x3e9222, 0x49b332, 0x60b772, 0x960cd1,
                 0x12d4c4e, 0x3539b92, 0x579ead6, 0x7a03a1a, 0x9c6895e, 0xbecd8a2,
                 0xe1327e6, 0x1039772a, 0x125fc66e, 0x148615b2, 0x16ac64f6,
                 0x18d2b43a, 0x1af9037e, 0x1d1f52c2, 0x1f45a206, 0x216bf14a,
                 0x2392408e, 0x25b88fd2, 0x27dedf16, 0x2a052e5a, 0x2c2b7d9e,
                 0x2e51cce2, 0x30781c26, 0x329e6b6a, 0x34c4baae, 0x36eb09f2,
                 0x39115936, 0x3b37a87a, 0x3d5df7be, 0x3f844702, 0x41aa9646,
                 0x43d0e58a, 0x45f734ce, 0x481d8412, 0x4a43d356, 0x4c6a229a,
                 0x4e9071de, 0x50b6c122, 0x52dd1066, 0x55035faa, 0x5729aeee,
                 0x594ffe32, 0x5b764d76, 0x5d9c9cba, 0x5fc2ebfe, 0x61e93b42,
                 0x640f8a86, 0x6635d9ca, 0x685c290e, 0x6a827852, 0x6ca8c796,
                 0x6ecf16da)

    _expPenalty = (
        Config.getint('charsettings', 'Lv50Exp'), Config.getint('charsettings', 'Lv51Exp'),
        Config.getint('charsettings', 'Lv52Exp'), Config.getint('charsettings', 'Lv53Exp'),
        Config.getint('charsettings', 'Lv54Exp'), Config.getint('charsettings', 'Lv55Exp'),
        Config.getint('charsettings', 'Lv56Exp'), Config.getint('charsettings', 'Lv57Exp'),
        Config.getint('charsettings', 'Lv58Exp'), Config.getint('charsettings', 'Lv59Exp'),
        Config.getint('charsettings', 'Lv60Exp'), Config.getint('charsettings', 'Lv61Exp'),
        Config.getint('charsettings', 'Lv62Exp'), Config.getint('charsettings', 'Lv63Exp'),
        Config.getint('charsettings', 'Lv64Exp'), Config.getint('charsettings', 'Lv65Exp'),
        Config.getint('charsettings', 'Lv66Exp'), Config.getint('charsettings', 'Lv67Exp'),
        Config.getint('charsettings', 'Lv68Exp'), Config.getint('charsettings', 'Lv69Exp'),
        Config.getint('charsettings', 'Lv70Exp'), Config.getint('charsettings', 'Lv71Exp'),
        Config.getint('charsettings', 'Lv72Exp'), Config.getint('charsettings', 'Lv73Exp'),
        Config.getint('charsettings', 'Lv74Exp'), Config.getint('charsettings', 'Lv75Exp'),
        Config.getint('charsettings', 'Lv76Exp'), Config.getint('charsettings', 'Lv77Exp'),
        Config.getint('charsettings', 'Lv78Exp'), Config.getint('charsettings', 'Lv79Exp'),
        Config.getint('charsettings', 'Lv80Exp'), Config.getint('charsettings', 'Lv81Exp'),
        Config.getint('charsettings', 'Lv82Exp'), Config.getint('charsettings', 'Lv83Exp'),
        Config.getint('charsettings', 'Lv84Exp'), Config.getint('charsettings', 'Lv85Exp'),
        Config.getint('charsettings', 'Lv86Exp'), Config.getint('charsettings', 'Lv87Exp'),
        Config.getint('charsettings', 'Lv88Exp'), Config.getint('charsettings', 'Lv89Exp'),
        Config.getint('charsettings', 'Lv90Exp'), Config.getint('charsettings', 'Lv91Exp'),
        Config.getint('charsettings', 'Lv92Exp'), Config.getint('charsettings', 'Lv93Exp'),
        Config.getint('charsettings', 'Lv94Exp'), Config.getint('charsettings', 'Lv95Exp'),
        Config.getint('charsettings', 'Lv96Exp'), Config.getint('charsettings', 'Lv97Exp'),
        Config.getint('charsettings', 'Lv98Exp'), Config.getint('charsettings', 'Lv99Exp'))

    @classmethod
    def getExpByLevel(cls, level):
        return cls._expTable[level - 1]

    @classmethod
    def getNeedExpNextLevel(cls, level):
        return cls.getExpByLevel(level + 1) - cls.getExpByLevel(level)

    @classmethod
    def getLevelByExp(cls, exp):
        level = 0
        for level in range(len(cls._expTable)):
            if exp < cls._expTable[level]:
                break
        return min(level, cls.MAX_LEVEL)

    @classmethod
    def getExpPercentage(cls, level, exp):
        return int(100 * (float(exp - cls.getExpByLevel(level)) / float(cls.getNeedExpNextLevel(level))))

    @classmethod
    def getPenaltyRate(cls, level):
        if level < 50:
            return float(1.0)

        expPenalty = float(1.0) / cls._expPenalty[level - 50]
        return expPenalty

