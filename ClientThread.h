//
// Created by 范炜东 on 2018/11/19.
//

#ifndef LINEAGE_CLIENTTHREAD_H
#define LINEAGE_CLIENTTHREAD_H

#include <Poco/Mutex.h>
#include <Poco/Util/Timer.h>
#include <Poco/Net/TCPServerConnection.h>
#include <Poco/Net/TCPServerConnectionFactory.h>
#include <Poco/Net/ServerSocket.h>
#include "ServerPacket.h"

namespace Lineage {

using Poco::FastMutex;
using Poco::Util::Timer;
using Poco::Net::StreamSocket;
using Poco::Net::TCPServerConnection;
using Poco::Net::TCPServerConnectionFactory;

enum LoginStatus {
    LOGIN, // 用户名密码验证
    SELECT, // 角色选取
    CONFIRM // 确认角色并进入游戏世界
};

class Connect : public TCPServerConnection {
public:
    Connect(const StreamSocket &s);

    // 返回数据包到客户端
    void sendBytes(ServerPacket &&pkt);

protected:
    // 加密
    void encrypt(char *pbuf, int size);

    // 解密
    void decrypt(char *pbuf, int size);

    // 字节和无符号整形转换
    unsigned int bytes2uint(char *pbuf);

protected:
    FastMutex mutex_; // 并发写锁
    unsigned int encrypt_[2], decrypt_[2]; // 加密、解密秘钥
};

class ClientThread : public Connect {
public:
    ClientThread(const StreamSocket &s);

    // 获取客户端地址
    std::string getIp();

    // 处理线程
    void run() override;

protected:
    LoginStatus status_; // 客户端状态
};

class ConnectionFactory : public TCPServerConnectionFactory {
public:
    ConnectionFactory() {}

    ClientThread *createConnection(const StreamSocket &socket) override {
        return new ClientThread(socket);
    }
};

}

#endif //LINEAGE_CLIENTTHREAD_H
