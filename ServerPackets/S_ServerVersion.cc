//
// Created by 范炜东 on 2019/4/29.
//

#include <chrono>
#include "Config.h"
#include "Opcodes.h"
#include "S_ServerVersion.h"

static int uptime = std::chrono::duration_cast<std::chrono::seconds>(std::chrono::system_clock::now().time_since_epoch()).count();

S_ServerVersion::S_ServerVersion() : ServerPacket() {
  writeC(Opcodes::S_OPCODE_SERVERVERSION);
  writeC(0x00);
  writeC(0x02);
  writeD(0x00a8c732);
  writeD(0x00a8c6a7);
  writeD(0x77cf6eba);
  writeD(0x00a8cdad);
  writeD(uptime);
  writeC(0x00);
  writeC(0x00);
  writeC(Config::CLIENT_LANGUAGE);
  writeD(0x00000000);
  writeC(0xae);
  writeC(0xb2);
}