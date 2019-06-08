//
// Created by 范炜东 on 2019/5/15.
//

#ifndef PROJECT_GENERATORCONTROLLER_H
#define PROJECT_GENERATORCONTROLLER_H

#include <atomic>

class GeneratorController : public Singleton<GeneratorController> {
public:
  GeneratorController();
  ~GeneratorController();

  // 初始化
  bool initialize();

  // 获取下一个编号
  int next();

protected:
  std::atomic<int> id_;
};

#endif //PROJECT_GENERATORCONTROLLER_H
