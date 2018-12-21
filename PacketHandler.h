//
// Created by 范炜东 on 2019/1/14.
//

#ifndef LINEAGE_PACKETHANDLER_H
#define LINEAGE_PACKETHANDLER_H

#include <vector>
#include <queue>
#include <Poco/Mutex.h>
#include <Poco/Util/TimerTask.h>
#include "ClientThread.h"

namespace Lineage {

using Poco::FastMutex;
using Poco::Util::TimerTask;

class PacketHandler : public TimerTask {
public:
    PacketHandler(ClientThread &client);

    // 添加待处理数据到缓冲队列
    void append(std::vector<char> &data);

    // 数据包处理
    void run() override;

protected:
    FastMutex mutex_;
    std::queue<std::vector<char>> buffer_;
    ClientThread &client_;
};

}

#endif //LINEAGE_PACKETHANDLER_H
