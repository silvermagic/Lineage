//
// Created by 范炜东 on 2018/12/20.
//

#ifndef LINEAGE_C_AUTHLOGIN_H
#define LINEAGE_C_AUTHLOGIN_H

#include "ClientThread.h"
#include "ClientPacket.h"

namespace Lineage {

class C_AuthLogin : public ClientPacket {
public:
    C_AuthLogin(std::vector<char> &data);

    // 处理
    bool handle(ClientThread &client);
};

}



#endif //LINEAGE_C_AUTHLOGIN_H
