//
// Created by 范炜东 on 2019/6/17.
//

#ifndef PROJECT_EFFECTTIMER_H
#define PROJECT_EFFECTTIMER_H

#include <memory>
#include <boost/asio.hpp>

class EffectStateMachine;
class EffectTimer : public std::enable_shared_from_this<EffectTimer> {
public:
  EffectTimer(boost::asio::io_context, std::shared_ptr<EffectStateMachine>);
  ~EffectTimer();

  // 停止效果计时器
  void stop();

  // 取消效果计时器
  void cancel();

  // 启动效果计时器
  void start();

protected:
  boost::asio::steady_timer timer_;
  std::shared_ptr<EffectStateMachine> esm_;
};

#endif //PROJECT_EFFECTTIMER_H
