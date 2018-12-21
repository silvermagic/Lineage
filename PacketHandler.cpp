//
// Created by 范炜东 on 2019/1/14.
//

#include <Poco/Util/Application.h>
#include "Opcodes.h"
#include "ClientPackets/C_ServerVersion.h"
#include "ClientPackets/C_AuthLogin.h"
#include "PacketHandler.h"

namespace Lineage {

using Poco::Util::Application;

PacketHandler::PacketHandler(Lineage::ClientThread &client) :
        client_(client) {

}

void PacketHandler::append(std::vector<char> &data) {
    FastMutex::ScopedLock lock(mutex_);
    buffer_.push(data);
}

void PacketHandler::run() {
    // 降低锁粒度
    std::queue<std::vector<char>> buffer;
    {
        FastMutex::ScopedLock lock(mutex_);
        buffer.swap(buffer_);
    }

    Application &app = Application::instance();

    try {
        bool next = true;
        // 数据包处理
        while (!buffer.empty() && next) {
            auto data = buffer.front();
            switch (data[0]) {
                case C_OPCODE_BANPARTY:
                    break;
                case C_OPCODE_SHIP:
                    break;
                case C_OPCODE_TELEPORTLOCK:
                    break;
                case C_OPCODE_SKILLBUYOK:
                    break;
                case C_OPCODE_ADDBUDDY:
                    break;
                case C_OPCODE_WAREHOUSELOCK:
                    break;
                case C_OPCODE_DROPITEM:
                    break;
                case C_OPCODE_BOARDNEXT:
                    break;
                case C_OPCODE_PETMENU:
                    break;
                case C_OPCODE_JOINCLAN:
                    break;
                case C_OPCODE_GIVEITEM:
                    break;
                case C_OPCODE_SETCASTLESECURITY:
                    break;
                case C_OPCODE_USESKILL:
                    break;
                case C_OPCODE_RESULT:
                    break;
                case C_OPCODE_DELETECHAR:
                    break;
                case C_OPCODE_BOARD:
                    break;
                case C_OPCODE_CHANGEPASS:
                    break;
                case C_OPCODE_TRADEADDCANCEL:
                    break;
                case C_OPCODE_USEITEM:
                    break;
                case C_OPCODE_PROPOSE:
                    break;
                case C_OPCODE_BOARDDELETE:
                    break;
                case C_OPCODE_CHANGEHEADING:
                    break;
                case C_OPCODE_BOOKMARKDELETE:
                    break;
                case C_OPCODE_SELECTLIST:
                    break;
                case C_OPCODE_SELECTTARGET:
                    break;
                case C_OPCODE_DELEXCLUDE:
                    break;
                case C_OPCODE_BUDDYLIST:
                    break;
                case C_OPCODE_SENDLOCATION:
                    break;
                case C_OPCODE_TITLE:
                    break;
                case C_OPCODE_TRADEADDOK:
                    break;
                case C_OPCODE_EMBLEM:
                    break;
                case C_OPCODE_MOVECHAR:
                    break;
                case C_OPCODE_CHECKPK:
                    break;
                case C_OPCODE_COMMONCLICK:
                    break;
                case C_OPCODE_QUITGAME:
                    break;
                case C_OPCODE_DEPOSIT:
                    break;
                case C_OPCODE_BEANFUN_LOGIN:
                    break;
                case C_OPCODE_BOOKMARK:
                    break;
                case C_OPCODE_SHOP:
                    break;
                case C_OPCODE_CHATWHISPER:
                    break;
                case C_OPCODE_PRIVATESHOPLIST:
                    break;
                case C_OPCODE_EXTCOMMAND:
                    break;
                case C_OPCODE_UNKOWN1:
                    break;
                case C_OPCODE_CLIENTVERSION:
                {
                    C_ServerVersion c(data);
                    next = c.handle(client_);
                    break;
                }
                case C_OPCODE_LOGINTOSERVER:
                    break;
                case C_OPCODE_ATTR:
                    break;
                case C_OPCODE_NPCTALK:
                    break;
                case C_OPCODE_NEWCHAR:
                    break;
                case C_OPCODE_TRADE:
                    break;
                case C_OPCODE_DELBUDDY:
                    break;
                case C_OPCODE_BANCLAN:
                    break;
                case C_OPCODE_FISHCLICK:
                    break;
                case C_OPCODE_LEAVECLANE:
                    break;
                case C_OPCODE_TAXRATE:
                    break;
                case C_OPCODE_RESTART:
                    break;
                case C_OPCODE_ENTERPORTAL:
                    break;
                case C_OPCODE_SKILLBUY:
                    break;
                case C_OPCODE_TELEPORT:
                    break;
                case C_OPCODE_DELETEINVENTORYITEM:
                    break;
                case C_OPCODE_CHAT:
                    break;
                case C_OPCODE_ARROWATTACK:
                    break;
                case C_OPCODE_USEPETITEM:
                    break;
                case C_OPCODE_EXCLUDE:
                    break;
                case C_OPCODE_FIX_WEAPON_LIST:
                    break;
                case C_OPCODE_PLEDGE:
                    break;
                case C_OPCODE_PARTY:
                    break;
                case C_OPCODE_NPCACTION:
                    break;
                case C_OPCODE_EXIT_GHOST:
                    break;
                case C_OPCODE_CALL:
                    break;
                case C_OPCODE_MAIL:
                    break;
                case C_OPCODE_WHO:
                    break;
                case C_OPCODE_PICKUPITEM:
                    break;
                case C_OPCODE_CHARRESET:
                    break;
                case C_OPCODE_AMOUNT:
                    break;
                case C_OPCODE_RANK:
                    break;
                case C_OPCODE_FIGHT:
                    break;
                case C_OPCODE_DRAWAL:
                    break;
                case C_OPCODE_KEEPALIVE:
                    break;
                case C_OPCODE_CHARACTERCONFIG:
                    break;
                case C_OPCODE_CHATGLOBAL:
                    break;
                case C_OPCODE_WAR:
                    break;
                case C_OPCODE_CREATECLAN:
                    break;
                case C_OPCODE_LOGINTOSERVEROK:
                    break;
                case C_OPCODE_LOGINPACKET:
                {
                    C_AuthLogin c(data);
                    next = c.handle(client_);
                    break;
                }
                case C_OPCODE_DOOR:
                    break;
                case C_OPCODE_ATTACK:
                    break;
                case C_OPCODE_PUTHIRESOLDIER:
                    break;
                case C_OPCODE_TRADEADDITEM:
                    break;
                case C_OPCODE_SMS:
                    break;
                case C_OPCODE_LEAVEPARTY:
                    break;
                case C_OPCODE_CASTLESECURITY:
                    break;
                case C_OPCODE_BOARDREAD:
                    break;
                case C_OPCODE_CHANGECHAR:
                    break;
                case C_OPCODE_PARTYLIST:
                    break;
                case C_OPCODE_XCHANGESKILL:
                    break;
                case C_OPCODE_BOARDWRITE:
                    break;
                case C_OPCODE_CREATEPARTY:
                    break;
                case C_OPCODE_CAHTPARTY:
                    break;
                case C_OPCODE_RETURNTOLOGIN:
                    break;
                case C_OPCODE_HIRESOLDIER:
                    break;
                case C_OPCODE_CLAN:
                    break;
                case C_OPCODE_CHANGEWARTIME:
                    break;
                case C_OPCODE_PUTSOLDIER:
                    break;
                case C_OPCODE_SELECTWARTIME:
                    break;
                case C_OPCODE_PUTBOWSOLDIER:
                    break;
                default:
                    next = true;
            }
            buffer.pop();
        }
    } catch (const std::out_of_range &e) {
        app.logger().error(e.what());
    }
}

}