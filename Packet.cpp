//
// Created by kyle on 2020/12/16.
//

#include <cassert>
#include "common/Buffer.h"
#include "common/Allocator.h"
#include "common/Packet.h"

namespace kge {

Packet::Packet(std::size_t headroom):headroom_(headroom), size_(headroom), rpos_(headroom)  {
  assert(headroom <= sizeof(std::size_t));
  data_ = Allocator::instance().balloc(MAX_BUF_SIZE);
}

Packet::Packet(std::size_t headroom, std::size_t size):headroom_(headroom), size_(size), rpos_(headroom) {
  assert(headroom <= sizeof(std::size_t));
  data_ = Allocator::instance().balloc(size);
}

Packet::~Packet() {
  if (data_)
    Allocator::instance().bfree(data_);
  rpos_ = headroom_ = size_ = 0;
}

std::size_t Packet::hdr() {
  switch (headroom_) {
    case sizeof(uint8_t):
      return static_cast<std::size_t>(data_->read<uint8_t>(0));
    case sizeof(uint16_t):
      return static_cast<std::size_t>(data_->read<uint16_t>(0));
    case sizeof(uint32_t):
      return static_cast<std::size_t>(data_->read<uint32_t>(0));
    case sizeof(uint64_t):
      return static_cast<std::size_t>(data_->read<uint64_t>(0));
    default:
      return 0;
  }
}

void Packet::hdr(std::size_t value) {
  switch (headroom_) {
    case sizeof(uint8_t): {
      uint8_t v = static_cast<uint8_t>(value);
      EndianConvert(v);
      data_->write(0, v);
      break;
    }
    case sizeof(uint16_t): {
      uint16_t v = static_cast<uint16_t>(value);
      EndianConvert(v);
      data_->write(0, v);
      break;
    }
    case sizeof(uint32_t): {
      uint32_t v = static_cast<uint32_t>(value);
      EndianConvert(v);
      data_->write(0, v);
      break;
    }
    case sizeof(uint64_t): {
      uint64_t v = static_cast<uint64_t>(value);
      EndianConvert(v);
      data_->write(0, v);
      break;
    }
  }
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