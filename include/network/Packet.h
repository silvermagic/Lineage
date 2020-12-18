//
// Created by kyle on 2020/12/16.
//

#ifndef KGE_PACKET_H
#define KGE_PACKET_H

#include <cstddef>
#include <cstdint>
#include <string>
#include "common/Buffer.h"

namespace kge {

class Packet {
public:
  Packet();
  Packet(std::size_t size);
  virtual ~Packet();

  // 数据缓存
  virtual uint8_t *data() { return data_->data(); }
  // 总长度
  std::size_t size() { return size_; }
  void size(std::size_t size) { size_ = size; }

  // 异步传输字节记录（已读取/发送字节数）
  std::size_t transfered() { return transfered_; }
  void transfered(std::size_t transfered) { transfered_ += transfered; }

  // 数据读
  Packet &operator<<(uint8_t);
  Packet &operator<<(uint16_t);
  Packet &operator<<(uint32_t);
  Packet &operator<<(uint64_t);
  Packet &operator<<(int8_t);
  Packet &operator<<(int16_t);
  Packet &operator<<(int32_t);
  Packet &operator<<(int64_t);
  Packet &operator<<(bool);
  Packet &operator<<(float);
  Packet &operator<<(double);
  Packet &operator<<(const std::string&);

  // 数据写
  Packet &operator>>(uint8_t&);
  Packet &operator>>(uint16_t&);
  Packet &operator>>(uint32_t&);
  Packet &operator>>(uint64_t&);
  Packet &operator>>(int8_t&);
  Packet &operator>>(int16_t&);
  Packet &operator>>(int32_t&);
  Packet &operator>>(int64_t&);
  Packet &operator>>(bool&);
  Packet &operator>>(float&);
  Packet &operator>>(double&);
  Packet &operator>>(std::string&);

protected:
  std::size_t size_, rpos_, transfered_;
  Buffer *data_;
};

}

#endif //KGE_PACKET_H
