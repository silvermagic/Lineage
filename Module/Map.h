//
// Created by 范炜东 on 2018/12/13.
//

#ifndef LINEAGE_MAP_H
#define LINEAGE_MAP_H

#include <vector>
#include "Point.h"

namespace Lineage {

enum ZONE {
    COMBAT = -1, // 战斗区域
    NORMAL, // 一般区域
    SAFETY // 安全区域
};

class Map {
public:
    // 返回指定坐标是否位于地图内
    bool isInMap(const Point &pt);
    bool isInMap(int x, int y);

    // 返回指定坐标是否能通过
    bool isPassable(const Point &pt);
    bool isPassable(int x, int y);
    bool isPassable(const Point &pt, Towards t);
    bool isPassable(int x, int y, Towards t);

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
    bool isArrowPassable(const Point &pt, Towards t);
    bool isArrowPassable(int x, int y, Towards t);

    // 返回指定坐标是否是钓鱼区域
    bool isFishingZone(int x, int y);

    // 返回指定坐标是否存在门
    bool isExistDoor(int x, int y);

    // 读取/设置地图数据
    char tile(int x, int y);
    void tile(int x, int y, char value);

public:
    int id;
    std::string name;
    Point leftTop;
    Point rightBottom;
    double monsterAmount;
    double dropRate;
    bool isUnderwater;
    bool isMarkable;
    bool isTeleportable;
    bool isEscapable;
    bool isUseResurrection;
    bool isUsePainwand;
    bool isEnabledDeathPenalty;
    bool isTakePets;
    bool isRecallPets;
    bool isUsableItem;
    bool isUsableSkill;
    bool isArena;
    int width;
    int height;
    std::vector<char> tiles;
};

}

#endif //LINEAGE_MAP_H
