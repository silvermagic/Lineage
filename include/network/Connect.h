//
// Created by kyle on 2020/12/22.
//

#ifndef KGE_CONNECT_H
#define KGE_CONNECT_H

#include <atomic>
#include <memory>
#include <queue>
#include "Packet.h"

namespace kge {

// 只能由单线程io_context驱动，读取和发送不存在多线程竞争问题，但是连接关闭可能由不同线程发起
class Connect : public std::enable_shared_from_this<Connect> {
public:
  Connect() {}

  virtual ~Connect() {
    if (buffer_)
      buffer_ = nullptr;
    std::queue<std::shared_ptr<Packet>>().swap(write_queue_);
  }

  // 开启数据包接收
  void Start() {
    do_handshake();
  }

  // 投递待发送的数据包
  void Post(std::shared_ptr<Packet> pkt) {
    write_queue_.push(pkt);
  }

  // 数据包发送处理
  bool Send() {
    if (closed_)
      return false;

    if (write_queue_.empty() && !closing_)
      return true;

    while(do_send());

    return true;
  }

  void Close(bool delay = false) {
    if (delay)
      closing_ = true;
    else {
      closed_ = true;
      do_close();
    }
  }

protected:
  virtual void do_handshake() {
    do_read();
  }

  virtual void do_read() = 0;

  virtual bool do_send() = 0;

  virtual void do_close() = 0;

  // 数据包处理，例如交由Session处理，然后重新获取一个空的数据包
  virtual void do_handle() {
    if (buffer_->transfered() == buffer_->size())
    {
      buffer_ = std::make_shared<Packet>(MAX_BUF_SIZE);
    }
  }

protected:
  std::atomic<bool> closed_, closing_;
  std::shared_ptr<Packet> buffer_;
  std::queue<std::shared_ptr<Packet>> write_queue_;
};

}

#endif //KGE_CONNECT_H
