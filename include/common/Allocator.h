//
// Created by kyle on 2020/12/16.
//

#ifndef KGE_BUFFERALLOCATOR_H
#define KGE_BUFFERALLOCATOR_H

#include <cstddef>
#include <vector>
#include <mutex>
#include "Singleton.h"

namespace kge {

// 简易内存分配器
class Buffer;
class Allocator : public Singleton<Allocator> {
public:
  Allocator(std::size_t size);
  ~Allocator();

  Buffer* balloc(std::size_t size);
  void bfree(Buffer*);

protected:
  std::mutex mutex_;
  Buffer *freelist_;
  std::vector<Buffer> buffers_;
};

}

#endif //KGE_BUFFERALLOCATOR_H
