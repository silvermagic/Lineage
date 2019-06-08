//
// Created by 范炜东 on 2019/5/9.
//

#include "Opcodes.h"
#include "S_LoginResult.h"

S_LoginResult::S_LoginResult(Prompt v) : ServerPacket() {
  writeC(Opcodes::S_OPCODE_LOGINRESULT);
  writeC(int(v));
  writeD(0x00000000);
  writeD(0x00000000);
  writeD(0x00000000);
}