//
// Created by kyle on 2020/12/16.
//

#include <format>
#include <stdexcept>
#include "common/Exception.h"
#include "common/Buffer.h"

namespace kge {

Buffer::Buffer(std::size_t headroom, std::size_t capacity):headroom(headroom) {
  data.resize(capacity);
}

Buffer::~Buffer() {
  data.clear();
}

void Buffer::read(std::size_t pos, uint8_t  *val) {
  if ((pos + sizeof(uint8_t)) > length)
    throw BufferException(true, pos, length, sizeof(uint8_t));

  *val = data[pos];
}

void Buffer::read(std::size_t pos, uint16_t *val) {
  if ((pos + sizeof(uint16_t)) > length)
    throw std::invalid_argument(std::format("read at {} out of {}", pos, length));

  *val = data[pos];
}

void Buffer::read(std::size_t pos, uint32_t *val) {
  if ((pos + sizeof(uint32_t)) > length)
    throw std::invalid_argument(std::format("read at {} out of {}", pos, length));
}

void Buffer::read(std::size_t pos, uint64_t *val) {
  if ((pos + sizeof(uint64_t)) > length)
    throw std::invalid_argument(std::format("read at {} out of {}", pos, length));
}

std::string Buffer::read(std::size_t pos) {
  if (pos > length)
    throw std::invalid_argument(std::format("read at {} out of {}", pos, length));
}

void Buffer::write(std::size_t pos, uint8_t val) {

}

void Buffer::write(std::size_t pos, uint16_t val) {

}

void Buffer::write(std::size_t pos, uint32_t val) {

}

void Buffer::write(std::size_t pos, uint64_t val) {

}

void Buffer::write(std::size_t pos, std::string val) {

}

}
