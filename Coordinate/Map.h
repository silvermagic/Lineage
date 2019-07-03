//
// Created by 范炜东 on 2019/6/19.
//

#ifndef PROJECT_MAP_H
#define PROJECT_MAP_H

#include <vector>
#include "Templates/Map.h"
#include "TowerAoi.h"
#include "Point.h"

enum ZONE {
  COMBAT = -1,
  NORMAL,
  SAFETY
};

class Map : public db::def::Map {
public:
  Map(int id, std::string note, int x, int y, int width, int height,
      bool underwater, bool markable, bool teleportable, bool escapable, bool useResurrection,
      bool usePainwand, bool enabledDeathPenalty, bool takePets,
      bool recallPets, bool usableItem, bool usableSkill);

  ~Map();

  // 加载瓦片地图数据
  bool initialize();

  // 返回指定坐标是否位于地图内
  bool isInMap(const Point &pt);
  bool isInMap(int x, int y);

  // 返回指定坐标是否能通过
  bool isPassable(const Point &pt);
  bool isPassable(int x, int y);
  bool isPassable(const Point &pt, int t);
  bool isPassable(int x, int y, int t);

  // 设置指定坐标是否允许通过
  void setPassable(const Point &pt, bool isPassable);
  void setPassable(int x, int y, bool isPassable);

  // 返回指定坐标是否是安全区域
  bool isSafetyZone(const Point &pt);
  bool isSafetyZone(int x, int y);

  // 返回指定坐标是否是战斗区域
  bool isCombatZone(const Point &pt);
  bool isCombatZone(int x, int y);

  // 返回指定坐标是否是一般区域
  bool isNormalZone(const Point &pt);
  bool isNormalZone(int x, int y);

  // 返回指定坐标是否允许箭矢通过
  bool isArrowPassable(const Point &pt);
  bool isArrowPassable(int x, int y);
  bool isArrowPassable(const Point &pt, int t);
  bool isArrowPassable(int x, int y, int t);

  // 返回指定坐标是否是钓鱼区域
  bool isFishingZone(int x, int y);

  // 返回指定坐标是否存在门
  bool isExistDoor(int x, int y);

protected:
  // 获取地图瓦片信息
  unsigned char tile(int x, int y);

  // 设置地图瓦片信息
  void tile(int x, int y, unsigned char value);

protected:
  TowerAoi aoi_;
  std::vector<unsigned char> tiles_;
};

#endif //PROJECT_MAP_H
