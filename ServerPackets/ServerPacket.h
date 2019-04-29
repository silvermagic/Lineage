//
// Created by 范炜东 on 2019/4/24.
//

#ifndef PROJECT_SERVERPACKET_H
#define PROJECT_SERVERPACKET_H

#include <vector>
#include <cstddef>

class ServerPacket {
public:
  ServerPacket();
  ServerPacket(std::size_t size);

  // 获取字节流
  char * data();
  const char * data() const;

  // 获取包长度
  std::size_t size() const;

  // 写入字节流
  void writeBytes(const char *, std::size_t);

  // 写入一个字节
  void writeC(unsigned int);

  // 写入一个双字
  void writeD(unsigned int);

  // 写入一个浮点数
  void writeF(double);

  // 写入一个字
  void writeH(unsigned int);

  // 写入字符串
  void writeS(const char *);

protected:
  std::vector<char> data_;
};

#endif //PROJECT_SERVERPACKET_H
