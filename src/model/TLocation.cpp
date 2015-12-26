#include "model/map/L1Map.h"
#include "model/TLocation.h"

TLocation::TLocation()
{
}

TLocation::TLocation(int x, int y, int mapId)
{
}

TLocation::TLocation(int x, int y, std::shared_ptr<L1Map> map)
{
}

TLocation::TLocation(const TLocation&)
{
}

TLocation::TLocation(const TPoint& pt, int mapId)
{
}

TLocation::TLocation(const TPoint& pt, std::shared_ptr<L1Map> map)
{
}

TLocation::~TLocation()
{
}


bool TLocation::equals(const TLocation& loc)
{
  return false;
}

const std::shared_ptr<L1Map> TLocation::geL1Map()
{
  return std::const_pointer_cast<L1Map>(_map);
}

unsigned int TLocation::geL1MapId()
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

void TLocation::set(int x, int y, std::shared_ptr<L1Map> map)
{
}

void TLocation::set(const TLocation& loc)
{
}

void TLocation::set(const TPoint& pt, unsigned int mapId)
{
}

void TLocation::set(const TPoint& pt, std::shared_ptr<L1Map> map)
{
}

void TLocation::seL1Map(unsigned int mapId)
{
}

void TLocation::seL1Map(std::shared_ptr<L1Map> map)
{
}

std::string TLocation::toString()
{
  return std::string();
}
