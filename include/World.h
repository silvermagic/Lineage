//
// Created by kyle on 2020/12/22.
//

#ifndef KGE_WORLD_H
#define KGE_WORLD_H

#include "common/Singleton.h"

namespace kge {

class World : public Singleton<World> {
  World();
  virtual ~World();

  virtual void Update(uint32_t diff);

protected:
  virutal void handle_sessions(uint32_t diff);

protected:
  // 会话列表
};

}

#endif //KGE_WORLD_H
