//
// Created by 范炜东 on 2019/6/17.
//

#include "EffectStateMachine.h"
#include "EffectTimer.h"

EffectTimer::EffectTimer(boost::asio::io_context io_context, std::shared_ptr<EffectStateMachine> esm) : timer_(io_context), esm_(esm) {
}

EffectTimer::~EffectTimer() {
}

void EffectTimer::stop() {
  auto self(shared_from_this());
  boost::asio::post(timer_.get_executor(), [self, this]() {
    esm_->transform(END);
  });
}

void EffectTimer::cancel() {
  auto self(shared_from_this());
  boost::asio::post(timer_.get_executor(), [self, this]() {
    if (timer_.expires_at(std::chrono::steady_clock::time_point::min()) == 0) {
      esm_->transform(BEGIN);
    }
  });
}

void EffectTimer::start() {
  auto self(shared_from_this());
  boost::asio::post(timer_.get_executor(), [self, this]() {
    esm_->transform(BEGIN);
    stop();
  });
}