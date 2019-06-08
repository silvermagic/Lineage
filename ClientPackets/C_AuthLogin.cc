//
// Created by 范炜东 on 2019/5/6.
//

#include <algorithm>
#include "Account.h"
#include "Config.h"
#include "Logger.h"
#include "Player.h"
#include "ServerPackets/S_LoginResult.h"
#include "ServerPackets/S_CommonNews.h"
#include "Tables/Account.h"
#include "C_AuthLogin.h"

C_AuthLogin::C_AuthLogin(std::vector<char> &data) : ClientPacket(data) {}

void C_AuthLogin::handle(std::shared_ptr<Player> player) {
  // 加载/创建账户
  std::string name = readS();
  std::transform(name.begin(), name.end(), name.begin(), ::tolower);
  std::string password = Account::encrypt(readS());
  auto account = std::make_shared<Account>(name, password, player);

  // 登入校验
  if (!account->load() || !account->validate(password)) {
    LOG_INFO << "C_AuthLogin::handle " << name << " ["<< player->address() << "] invalid";
    S_LoginResult pkt(S_LoginResult::Prompt::USER_OR_PASS_WRONG);
    player->write(pkt);
    return;
  }

  // 禁用账户检测
  if (account->banned) {
    LOG_INFO << "C_AuthLogin::handle " << name << " ["<< player->address() << "] disable";
    S_LoginResult pkt(S_LoginResult::Prompt::USER_OR_PASS_WRONG);
    player->write(pkt);
    return;
  }

  // 设置登入账户
  if (player->account() != nullptr) {
    LOG_INFO << "C_AuthLogin::handle " << name << " ["<< player->address() << "] conflict";
    player->account(nullptr);
    S_LoginResult pkt(S_LoginResult::Prompt::ACCOUNT_IN_USE);
    player->write(pkt);
    return;
  }
  player->account(account);

  // 更新登入信息
  db::oper::Account::update(player->account());
  {
    S_LoginResult pkt(S_LoginResult::Prompt::LOGIN_OK);
    player->write(pkt);
  }
  {
    S_CommonNews pkt;
    player->write(pkt);
  }
}