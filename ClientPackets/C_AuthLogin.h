//
// Created by 范炜东 on 2019/5/6.
//

#ifndef PROJECT_C_AUTHLOGIN_H
#define PROJECT_C_AUTHLOGIN_H

#include "ClientPacket.h"

class C_AuthLogin : public ClientPacket {
public:
  C_AuthLogin(std::vector<char> &data);
  void handle(std::shared_ptr<Player>) override;
};

#endif //PROJECT_C_AUTHLOGIN_H
