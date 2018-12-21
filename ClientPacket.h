//
// Created by 范炜东 on 2018/11/16.
//

#ifndef LINEAGE_CLIENTPACKET_H
#define LINEAGE_CLIENTPACKET_H

#include <vector>

namespace Lineage {

class ClientPacket {
public:
    ClientPacket(std::vector<char> &data);

    // 获取操作码
    unsigned char getOpcode();

    // 读取字节流
    std::vector<char> readBytes();

    // 读取1个字节
    unsigned int readC();

    // 读取3个字节
    unsigned int readCH();

    // 读取4个字节
    unsigned int readD();

    // 读取8个字节
    double readF();

    // 读取2个字节
    unsigned int readH();

    // 读取字符串
    std::string readS();

protected:
    size_t offset_; // 已读取位置偏移
    unsigned char opcode_; // 操作码
    std::vector<char> data_;
};

}

#endif //LINEAGE_CLIENTPACKET_H
