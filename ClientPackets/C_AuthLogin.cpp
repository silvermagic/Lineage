//
// Created by 范炜东 on 2018/12/20.
//

#include <Poco/Util/Application.h>
#include "ServerPackets/S_LoginResult.h"
#include "ServerPackets/S_CommonNews.h"
#include "Schema/Account.h"
#include "C_AuthLogin.h"

namespace Lineage {

using Poco::Util::Application;

C_AuthLogin::C_AuthLogin(std::vector<char> &data) : ClientPacket(data) {
}

bool C_AuthLogin::handle(ClientThread &client) {
    Application &app = Application::instance();

    std::string name = readS();
    std::string password = readS();

    app.logger().information("验证登入: %s", name);
    // TODO: 禁用双开

    Account account(name);
    if (!account.exist()) {
        if (app.config().getBool("Server.auto_create_account", false)) {
            account.save();
        } else {
            client.sendBytes(S_LoginResult(REASON_USER_OR_PASS_WRONG));
            return false;
        }
    }
    account.load();
    if (!account.validatePassword(password))
    {
        client.sendBytes(S_LoginResult(REASON_USER_OR_PASS_WRONG));
        return false;
    }
    if (account.banned) {
        app.logger().information("禁用玩家登入，登入账号: %s 登入地址: %s", name, client.getIp());
        client.sendBytes(S_LoginResult(REASON_USER_OR_PASS_WRONG));
        return false;
    }

    // 更新账户信息
    account.ip = client.getIp();
    account.updateLastActive();

    // 登入成功
    client.sendBytes(S_LoginResult(REASON_LOGIN_OK));
    client.sendBytes(S_CommonNews());

    return true;
}

}