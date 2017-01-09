# -*- coding: utf-8 -*-

# 起始字节号    字节十六进制格式                                      字节ASCII格式
# 0000:        36 33 00 a8 03 00 00 00 d4 b0 01 00                63..........

class ByteArrayUtil():
    @classmethod
    def dumpToString(cls, byteArray):
        j = 0
        str = ''
        for k in range(len(byteArray)):
            # 打印起始字节号
            if j % 16 == 0:
                str += '{:0>4x}'.format(k) + ': '
            # 十六进制打印bytes数据
            str += '{:0>2x}'.format(byteArray[k] & 0xFF) + ' '
            j += 1
            if j != 16:
                continue

            # ascii打印bytes数据
            str += '   '
            i = k - 15
            for l in range(16):
                byte0 = byteArray[i]
                i += 1
                if byte0 > 31 and byte0 < 128:
                    str += chr(byte0)
                else:
                    str += '.'
            str += '\n'
            j = 0

        # 如果最后一次不足16需要单独处理
        l = len(byteArray) % 16
        if l > 0:
            # 用空格代替十六进制填充不足的bytes数据
            for j in range(17 - l):
                str += '    '
            # ascii打印剩余字节
            k = len(byteArray) - l
            for i in range(l):
                byte0 = byteArray[k]
                k += 1
                if byte0 > 31 and byte0 < 128:
                    str += chr(byte0)
                else:
                    str += '.'
            str += '\n'

        return str



