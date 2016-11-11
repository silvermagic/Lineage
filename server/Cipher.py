# -*- coding: utf-8 -*-

import struct

# Rotate left: 0b1001 --> 0b0011
rotateLeft = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# Rotate right: 0b1001 --> 0b1100
rotateRight = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

# 将乱数数值混淆用的混淆密码
_C1 = 0x9c30d539L
# 初始的解码数值
_C2 = 0x930fd7e2L
# 将乱数数值混淆用的混淆密码
_C3 = 0x7c72e993L
# 将封包数值混淆用的混淆密码
_C4 = 0x287effc3L

class Cipher:

    def __init__(self, key):
        loInt64,hiInt64 = key ^ _C1,_C2
        loInt64 = rotateRight(loInt64, 13, 32)
        hiInt64 ^= loInt64 ^ _C3
        self._db = [loInt64, hiInt64]
        self._eb = [loInt64, hiInt64]

    def _encrypt(self, buf):
        ek = bytearray(struct.pack('<LL', *self._eb))

        buf[0] ^= ek[0]
        for i in range(1, len(buf)):
            buf[i] ^= buf[i - 1] ^ ek[i & 7]
        buf[3] = buf[3] ^ ek[2]
        buf[2] = buf[2] ^ buf[3] ^ ek[3]
        buf[1] = buf[1] ^ buf[2] ^ ek[4]
        buf[0] = buf[0] ^ buf[1] ^ ek[5]

        return buf

    def _decrypt(self, buf):
        dk = bytearray(struct.pack('<LL', *self._db))

        k = buf[0] ^ buf[1] ^ dk[5]
        buf[0] ^= buf[1] ^ dk[5] ^ dk[0]
        buf[1] ^= buf[2] ^ dk[4]
        buf[2] ^= buf[3] ^ dk[3]
        buf[3] ^= dk[2]
        for i in range(1, len(buf)):
            t = buf[i]
            buf[i] ^= dk[i & 7] ^ k
            k = t

        return buf

    def encrypt(self, buf):
        mask, = struct.unpack('<L', buf[0:4])
        self._encrypt(buf)
        self._eb[0] ^= mask
        self._eb[1] = (self._eb[1] + 0x287EFFC3L) & 0xFFFFFFFFL

        return buf

    def decrypt(self, buf):
        self._decrypt(buf)
        mask, = struct.unpack('<L', buf[0:4])
        self._db[0] ^= mask
        self._db[1] = (self._db[1] + 0x287EFFC3L) & 0xFFFFFFFFL

        return buf



