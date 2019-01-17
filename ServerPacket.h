//
// Created by 范炜东 on 2018/11/15.
//

#ifndef LINEAGE_SERVERPACKET_H
#define LINEAGE_SERVERPACKET_H

#include <vector>

namespace Lineage {

class ServerPacket {
public:
    ServerPacket();

    // 带预留大小的数据包，可避免频发的内存重分配
    ServerPacket(unsigned int size);

    // 获取字节流
    char * getBytes();
    const char * getBytes() const;

    // 获取包长度
    unsigned int getLength();

    // 写入字节流
    void writeBytes(const char *, int);

    // 写入一个字节
    void writeC(unsigned int);

    // 写入一个双字
    void writeD(unsigned int);

    // 写入一个浮点数
    void writeF(double);

    // 写入一个字
    void writeH(unsigned int);

    // 写入字符串
    void writeS(const char *);

protected:
    std::vector<char> data_;
};

}

#endif //LINEAGE_SERVERPACKET_H
