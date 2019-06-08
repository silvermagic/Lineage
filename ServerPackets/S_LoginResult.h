//
// Created by 范炜东 on 2019/5/9.
//

#ifndef PROJECT_S_LOGINRESULT_H
#define PROJECT_S_LOGINRESULT_H

#include "ServerPacket.h"

class S_LoginResult : public ServerPacket {
public:
  enum class Prompt {
    LOGIN_OK = 0x00,
    USER_OR_PASS_WRONG = 0x08,
    ACCOUNT_IN_USE = 0x16
  };
public:
  S_LoginResult(Prompt);
};

#endif //PROJECT_S_LOGINRESULT_H
