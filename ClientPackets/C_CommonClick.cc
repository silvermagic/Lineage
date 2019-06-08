//
// Created by 范炜东 on 2019/5/9.
//

#include "Player.h"
#include "Account.h"
#include "ServerPackets/S_CharAmount.h"
#include "ServerPackets/S_CharPacks.h"
#include "Tables/Character.h"
#include "Templates/Character.h"
#include "C_CommonClick.h"

C_CommonClick::C_CommonClick(std::vector<char> &data) : ClientPacket(data) {}

void C_CommonClick::handle(std::shared_ptr<Player> player) {
  std::string account_name = player->account()->name();
  auto character_names = db::oper::Character::delete_expired(account_name);
  for (auto character_name : character_names) {
    // TODO: 血盟处理
  }
  auto roles = db::oper::Character::query_by_account(account_name);
  S_CharAmount pkt(roles.size(), player->account()->character_slot);
  player->write(pkt);
  if (roles.size() > 0) {
    for (auto role : roles) {
      S_CharPacks pkt(role);
      player->write(pkt);
    }
  }
}