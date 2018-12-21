//
// Created by 范炜东 on 2019/1/17.
//

#include "Opcodes.h"
#include "S_CommonNews.h"

namespace Lineage {

S_CommonNews::S_CommonNews() : ServerPacket()
{
    writeC(S_OPCODE_COMMONNEWS);
    // TODO: 读取公告文件
    writeS("");
}

}