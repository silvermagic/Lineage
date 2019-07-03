//
// Created by 范炜东 on 2019/6/19.
//

#ifndef PROJECT_DB_DEF_MAP_H
#define PROJECT_DB_DEF_MAP_H

#include <memory>

namespace db {
namespace def {

class Map : public std::enable_shared_from_this<Map> {
public:
  Map(int id, std::string note, int x, int y, int width, int height,
      bool underwater, bool markable, bool teleportable, bool escapable, bool useResurrection,
      bool usePainwand, bool enabledDeathPenalty, bool takePets,
      bool recallPets, bool usableItem, bool usableSkill);

  // 返回地图编号
  int id();

  // 返回地图名
  std::string note();

  // 获取地图起点X轴坐标
  int x();

  // 获取地图起点Y轴坐标
  int y();

  // 获取地图宽度
  int width();

  // 获取地图高度
  int height();

  // 返回地图是否位于水下
  bool isUnderwater();

  // 返回地图是否允许记忆坐标
  bool isMarkable();

  // 返回地图是否允许随机传送
  bool isTeleportable();

  // 返回地图是否允许传送回家
  bool isEscapable();

  // 返回地图是否允许复活
  bool isUseResurrection();

  // 返回地图是否允许使用松木魔杖
  bool isUsePainwand();

  // 返回地图死亡是否有惩罚
  bool isEnabledDeathPenalty();

  // 返回地图是否允许携带宠物
  bool isTakePets();

  // 返回地图是否允许召唤宠物
  bool isRecallPets();

  // 返回地图是否允许使用道具
  bool isUsableItem();

  // 返回地图是否允许使用技能
  bool isUsableSkill();

protected:
  int id_;
  std::string note_;
  int x_;
  int y_;
  int width_;
  int height_;
  bool is_underwater_;
  bool is_markable_;
  bool is_teleportable_;
  bool is_escapable_;
  bool is_use_resurrection_;
  bool is_use_painwand_;
  bool is_enabled_death_penalty_;
  bool is_take_pets_;
  bool is_recall_pets_;
  bool is_usable_item_;
  bool is_usable_skill_;
};

}
}

#endif //PROJECT_DB_DEF_MAP_H
