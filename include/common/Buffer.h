//
// Created by kyle on 2020/12/16.
//

#ifndef KGE_BUFFER_H
#define KGE_BUFFER_H

#include <cstddef>
#include <bit>
#include <string>
#include "Exception.h"

namespace kge {

#define MAX_BUF_SIZE 4096

template <std::size_t T>
inline void convert(uint8_t *val) {
  std::swap(*val, *(val + T -1));
  convert<T - 2>(val + 1);
}
template<> inline void convert<0>(uint8_t *) {}
template<> inline void convert<1>(uint8_t *) {}

#if std::endian::native == std::endian::big
template<typename T> inline void EndianConvert(T& val) { convert<sizeof<T>>((uint8_t)&val); }
#else
template<typename T> inline void EndianConvert(T&) { }
#endif
inline void EndianConvert(uint8_t&) {}

class Buffer {
public:
  Buffer() {}
  virtual ~Buffer() {}

  // 缓存信息
  uint8_t *data() { return data_; }
  virtual std::size_t capability() { return MAX_BUF_SIZE; }

  // 读写操作
  template<typename T>
  T read(size_t pos) const {
    if ((sizeof(T) + pos) > length)
      throw BufferException(true, pos, size_, sizeof(T));

    T val = *((const T*)&data_[pos]);
    EndianConvert(val);
    return val;
  }
  std::string read(std::size_t pos) {
    std::string s;
    while (pos < MAX_BUF_SIZE) {
      char c = static_cast<char>(data_[pos]);
      if (c == 0 || !isascii(c))
        break;
      s += c;
      pos++;
    }
    s += '\0';
    return std::move(s);
  }

  template<typename T>
  void write(std::size_t pos, T val) {
    EndianConvert(val);
    write(pos, (const uint8_t*)&val, sizeof(T));
  }
  void write(std::size_t pos, const uint8_t *data, std::size_t size) {
    if (!size)
      return;
    if ((pos + size) > MAX_BUF_SIZE)
      throw BufferException(false, pos, MAX_BUF_SIZE, size);

    std::memcpy(&data_[pos], data, size);
  }

public:
  Buffer* next;

protected:
  uint8_t data_[MAX_BUF_SIZE];
};

}

#endif //KGE_BUFFER_H


