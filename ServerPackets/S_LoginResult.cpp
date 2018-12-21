//
// Created by 范炜东 on 2019/1/17.
//

#include "Opcodes.h"
#include "S_LoginResult.h"

namespace Lineage {

S_LoginResult::S_LoginResult(unsigned int reason) : ServerPacket() {
    writeC(S_OPCODE_LOGINRESULT);
    writeC(reason);
    writeD(0x00000000);
    writeD(0x00000000);
    writeD(0x00000000);
}

}
