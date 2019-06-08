//
// Created by 范炜东 on 2019/5/9.
//

#include "Config.h"
#include "Opcodes.h"
#include "S_CharAmount.h"

S_CharAmount::S_CharAmount(int count, int slot) : ServerPacket() {
  writeC(Opcodes::S_OPCODE_CHARAMOUNT);
  writeC(count);
  writeC(Config::DEFAULT_CHARACTER_SLOT + slot);
}