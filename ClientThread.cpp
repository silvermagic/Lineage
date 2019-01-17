//
// Created by 范炜东 on 2018/11/19.
//

#include <atomic>
#include <Poco/AutoPtr.h>
#include <Poco/Util/Application.h>
#include "ServerPacket.h"
#include "PacketHandler.h"
#include "Opcodes.h"
#include "ClientThread.h"

namespace Lineage {

using Poco::AutoPtr;
using Poco::Util::Application;

// 游戏服务器运行标志
extern std::atomic_bool g_Running;

// 将乱数数值混淆用的混淆密码
static const unsigned int C1 = 0x9c30d539L;
// 初始的解码数值
static const unsigned int C2 = 0x930fd7e2L;
// 将乱数数值混淆用的混淆密码
static const unsigned int C3 = 0x7c72e993L;
// 将封包数值混淆用的混淆密码
static const unsigned int C4 = 0x287effc3L;
// 数据包最大长度
static const int MAX_PACKET_SIZE = 1024;
static const unsigned char FIRST_PACKET[] = {0xF4, 0x0a, 0x8d, 0x23, 0x6f, 0x7f, 0x04, 0x00, 0x05, 0x08, 0x00};

Connect::Connect(const StreamSocket &s) :
        TCPServerConnection(s) {
    unsigned int key = 2147483647 ^C1;
    key = key >> 13 | key << 19;
    encrypt_[0] = decrypt_[0] = key;
    encrypt_[1] = decrypt_[1] = C2 ^ key ^ C3;
}

void Connect::sendBytes(ServerPacket &&pkt) {
    FastMutex::ScopedLock lock(mutex_);
    unsigned int len = pkt.getLength();
    if (len <= 0)
        return;

    ServerPacket data(len + 2);
    data.writeH(len + 2);
    data.writeBytes(pkt.getBytes(), len);
    encrypt(data.getBytes(), data.getLength());
    int n = socket().sendBytes(data.getBytes(), data.getLength());
    poco_assert(n == len);
}

void Connect::decrypt(char *pbuf, unsigned int size) {
    char *key = reinterpret_cast<char *>(&decrypt_);
    pbuf[0] ^= key[0];
    for (unsigned int i = 0; i < size; i++) {
        pbuf[i] = pbuf[i - 1] ^ key[i & 7];
    }
    pbuf[3] ^= key[2];
    pbuf[2] ^= pbuf[3] ^ key[3];
    pbuf[1] ^= pbuf[2] ^ key[4];
    pbuf[0] ^= pbuf[1] ^ key[5];
    unsigned int mask = bytes2uint(pbuf);
    decrypt_[0] ^= mask;
    decrypt_[1] = (unsigned int)((decrypt_[1] + C4) & 0xFFFFFFFFL);
}

void Connect::encrypt(char *pbuf, unsigned int size) {
    char *key = reinterpret_cast<char *>(&encrypt_);
    unsigned int mask = bytes2uint(pbuf);
    char k = pbuf[0] ^pbuf[1] ^key[5];
    pbuf[0] ^= k ^ key[0];
    pbuf[1] ^= pbuf[2] ^ key[4];
    pbuf[2] ^= pbuf[3] ^ key[3];
    pbuf[3] ^= key[2];
    for (unsigned int i = 0; i < size; i++) {
        char t = pbuf[i];
        pbuf[i] ^= key[i & 7] ^ k;
        k = t;
    }
    encrypt_[0] ^= mask;
    encrypt_[1] = (unsigned int)((encrypt_[1] + C4) & 0xFFFFFFFFL);
}

unsigned int Connect::bytes2uint(char *pbuf) {
    unsigned int i = (unsigned int)pbuf[0] & 0xFF;
    i |= pbuf[1] << 8 & 0xFF00L;
    i |= pbuf[2] << 16 & 0xFF0000L;
    i |= pbuf[3] << 24 & 0xFF000000L;
    return i;
}

ClientThread::ClientThread(const Poco::Net::StreamSocket &s) :
        Connect(s),
        status_(LOGIN) {

}

std::string ClientThread::getIp()
{
    return socket().peerAddress().toString();
}

void ClientThread::run() {
    Application &app = Application::instance();
    app.logger().information("请求来自: " + socket().peerAddress().toString());
    try {
        // 数据包处理线程
        Timer workers;
        AutoPtr<PacketHandler> work_for_item(new PacketHandler(*this));
        AutoPtr<PacketHandler> work_for_move(new PacketHandler(*this));
        AutoPtr<PacketHandler> work_for_all(new PacketHandler(*this));
        workers.scheduleAtFixedRate(work_for_item, 0, 400);
        workers.scheduleAtFixedRate(work_for_move, 0, 400);
        workers.scheduleAtFixedRate(work_for_all, 0, 400);

        // 初始包发送
        ServerPacket body;
        body.writeC(S_OPCODE_INITPACKET);
        body.writeD(2147483647);
        body.writeBytes((char *) FIRST_PACKET, sizeof(FIRST_PACKET));
        ServerPacket pkt(body.getLength() + 2);
        pkt.writeH(body.getLength() + 2);
        pkt.writeBytes(body.getBytes(), body.getLength());
        socket().sendBytes(pkt.getBytes(), pkt.getLength());

        // 处理来自客户端的数据包
        while (g_Running.load()) {
            char header[2];
            if (socket().receiveBytes(header, sizeof(header)) != 2) {
                app.logger().error(std::string("获取数据头失败"));
                break;
            }
            int len = (int)header[1] << 8 & 0xFF00 + (int)header[0] & 0xFF - 2;
            poco_assert(len < MAX_PACKET_SIZE);
            std::vector<char> buf((unsigned int)len);
            if (socket().receiveBytes(buf.data(), len) != len) {
                app.logger().error(std::string("获取数据失败"));
                break;
            }
            decrypt(buf.data(), (unsigned int)buf.size());

            unsigned int opcode = (unsigned int)buf[0] & 0xFF;
            // 客户端状态机
            if (opcode == C_OPCODE_COMMONCLICK || opcode == C_OPCODE_CHANGECHAR)
                status_ = SELECT;
            if (opcode == C_OPCODE_LOGINTOSERVER && status_ == LOGIN)
                continue;
            if (opcode == C_OPCODE_LOGINTOSERVEROK || opcode == C_OPCODE_RETURNTOLOGIN)
                status_ = LOGIN;
            // 将数据包交由对应处理队列
            if (opcode == C_OPCODE_CHANGECHAR || opcode == C_OPCODE_DROPITEM || opcode == C_OPCODE_DELETEINVENTORYITEM)
                work_for_item->append(buf);
            else if (opcode == C_OPCODE_MOVECHAR)
                work_for_move->append(buf);
            else
                work_for_all->append(buf);
        }
    }
    catch (Poco::Exception &e) {
        app.logger().log(e);
    }

    app.logger().information("请求处理结束");
}

}

