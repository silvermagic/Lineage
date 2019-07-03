//
// Created by 范炜东 on 2019/6/19.
//

#include "Logger.h"
#include "ThreadPoolManager.h"
#include "Tables/Map.h"
#include "Map.h"
#include "WorldMap.h"

bool WorldMap::initialize() {
  LOG_INFO << "WorldMap::initialize building coordinate system";

  // 从数据库加载地图信息
  auto maps = db::oper::Map::query();
  for (auto map : maps) {
    maps_[map->id()] = std::make_shared<Map>(map->id(), map->note(), map->x(), map->y(), map->width(), map->height(),
                                             map->isUnderwater(), map->isMarkable(), map->isTeleportable(),
                                             map->isEscapable(), map->isUseResurrection(), map->isUsePainwand(),
                                             map->isEnabledDeathPenalty(), map->isTakePets(), map->isRecallPets(),
                                             map->isUsableItem(), map->isUsableSkill());
  }

  // 加载地图数据，并构建AOI
  for (auto iter = maps_.begin(); iter != maps_.end(); iter++) {
    int key = iter->first;
    boost::asio::post(ThreadPoolManager::instance(), [this, key]() {
      if (!maps_[key]->initialize()) {
        maps_[key] = nullptr;
      }
    });
  }

  // 等待加载完成
  ThreadPoolManager::instance().join();
  for (auto iter = maps_.begin(); iter != maps_.end(); iter++) {
    if (iter->second == nullptr)
      return false;
  }

  LOG_INFO << "WorldMap::initialize success";
  return true;
}

std::shared_ptr<Map> WorldMap::operator[](int id) {
  auto iter = maps_.find(id);
  if (iter != maps_.end())
    return iter->second;

  return nullptr;
}