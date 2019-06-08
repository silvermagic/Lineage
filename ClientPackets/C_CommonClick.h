//
// Created by 范炜东 on 2019/5/9.
//

#ifndef PROJECT_C_COMMONCLICK_H
#define PROJECT_C_COMMONCLICK_H

#include "ClientPacket.h"

class Player;
class C_CommonClick : public ClientPacket {
public:
  C_CommonClick(std::vector<char> &data);
  void handle(std::shared_ptr<Player>) override;
};

#endif //PROJECT_C_COMMONCLICK_H
