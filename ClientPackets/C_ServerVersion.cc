//
// Created by 范炜东 on 2019/4/29.
//

#include "Account.h"
#include "Logger.h"
#include "Player.h"
#include "ServerPackets/S_ServerVersion.h"
#include "C_ServerVersion.h"

C_ServerVersion::C_ServerVersion(std::vector<char> &data) : ClientPacket(data) {}

void C_ServerVersion::handle(std::shared_ptr<Player> player) {
  S_ServerVersion pkt;
  player->write(pkt);
}