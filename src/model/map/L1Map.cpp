#include "types/TPoint.h"
#include "model/map/L1Map.h"

L1Map::L1Map()
{
}

L1Map::~L1Map()
{
}

std::shared_ptr<L1Map> L1Map::newNull()
{
  static std::shared_ptr<L1Map> nullMap = std::dynamic_pointer_cast<L1Map>(std::make_shared<L1NullMap>());
  return nullMap;
}

bool L1Map::isNull()
{
  return false;
}

L1NullMap::L1NullMap()
{
}

L1NullMap::~L1NullMap()
{
}

int L1NullMap::getId()
{
  return 0;
}

int L1NullMap::getX()
{
  return 0;
}

int L1NullMap::getY()
{
  return 0;
}

int L1NullMap::getWidth()
{
  return 0;
}

int L1NullMap::getHeight()
{
  return 0;
}

int L1NullMap::getTile(int x, int y)
{
  return 0;
}


int L1NullMap::getOriginalTile(int x, int y)
{
  return 0;
}

bool L1NullMap::isInMap(const TPoint& pt)
{
  return false;
}

bool L1NullMap::isInMap(int x, int y)
{
  return false;
}

bool L1NullMap::isPassable(const TPoint& pt)
{
  return false;
}

bool L1NullMap::isPassable(int x, int y)
{
  return false;
}

bool L1NullMap::isPassable(const TPoint& pt, int heading)
{
  return false;
}

bool L1NullMap::isPassable(int x, int y, int heading)
{
  return false;
}

void L1NullMap::setPassable(const TPoint& pt, bool isPassable)
{
}

void L1NullMap::setPassable(int x, int y, bool isPassable)
{
}

bool L1NullMap::isArrowPassable(const TPoint& pt)
{
  return false;
}

bool L1NullMap::isArrowPassable(int x, int y)
{
  return false;
}

bool L1NullMap::isArrowPassable(const TPoint& pt, int heading)
{
  return false;
}

bool L1NullMap::isArrowPassable(int x, int y, int heading)
{
  return false;
}

bool L1NullMap::isSafetyZone(const TPoint& pt)
{
  return false;
}

bool L1NullMap::isSafetyZone(int x, int y)
{
  return false;
}

bool L1NullMap::isCombatZone(const TPoint& pt)
{
  return false;
}

bool L1NullMap::isCombatZone(int x, int y)
{
  return false;
}

bool L1NullMap::isNormalZone(const TPoint& pt)
{
  return false;
}

bool L1NullMap::isNormalZone(int x, int y)
{
  return false;
}

bool L1NullMap::isUnderwater()
{
  return false;
}

bool L1NullMap::isMarkable()
{
  return false;
}

bool L1NullMap::isTeleportable()
{
  return false;
}

bool L1NullMap::isEscapable()
{
  return false;
}

bool L1NullMap::isUseResurrection()
{
  return false;
}

bool L1NullMap::isUsePainwand()
{
  return false;
}

bool L1NullMap::isEnabledDeathPenalty()
{
  return false;
}

bool L1NullMap::isTakePets()
{
  return false;
}

bool L1NullMap::isRecallPets()
{
  return false;
}

bool L1NullMap::isUsableItem()
{
  return false;
}

bool L1NullMap::isUsableSkill()
{
  return false;
}

bool L1NullMap::isFishingZone(int x, int y)
{
  return false;
}

bool L1NullMap::isExistDoor(int x, int y)
{
  return false;
}

std::string L1NullMap::toString(const TPoint& pt)
{
  return std::string();
}

bool L1NullMap::isNull()
{
  return true;
}
