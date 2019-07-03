//
// Created by 范炜东 on 2019/6/17.
//

#include "../Logger.h"
#include "../Object.h"
#include "EffectStateMachine.h"

static const char* state_names[] = { "start", "active", "stop" };
static const char* event_names[] = { "begin", "end" };
EffectTranstion EffectStateMachine::transtion_tables_[] = {
        {  START, BEGIN, ACTIVE, &EffectStateMachine::on_active },
        {  START,   END,   STOP, &EffectStateMachine::on_stop },
        { ACTIVE, BEGIN, ACTIVE, &EffectStateMachine::on_active },
        { ACTIVE,   END,   STOP, &EffectStateMachine::on_stop },
        {   STOP, BEGIN,  START, &EffectStateMachine::on_start },
        {   STOP,   END,   STOP, nullptr },
};

EffectStateMachine::EffectStateMachine(std::shared_ptr<Object> target) : now_(INIT), target_(target) {
}

void EffectStateMachine::transform(EFFECT_EVENT event) {
  if (now_ == INIT) {
    if (on_start()) {
      now_ = START;
    } else {
      LOG_ERROR << "EffectStateMachine::process_event " << target_->toString() << "trigger transtion by " << event_names[event] << " from init to start failed";
    }
  } else {
    for (const auto& transtion : transtion_tables_) {
      if (transtion.now == now_ && transtion.event == event) {
        if (transtion.action == nullptr || (this->*transtion.action)()) {
          now_ = transtion.next;
        } else {
          LOG_ERROR << "EffectStateMachine::process_event " << target_->toString() << "trigger transtion by " << event_names[event] << " from " << state_names[now_] << " to " << state_names[transtion.next] << " failed";
        }
      }
    }
  }
}

int EffectStateMachine::id() {
  return -1;
}

EFFECT_STATUS EffectStateMachine::now() {
  return now_;
}

bool EffectStateMachine::on_start() {
  return true;
}

bool EffectStateMachine::on_stop() {
  return true;
}

bool EffectStateMachine::on_active() {
  return true;
}