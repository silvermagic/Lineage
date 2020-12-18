//
// Created by kyle on 2020/12/17.
//

#ifndef KGE_ENGINE_H
#define KGE_ENGINE_H

#include <thread>
#include <vector>
#include <boost/asio.hpp>

namespace kge {

class Engine {
public:
  void run();

protected:
  boost::asio::io_context io_context_; // 异步操作执行上下文
  boost::asio::signal_set signals_; // 退出信号处理
  std::vector<std::thread> workers_;
};

}

#endif //KGE_ENGINE_H
