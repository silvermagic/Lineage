//
// Created by 范炜东 on 2019/5/20.
//

#ifndef PROJECT_S_CHARPACKS_H
#define PROJECT_S_CHARPACKS_H

#include "ServerPacket.h"

namespace db {
namespace def {
class Character;
}
}

class S_CharPacks : public ServerPacket {
public:
  S_CharPacks(std::shared_ptr<db::def::Character> role);
};

#endif //PROJECT_S_CHARPACKS_H
