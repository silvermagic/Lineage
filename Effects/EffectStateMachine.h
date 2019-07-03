//
// Created by 范炜东 on 2019/6/17.
//

#ifndef PROJECT_EFFECTSTATEMACHINE_H
#define PROJECT_EFFECTSTATEMACHINE_H

#include <memory>

enum EFFECT_STATUS {
  INIT = -1, // 初始伪状态
  START, // 效果生效
  ACTIVE, // 效果持续生效
  STOP // 效果失效
};

enum EFFECT_EVENT {
  BEGIN = 0, // 释放技能
  END // 技能效果结束
};

class EffectStateMachine;
class EffectTranstion {
public:
  EFFECT_STATUS now;
  EFFECT_EVENT event;
  EFFECT_STATUS next;
  bool (EffectStateMachine::*action)();
};

class Object;
class EffectStateMachine {
public:
  EffectStateMachine(std::shared_ptr <Object>);

  // 触发状态机转换
  void transform(EFFECT_EVENT);

  // 获取特效标识
  virtual int id();

  // 获取特效实例当前所处状态
  EFFECT_STATUS now();

protected:
  // 效果生效回调
  virtual bool on_start();

  // 效果失效回调
  virtual bool on_stop();

  // 效果持续生效回调
  virtual bool on_active();

protected:
  EFFECT_STATUS now_;
  std::shared_ptr<Object> target_; // 效果作用的目标对象
  static EffectTranstion transtion_tables_[]; // 状态转换表
};

#endif //PROJECT_EFFECTSTATEMACHINE_H
