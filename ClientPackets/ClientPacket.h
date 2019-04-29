//
// Created by 范炜东 on 2019/4/24.
//

#ifndef PROJECT_CLIENTPACKET_H
#define PROJECT_CLIENTPACKET_H

#include <string>
#include <vector>
#include <memory>
#include <cstddef>

class Player;
class ClientPacket {
public:
  ClientPacket(std::vector<char> &data);

  // 获取操作码
  unsigned int opcode();

  // 读取字节流
  std::vector<char> readBytes();

  // 读取1个字节
  unsigned int readC();

  // 读取3个字节
  unsigned int readCH();

  // 读取4个字节
  unsigned int readD();

  // 读取8个字节
  double readF();

  // 读取2个字节
  unsigned int readH();

  // 读取字符串
  std::string readS();

  // 处理数据包
  virtual void handle(std::shared_ptr<Player>) = 0;

protected:
  std::size_t offset_; // 已读取位置偏移
  unsigned int opcode_; // 操作码
  std::vector<char> data_;
};

#endif //PROJECT_CLIENTPACKET_H
