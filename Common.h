//
// Created by 范炜东 on 2019/5/15.
//

#ifndef PROJECT_COMMON_H
#define PROJECT_COMMON_H

#include <string>

enum {
  HEADER_LENGTH = 2,
  MAX_BODY_LENGTH = 4096
};

enum {
  SOUTH = 0,
  SOUTH_EAST = 1,
  EAST = 2,
  NORTH_EAST = 3,
  NORTH = 4,
  NORTH_WEST = 5,
  WEST = 6,
  SOUTH_WEST = 7
};

enum {
  OBJECT_TYPE_UNKNOWN = 1 << 0,
  OBJECT_TYPE_PC      = 1 << 1,
  OBJECT_TYPE_NPC     = 1 << 2,
  OBJECT_TYPE_PET     = 1 << 3
};

// 获取一个随机数（平均分布）
int random(int);

// 打印字节流
// 起始字节号    字节十六进制格式                                      字节ASCII格式
// 0000:        36 33 00 a8 03 00 00 00 d4 b0 01 00                63..........
std::string bytes_to_str(const char* buffer, int len);

#endif //PROJECT_COMMON_H
