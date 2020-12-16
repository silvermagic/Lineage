//
// Created by kyle on 2020/12/16.
//

#include "common/Buffer.h"
#include "common/Allocator.h"

namespace kge {

KGE_SINGLETON_INIT(Allocator)

Allocator::Allocator(std::size_t size):freelist_(nullptr) {
  buffers_.resize(size);
  for (std::size_t i = 0; i < buffers_.size(); i++) {
    bfree(&buffers_[i]);
  }
}

// TODO: 未来可以有大小不同的Buffer，存放在不同链中
Buffer* Allocator::balloc(std::size_t size) {
  const std::lock_guard<std::mutex> lock(mutex_);
  Buffer *r;
  r = freelist_;
  if (r)
    freelist_ = r->next;
  return r;
}

void Allocator::bfree(Buffer *buffer) {
  const std::lock_guard<std::mutex> lock(mutex_);
  if (buffer != nullptr) {
    buffer->next = freelist_;
    freelist_ = buffer;
  }
}

}