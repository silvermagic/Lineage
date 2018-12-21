//
// Created by 范炜东 on 2019/1/16.
//

#include <Poco/Timestamp.h>
#include <Poco/Util/Application.h>
#include "Opcodes.h"
#include "S_ServerVersion.h"

namespace Lineage {

using Poco::Timestamp;
using Poco::Util::Application;

S_ServerVersion::S_ServerVersion() : ServerPacket() {
    Application &app = Application::instance();

    writeC(S_OPCODE_SERVERVERSION);
    writeC(0x00);
    writeC(0x02);
    writeD(0x00a8c732);
    writeD(0x00a8c6a7);
    writeD(0x77cf6eba);
    writeD(0x00a8cdad);
    Timestamp t;
    writeD(t.epochMicroseconds() / 1000);
    writeC(0x00);
    writeC(0x00);
    writeC(app.config().getInt("Server.language", 5));
    writeD(0x00000000);
    writeC(0xae);
    writeC(0xb2);
}

}
