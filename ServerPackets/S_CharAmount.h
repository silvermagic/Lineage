//
// Created by 范炜东 on 2019/5/9.
//

#ifndef PROJECT_S_CHARAMOUNT_H
#define PROJECT_S_CHARAMOUNT_H

#include "ServerPacket.h"

class S_CharAmount : public ServerPacket {
public:
  S_CharAmount(int count, int slot);
};

#endif //PROJECT_S_CHARAMOUNT_H
