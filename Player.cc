//
// Created by 范炜东 on 2019/4/25.
//

#include "Logger.h"
#include "ConnectionManager.h"
#include "Opcodes.h"
#include "ClientPackets/C_ServerVersion.h"
#include "Player.h"

Player::Player(boost::asio::ip::tcp::socket socket, ConnectionManager &manager) : Connection(std::move(socket),
                                                                                             manager) {
}

Player::~Player() {
}

void Player::handle() {
  try {
    std::shared_ptr<ClientPacket> pkt = nullptr;
    unsigned int opcode = (unsigned int)read_msg_[0] & 0xFF;
    switch (opcode) {
      case Opcodes::C_OPCODE_BANPARTY:
        break;
      case Opcodes::C_OPCODE_SHIP: // 请求下船
        break;
      case Opcodes::C_OPCODE_TELEPORTLOCK: // 玩家传送锁定
        break;
      case Opcodes::C_OPCODE_SKILLBUYOK: // 请求学习魔法
        break;
      case Opcodes::C_OPCODE_ADDBUDDY: // 请求新增好友
        break;
      case Opcodes::C_OPCODE_WAREHOUSELOCK: // 请求变更仓库密码
        break;
      case Opcodes::C_OPCODE_DROPITEM: // 请求丢弃物品
        break;
      case Opcodes::C_OPCODE_BOARDNEXT: // 请求查看下一页公告栏的讯息
        break;
      case Opcodes::C_OPCODE_PETMENU: // 请求宠物汇报选单
        break;
      case Opcodes::C_OPCODE_JOINCLAN: // 请求加入血盟
        break;
      case Opcodes::C_OPCODE_GIVEITEM: // 请求给予物品
        break;
      case Opcodes::C_OPCODE_SETCASTLESECURITY: // 3.3C ClientPacket
        break;
      case Opcodes::C_OPCODE_USESKILL: // 请求使用技能
        break;
      case Opcodes::C_OPCODE_RESULT: // 请求取得列表中的项目
        break;
      case Opcodes::C_OPCODE_DELETECHAR: // 请求删除角色
        break;
      case Opcodes::C_OPCODE_BOARD: // 请求浏览公布栏
        break;
      case Opcodes::C_OPCODE_CHANGEPASS:
        break;
      case Opcodes::C_OPCODE_TRADEADDCANCEL: // 请求取消交易
        break;
      case Opcodes::C_OPCODE_USEITEM: // 请求使用物品
        break;
      case Opcodes::C_OPCODE_PROPOSE: // 请求结婚
        break;
      case Opcodes::C_OPCODE_BOARDDELETE: // 请求删除公告栏内容
        break;
      case Opcodes::C_OPCODE_CHANGEHEADING: // 请求改变角色朝向
        break;
      case Opcodes::C_OPCODE_BOOKMARKDELETE: // 请求删除记忆坐标
        break;
      case Opcodes::C_OPCODE_SELECTLIST: // 请求修理道具
        break;
      case Opcodes::C_OPCODE_SELECTTARGET: // 请求攻击指定目标(宠物&召唤)
        break;
      case Opcodes::C_OPCODE_DELEXCLUDE: // 请求使用开启名单(拒绝指定人物讯息)
        break;
      case Opcodes::C_OPCODE_BUDDYLIST: // 请求查询好友名单
        break;
      case Opcodes::C_OPCODE_SENDLOCATION: // 请求传送位置
        break;
      case Opcodes::C_OPCODE_TITLE: // 请求赋予封号
        break;
      case Opcodes::C_OPCODE_TRADEADDOK: // 请求完成交易
        break;
      case Opcodes::C_OPCODE_EMBLEM: // 请求上载盟徽
        break;
      case Opcodes::C_OPCODE_MOVECHAR: // 请求移动角色
        break;
      case Opcodes::C_OPCODE_CHECKPK: // 请求查询PK次数 請求查詢PK次數
        break;
      case Opcodes::C_OPCODE_COMMONCLICK: // 请求下一步(伺服器公告)
        break;
      case Opcodes::C_OPCODE_QUITGAME: // 请求离开游戏
        break;
      case Opcodes::C_OPCODE_DEPOSIT: // 请求将资金存入城堡仓库
        break;
      case Opcodes::C_OPCODE_BOOKMARK: // 请求增加记忆坐标
        break;
      case Opcodes::C_OPCODE_SHOP: // 请求开启个人商店
        break;
      case Opcodes::C_OPCODE_CHATWHISPER: // 请求使用密语聊天频道
        break;
      case Opcodes::C_OPCODE_PRIVATESHOPLIST: // 请求购买指定的个人商店商品
        break;
      case Opcodes::C_OPCODE_EXTCOMMAND: // 请求角色表情动作
        break;
      case Opcodes::C_OPCODE_CLIENTVERSION: // 请求验证客户端版本
        pkt = std::make_shared<C_ServerVersion>(read_msg_);
        break;
      case Opcodes::C_OPCODE_LOGINTOSERVER: // 请求登入角色
        break;
      case Opcodes::C_OPCODE_ATTR: // 请求点选项目的结果
        break;
      case Opcodes::C_OPCODE_NPCTALK: // 请求对话视窗
        break;
      case Opcodes::C_OPCODE_NEWCHAR: // 请求创造角色
        break;
      case Opcodes::C_OPCODE_TRADE: // 请求交易
        break;
      case Opcodes::C_OPCODE_DELBUDDY: // 请求删除好友
        break;
      case Opcodes::C_OPCODE_BANCLAN: // 请求驱逐血盟成员
        break;
      case Opcodes::C_OPCODE_FISHCLICK: // 请求钓鱼收竿
        break;
      case Opcodes::C_OPCODE_LEAVECLANE: // 请求离开血盟
        break;
      case Opcodes::C_OPCODE_TAXRATE: // 请求配置税收
        break;
      case Opcodes::C_OPCODE_RESTART: // 请求重新开始
        break;
      case Opcodes::C_OPCODE_ENTERPORTAL: // 请求传送(进入地监)
        break;
      case Opcodes::C_OPCODE_SKILLBUY: // 请求查询可以学习的魔法清单
        break;
      case Opcodes::C_OPCODE_TELEPORT: // 请求解除传送锁定
        break;
      case Opcodes::C_OPCODE_DELETEINVENTORYITEM: // 请求删除物品
        break;
      case Opcodes::C_OPCODE_CHAT: // 请求使用一般聊天频道
        break;
      case Opcodes::C_OPCODE_ARROWATTACK: // 请求使用远距攻击
        break;
      case Opcodes::C_OPCODE_USEPETITEM: // 请求使用宠物装备
        break;
      case Opcodes::C_OPCODE_EXCLUDE: // 请求使用拒绝名单(开启指定人物讯息)
        break;
      case Opcodes::C_OPCODE_FIX_WEAPON_LIST: // 请求查询损坏的道具
        break;
      case Opcodes::C_OPCODE_PLEDGE: // 请求查询血盟成员
        break;
      case Opcodes::C_OPCODE_PARTY:
        break;
      case Opcodes::C_OPCODE_NPCACTION: // 请求执行对话视窗的动作
        break;
      case Opcodes::C_OPCODE_EXIT_GHOST: // 请求退出观看模式
        break;
      case Opcodes::C_OPCODE_MAIL: // 请求打开邮箱
        break;
      case Opcodes::C_OPCODE_WHO: // 请求查询游戏人数
        break;
      case Opcodes::C_OPCODE_PICKUPITEM: // 请求拾取物品
        break;
      case Opcodes::C_OPCODE_CHARRESET: // 请求重置人物属性点数
        break;
      case Opcodes::C_OPCODE_AMOUNT: // 请求传回选取的数量
        break;
      case Opcodes::C_OPCODE_RANK: // 请求给予角色血盟阶级
        break;
      case Opcodes::C_OPCODE_FIGHT: // 请求决斗
        break;
      case Opcodes::C_OPCODE_DRAWAL: // 请求领取城堡仓库的资金
        break;
      case Opcodes::C_OPCODE_KEEPALIVE: // 请求更新连线状态
        break;
      case Opcodes::C_OPCODE_CHARACTERCONFIG: // 请求几率快捷键
        break;
      case Opcodes::C_OPCODE_CHATGLOBAL: // 请求使用广播聊天频道
        break;
      case Opcodes::C_OPCODE_WAR: // 请求宣战
        break;
      case Opcodes::C_OPCODE_CREATECLAN: // 请求创立血盟
        break;
      case Opcodes::C_OPCODE_LOGINTOSERVEROK: // 请求配置角色设定
        break;
      case Opcodes::C_OPCODE_LOGINPACKET: // 请求登入伺服器
        break;
      case Opcodes::C_OPCODE_DOOR: // 请求开门或关门
        break;
      case Opcodes::C_OPCODE_ATTACK: // 请求攻击对象
        break;
      case Opcodes::C_OPCODE_PUTHIRESOLDIER: // 3.3C ClientPacket
        break;
      case Opcodes::C_OPCODE_TRADEADDITEM: // 请求交易(添加物品)
        break;
      case Opcodes::C_OPCODE_SMS: // 请求传送简讯
        break;
      case Opcodes::C_OPCODE_LEAVEPARTY: // 请求退出退伍
        break;
      case Opcodes::C_OPCODE_CASTLESECURITY: // 请求管理城内治安
        break;
      case Opcodes::C_OPCODE_BOARDREAD: // 请求阅读公告栏讯息
        break;
      case Opcodes::C_OPCODE_CHANGECHAR: // 请求切换角色
        break;
      case Opcodes::C_OPCODE_PARTYLIST: // 请求查询队伍成员
        break;
      case Opcodes::C_OPCODE_XCHANGESKILL:
        break;
      case Opcodes::C_OPCODE_BOARDWRITE: // 请求撰写新的公告栏讯息
        break;
      case Opcodes::C_OPCODE_CREATEPARTY: // 请求邀请加入队伍或建立队伍
        break;
      case Opcodes::C_OPCODE_CAHTPARTY: // 请求聊天队伍
        break;
      case Opcodes::C_OPCODE_RETURNTOLOGIN: // 请求回到选人画面
        break;
      case Opcodes::C_OPCODE_HIRESOLDIER: // 请求雇佣雇佣兵列表(购买)
        break;
      case Opcodes::C_OPCODE_CLAN: // 请求血盟数据(例如盟标)
        break;
      case Opcodes::C_OPCODE_CHANGEWARTIME: // 修正城堡管理全部功能
        break;
      case Opcodes::C_OPCODE_PUTSOLDIER: // 请求配置已雇佣的士兵
        break;
      case Opcodes::C_OPCODE_SELECTWARTIME: // 请求变更攻城时间
        break;
      case Opcodes::C_OPCODE_PUTBOWSOLDIER: // 请求配置城墙上的弓箭手
        break;
      default:
        LOG_WARNING << "未处理的消息";
        connection_manager_.stop(shared_from_this());
        return;
    }
    pkt->handle(std::dynamic_pointer_cast<Player>(shared_from_this()));
  } catch (std::exception &e) {
    LOG_ERROR << e.what();
    connection_manager_.stop(shared_from_this());
  }
}