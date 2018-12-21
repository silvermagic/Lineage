//
// Created by 范炜东 on 2019/1/17.
//

#ifndef LINEAGE_S_LOGINRESULT_H
#define LINEAGE_S_LOGINRESULT_H

#include "ServerPacket.h"

namespace Lineage {

const unsigned int REASON_LOGIN_OK = 0x00;
const unsigned int REASON_ACCOUNT_IN_USE = 0x16;
const unsigned int REASON_USER_OR_PASS_WRONG = 0x08;

class S_LoginResult : public ServerPacket {
public:
    S_LoginResult(unsigned int reason);
};

}

#endif //LINEAGE_S_LOGINRESULT_H
