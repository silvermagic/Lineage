//
// Created by kyle on 2020/12/16.
//

#ifndef KGE_EXCEPTION_H
#define KGE_EXCEPTION_H

#include <format>
#include <exception>

namespace kge {

class BufferException : std::exception {
public:
  BufferException(bool rw, std::size_t pos, std::size_t size, std::size_t opsize): rw_(rw), size_(size), opsize_(opsize) {
  }
  virtual const char* what() const override {
    return std::format("{} buffer at (pos:{}, size:{}, opsize{})!\n").c_str();
  }

protected:
  bool rw_; // true-读 false-写
  std::size_t pos_; // 读/写起始地址
  std::size_t size_; // 缓存最大长度
  std::size_t opsize_; // 读/写请求长度
};

}

#endif //KGE_EXCEPTION_H
