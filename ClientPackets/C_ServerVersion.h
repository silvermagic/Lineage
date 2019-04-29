//
// Created by 范炜东 on 2019/4/29.
//

#ifndef PROJECT_C_SERVERVERSION_H
#define PROJECT_C_SERVERVERSION_H

#include "ClientPacket.h"

class C_ServerVersion : public ClientPacket {
public:
  C_ServerVersion(std::vector<char> &data);
  void handle(std::shared_ptr<Player>) override;
};

#endif //PROJECT_C_SERVERVERSION_H
