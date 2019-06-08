//
// Created by 范炜东 on 2019/5/20.
//

#include "Config.h"
#include "Opcodes.h"
#include "Templates/Character.h"
#include "S_CharPacks.h"

S_CharPacks::S_CharPacks(std::shared_ptr<db::def::Character> role) : ServerPacket() {
  writeC(Opcodes::S_OPCODE_CHARLIST);
  writeS(role->character_name.c_str());
  writeS(role->clan_name.c_str());
  writeC(role->career);
  writeC(int(role->sex));
  writeH(role->justice());
  writeH(role->cur_hp());
  writeH(role->cur_mp());
  if (Config::CHARACTER_CONFIG_IN_SERVER_SIDE) {
    writeC(role->level);
  } else {
    writeC(1);
  }
  writeC(role->ac());
  writeC(role->str());
  writeC(role->dex());
  writeC(role->con());
  writeC(role->men());
  writeC(role->cha());
  writeC(role->wis());
  writeC(role->access_level());
  writeD(std::mktime(&role->birthday));
}