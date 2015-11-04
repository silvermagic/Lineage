#include "model/map/TMap.h"
#include "model/TLocation.h"

TLocation::TLocation()
{
}

TLocation::TLocation(int x, int y, int mapId)
{
}

TLocation::TLocation(int x, int y, std::shared_ptr<TMap> map)
{
}

TLocation::TLocation(const TLocation&)
{
}

TLocation::TLocation(const TPoint& pt, int mapId)
{
}

TLocation::TLocation(const TPoint& pt, std::shared_ptr<TMap> map)
{
}

TLocation::~TLocation()
{
}


bool TLocation::equals(const TLocation& loc)
{
  return false;
}

const std::shared_ptr<TMap> TLocation::getMap()
{
  return std::const_pointer_cast<TMap>(_map);
}

unsigned int TLocation::getMapId()
{
  return 0;
}

int TLocation::hashCode()
{
  return 0;
}

TLocation TLocation::randomLocation(TLocation& baseLocation, int min, int max, bool isRandomTeleport)
{
  return TLocation();
}

TLocation TLocation::randomLocation(int max, bool isRandomTeleport)
{
  return TLocation();
}

TLocation TLocation::randomLocation(int min, int max, bool isRandomTeleport)
{
  return TLocation();
}

void TLocation::set(int x, int y, int mapId)
{
}

void TLocation::set(int x, int y, std::shared_ptr<TMap> map)
{
}

void TLocation::set(const TLocation& loc)
{
}

void TLocation::set(const TPoint& pt, unsigned int mapId)
{
}

void TLocation::set(const TPoint& pt, std::shared_ptr<TMap> map)
{
}

void TLocation::setMap(unsigned int mapId)
{
}

void TLocation::setMap(std::shared_ptr<TMap> map)
{
}

std::string TLocation::toString()
{
  return std::string();
}
