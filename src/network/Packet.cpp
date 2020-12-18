//
// Created by kyle on 2020/12/16.
//

#include <cassert>
#include "common/Buffer.h"
#include "common/Allocator.h"
#include "network/Packet.h"

namespace kge {

Packet::Packet():size_(0), rpos_(0), transfered_(0)  {
  data_ = Allocator::instance().balloc(MAX_BUF_SIZE);
}

Packet::Packet(std::size_t size):size_(size), rpos_(0), transfered_(0) {
  data_ = Allocator::instance().balloc(size);
}

Packet::~Packet() {
  if (data_)
    Allocator::instance().bfree(data_);
  rpos_ = size_ = 0;
}

Packet &Packet::operator<<(uint8_t value) {
  data_->write(size_, value);
  size_ += sizeof(uint8_t);
  return *this;
}

Packet &Packet::operator<<(uint16_t value) {
  data_->write(size_, value);
  size_ += sizeof(uint16_t);
  return *this;
}

Packet &Packet::operator<<(uint32_t value) {
  data_->write(size_, value);
  size_ += sizeof(uint32_t);
  return *this;
}

Packet &Packet::operator<<(uint64_t value) {
  data_->write(size_, value);
  size_ += sizeof(uint64_t);
  return *this;
}

Packet &Packet::operator<<(int8_t value) {
  data_->write(size_, static_cast<uint8_t>(value));
  size_ += sizeof(uint8_t);
  return *this;
}

Packet &Packet::operator<<(int16_t value) {
  data_->write(size_, static_cast<uint16_t>(value));
  size_ += sizeof(uint16_t);
  return *this;
}

Packet &Packet::operator<<(int32_t value) {
  data_->write(size_, static_cast<uint32_t>(value));
  size_ += sizeof(uint32_t);
  return *this;
}

Packet &Packet::operator<<(int64_t value) {
  data_->write(size_, static_cast<uint64_t>(value));
  size_ += sizeof(uint64_t);
  return *this;
}

Packet &Packet::operator<<(bool value) {
  data_->write(size_, static_cast<uint8_t>(value));
  size_ += sizeof(uint8_t);
  return *this;
}

Packet &Packet::operator<<(float value) {
  data_->write(size_, static_cast<uint32_t>(value));
  size_ += sizeof(uint32_t);
  return *this;
}

Packet &Packet::operator<<(double value) {
  data_->write(size_, static_cast<uint64_t>(value));
  size_ += sizeof(uint64_t);
  return *this;
}

Packet &Packet::operator<<(const std::string& value) {
  data_->write(size_, (const uint8_t *)(value.c_str()), value.size() + 1);
  size_ += value.size() + 1;
  return *this;
}

Packet &Packet::operator>>(uint8_t &value) {
  value = data_->read<uint8_t>(rpos_);
  rpos_ += sizeof(uint8_t);
  return *this;
}

Packet &Packet::operator>>(uint16_t &value) {
  value = data_->read<uint16_t>(rpos_);
  rpos_ += sizeof(uint16_t);
  return *this;
}

Packet &Packet::operator>>(uint32_t &value) {
  value = data_->read<uint32_t>(rpos_);
  rpos_ += sizeof(uint32_t);
  return *this;
}

Packet &Packet::operator>>(uint64_t &value) {
  value = data_->read<uint64_t>(rpos_);
  rpos_ += sizeof(uint64_t);
  return *this;
}

Packet &Packet::operator>>(int8_t &value) {
  value = static_cast<int8_t>(data_->read<uint8_t>(rpos_));
  rpos_ += sizeof(uint8_t);
  return *this;
}

Packet &Packet::operator>>(int16_t &value) {
  value = static_cast<int16_t>(data_->read<uint16_t>(rpos_));
  rpos_ += sizeof(uint16_t);
  return *this;
}

Packet &Packet::operator>>(int32_t &value) {
  value = static_cast<int32_t>(data_->read<uint32_t>(rpos_));
  rpos_ += sizeof(uint32_t);
  return *this;
}

Packet &Packet::operator>>(int64_t &value) {
  value = static_cast<int64_t>(data_->read<uint64_t>(rpos_));
  rpos_ += sizeof(uint64_t);
  return *this;
}

Packet &Packet::operator>>(bool &value) {
  value = static_cast<bool>(data_->read<uint8_t>(rpos_));
  rpos_ += sizeof(uint8_t);
  return *this;
}

Packet &Packet::operator>>(float &value) {
  value = static_cast<float>(data_->read<uint32_t>(rpos_));
  rpos_ += sizeof(uint32_t);
  return *this;
}

Packet &Packet::operator>>(double &value) {
  value = static_cast<double>(data_->read<uint64_t>(rpos_));
  rpos_ += sizeof(uint64_t);
  return *this;
}

Packet &Packet::operator>>(std::string &value) {
  value = data_->read(rpos_);
  rpos_ = value.size() + 1;
  return *this;
}

}