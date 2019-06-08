//
// Created by 范炜东 on 2019/5/9.
//

#include <fstream>
#include <exception>
#include "Logger.h"
#include "Opcodes.h"
#include "S_CommonNews.h"

S_CommonNews::S_CommonNews() : ServerPacket() {
  writeC(Opcodes::S_OPCODE_COMMONNEWS);
  std::string message;
  try {
    std::ifstream ifs;
    ifs.open("data/announcements.txt");
    if (ifs.is_open()) {
      std::string line;
      while (getline(ifs, line)) {
        message += line + "\n";
      }
    }
  } catch (std::exception &e) {
    LOG_ERROR << e.what();
  }
  writeS(message.c_str());
}