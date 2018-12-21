//
// Created by 范炜东 on 2019/1/16.
//

#include "ServerPackets/S_ServerVersion.h"
#include "C_ServerVersion.h"

namespace Lineage {

C_ServerVersion::C_ServerVersion(std::vector<char> &data) : ClientPacket(data) {
}

bool C_ServerVersion::handle(ClientThread &client) {
    client.sendBytes(S_ServerVersion());
    return true;
}

}