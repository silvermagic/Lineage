//
// Created by 范炜东 on 2019/4/24.
//

#include <cstring>
#include "ServerPacket.h"

ServerPacket::ServerPacket() : data_() {
}

ServerPacket::ServerPacket(std::size_t size) : data_() {
  data_.reserve(size);
}

char *ServerPacket::data() {
  return data_.data();
}

const char *ServerPacket::data() const {
  return data_.data();
}

std::size_t ServerPacket::size() const {
  return data_.size();
}

void ServerPacket::writeBytes(const char *value, std::size_t size) {
  if (value != nullptr)
    data_.insert(data_.end(), value, value + size);
}

void ServerPacket::writeC(unsigned int value) {
  data_.push_back(char(value & 0xFF));
}

void ServerPacket::writeD(unsigned int value) {
  data_.push_back(char(value & 0xFF));
  data_.push_back(char(value >> 8 & 0xFF));
  data_.push_back(char(value >> 16 & 0xFF));
  data_.push_back(char(value >> 24 & 0xFF));
}

void ServerPacket::writeF(double raw) {
  unsigned long long value = *reinterpret_cast<unsigned long long *>(&raw);
  data_.push_back(char(value & 0xFF));
  data_.push_back(char(value >> 8 & 0xFF));
  data_.push_back(char(value >> 16 & 0xFF));
  data_.push_back(char(value >> 24 & 0xFF));
  data_.push_back(char(value >> 32 & 0xFF));
  data_.push_back(char(value >> 40 & 0xFF));
  data_.push_back(char(value >> 48 & 0xFF));
  data_.push_back(char(value >> 56 & 0xFF));
}

void ServerPacket::writeH(unsigned int value) {
  data_.push_back(char(value & 0xFF));
  data_.push_back(char(value >> 8 & 0xFF));
}

void ServerPacket::writeS(const char *value) {
  if (value != nullptr) {
    data_.insert(data_.end(), value, value + std::strlen(value));
  }
  data_.push_back('\0');
}