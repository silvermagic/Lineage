//
// Created by 范炜东 on 2019/1/16.
//

#ifndef LINEAGE_C_SERVERVERSION_H
#define LINEAGE_C_SERVERVERSION_H

#include "ClientThread.h"
#include "ClientPacket.h"

namespace Lineage {

class C_ServerVersion : public ClientPacket {
public:
    C_ServerVersion(std::vector<char> &data);

    // 处理
    bool handle(ClientThread &client);
};

}


#endif //LINEAGE_C_SERVERVERSION_H
