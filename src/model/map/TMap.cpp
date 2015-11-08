#include "types/TPoint.h"
#include "model/map/TMap.h"

TMap::TMap()
{
}

TMap::~TMap()
{
}

std::shared_ptr<TMap> TMap::newNull()
{
  static std::shared_ptr<TMap> nullMap = std::dynamic_pointer_cast<TMap>(std::make_shared<TNullMap>());
  return nullMap;
}

bool TMap::isNull()
{
  return false;
}

TNullMap::TNullMap()
{
}

TNullMap::~TNullMap()
{
}

int TNullMap::getId()
{
  return 0;
}

int TNullMap::getX()
{
  return 0;
}

int TNullMap::getY()
{
  return 0;
}

int TNullMap::getWidth()
{
  return 0;
}

int TNullMap::getHeight()
{
  return 0;
}

int TNullMap::getTile(int x, int y)
{
  return 0;
}


int TNullMap::getOriginalTile(int x, int y)
{
  return 0;
}

bool TNullMap::isInMap(const TPoint& pt)
{
  return false;
}

bool TNullMap::isInMap(int x, int y)
{
  return false;
}

bool TNullMap::isPassable(const TPoint& pt)
{
  return false;
}

bool TNullMap::isPassable(int x, int y)
{
  return false;
}

bool TNullMap::isPassable(const TPoint& pt, int heading)
{
  return false;
}

bool TNullMap::isPassable(int x, int y, int heading)
{
  return false;
}

void TNullMap::setPassable(const TPoint& pt, bool isPassable)
{
}

void TNullMap::setPassable(int x, int y, bool isPassable)
{
}

bool TNullMap::isArrowPassable(const TPoint& pt)
{
  return false;
}

bool TNullMap::isArrowPassable(int x, int y)
{
  return false;
}

bool TNullMap::isArrowPassable(const TPoint& pt, int heading)
{
  return false;
}

bool TNullMap::isArrowPassable(int x, int y, int heading)
{
  return false;
}

bool TNullMap::isSafetyZone(const TPoint& pt)
{
  return false;
}

bool TNullMap::isSafetyZone(int x, int y)
{
  return false;
}

bool TNullMap::isCombatZone(const TPoint& pt)
{
  return false;
}

bool TNullMap::isCombatZone(int x, int y)
{
  return false;
}

bool TNullMap::isNormalZone(const TPoint& pt)
{
  return false;
}

bool TNullMap::isNormalZone(int x, int y)
{
  return false;
}

bool TNullMap::isUnderwater()
{
  return false;
}

bool TNullMap::isMarkable()
{
  return false;
}

bool TNullMap::isTeleportable()
{
  return false;
}

bool TNullMap::isEscapable()
{
  return false;
}

bool TNullMap::isUseResurrection()
{
  return false;
}

bool TNullMap::isUsePainwand()
{
  return false;
}

bool TNullMap::isEnabledDeathPenalty()
{
  return false;
}

bool TNullMap::isTakePets()
{
  return false;
}

bool TNullMap::isRecallPets()
{
  return false;
}

bool TNullMap::isUsableItem()
{
  return false;
}

bool TNullMap::isUsableSkill()
{
  return false;
}

bool TNullMap::isFishingZone(int x, int y)
{
  return false;
}

bool TNullMap::isExistDoor(int x, int y)
{
  return false;
}

std::string TNullMap::toString(const TPoint& pt)
{
  return std::string();
}

bool TNullMap::isNull()
{
  return true;
}
