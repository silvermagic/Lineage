# -*- coding: utf-8 -*-

from server.codes import Opcodes
from ServerBasePacket import ServerBasePacket

STATUS_POISON = 1
STATUS_INVISIBLE = 2
STATUS_PC = 4
STATUS_FREEZE = 8
STATUS_BRAVE = 16
STATUS_ELFBRAVE = 32
STATUS_FASTMOVABLE = 64
STATUS_GHOST = 128

class S_OwnCharPack(ServerBasePacket):
    def __init__(self, pc):
        ServerBasePacket.__init__(self)
        status = STATUS_PC

        # todo: 可见

        # todo: 二段加速

        # todo: 魔法状态

        if pc._ghost:
            status |= STATUS_GHOST

        self.writeC(Opcodes.S_OPCODE_CHARPACK)
        self.writeH(pc._loc._x)
        self.writeH(pc._loc._y)
        self.writeD(pc._id)
        if pc._isDead:
            self.writeH(pc._tempCharGfxAtDead)
        else:
            self.writeH(pc._tempCharGfx)

        if pc._isDead:
            self.writeC(pc._status)
        else:
            self.writeC(pc._weaponType)

        self.writeC(pc._heading)
        self.writeC(pc._moveSpeed)
        self.writeD(pc._exp)
        self.writeH(pc._lawful)
        self.writeS(pc._name)
        self.writeS(pc._title)
        self.writeC(status)
        self.writeD(pc._clanid)
        self.writeS(pc._clanname)
        self.writeS('')
        self.writeC(0)
        # todo: 队伍系统
        if not pc._party:
            self.writeC(0xFF)
        else:
            pass
        self.writeC(0)
        self.writeC(0)
        self.writeC(0)
        self.writeC(0xFF)
        self.writeC(0xFF)

