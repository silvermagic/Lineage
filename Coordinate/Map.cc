//
// Created by 范炜东 on 2019/6/19.
//

#include <fstream>
#include <functional>
#include <boost/format.hpp>
#include <boost/algorithm/string.hpp>
#include "Config.h"
#include "Common.h"
#include "Logger.h"
#include "Map.h"

static unsigned char BITFLAG_IS_IMPASSABLE = 128;

Map::Map(int id, std::string note, int x, int y, int width, int height,
         bool underwater, bool markable, bool teleportable, bool escapable, bool useResurrection,
         bool usePainwand, bool enabledDeathPenalty, bool takePets,
         bool recallPets, bool usableItem, bool usableSkill) : db::def::Map(id, note, x, y, width, height, underwater,
                                                                            markable, teleportable, escapable,
                                                                            useResurrection, usePainwand,
                                                                            enabledDeathPenalty, takePets, recallPets,
                                                                            usableItem, usableSkill),
                                                               aoi_(id, x, y, width, height),
                                                               tiles_(width * height) {
}

Map::~Map() {
  tiles_.clear();
}

// 加载瓦片地图数据
bool Map::initialize() {
  // AOI初始化
  aoi_.initialize();

  // 加载地图数据
  std::ifstream ifs((boost::format("%1%/%2%.txt") % Config::MAP_DIR % id_).str().c_str());
  if (!ifs)
  {
    LOG_ERROR << "Map::initialize open failed [" << id_ << ".txt]";
    return false;
  }

  int y = 0;
  for (std::string line; std::getline(ifs, line);)
  {
    if (line.front() == '#' || line.empty())
      continue;

    std::vector<std::string> tiles;
    boost::split(tiles, line, boost::is_any_of(","));
    if (static_cast<int>(tiles.size()) != width_) {
      LOG_ERROR << "Map::initialize the " << y << " line of " << id_ << ".txt is incorrect";
      return false;
    } else {
      for (std::size_t i = 0; i < tiles.size(); i++) {
        tiles_[i + y * width_] = std::atoi(tiles[i].c_str());
      }
    }
    ++y;
  }
  if (y != height_) {
    LOG_ERROR << "Map::initialize the number of " << id_ << ".txt lines is incorrect";
    return false;
  }

  if (!ifs.eof())
  {
    LOG_ERROR << "Map::initialize " << ifs.rdstate() << " [" << id_ << ".txt]";
    return false;
  }

  return true;
}

bool Map::isInMap(const Point &pt) {
  return isInMap(pt.x(), pt.y());
}

bool Map::isInMap(int x, int y) {
  return (x_ <= x && x <= (x_ + width_) && y_ <= y && y <= (y_ + height_));
}

bool Map::isPassable(const Point &pt) {
  return isPassable(pt.x(), pt.y());
}

bool Map::isPassable(int x, int y) {
  return isPassable(x, y - 1, NORTH) || isPassable(x + 1, y, WEST) || isPassable(x, y + 1, SOUTH) ||
         isPassable(x - 1, y, EAST);
}

bool Map::isPassable(const Point &pt, int t) {
  return isPassable(pt.x(), pt.y(), t);
}

bool Map::isPassable(int x, int y, int t) {
  // 现在的位置
  unsigned char currtile = tile(x, y);

  // 移动后的位置
  unsigned char nextTile;
  switch (t) {
    case SOUTH:
      nextTile = tile(x, y - 1);
      break;
    case SOUTH_EAST:
      nextTile = tile(x + 1, y - 1);
      break;
    case EAST:
      nextTile = tile(x + 1, y);
      break;
    case NORTH_EAST:
      nextTile = tile(x + 1, y + 1);
      break;
    case NORTH:
      nextTile = tile(x, y + 1);
      break;
    case NORTH_WEST:
      nextTile = tile(x - 1, y + 1);
      break;
    case WEST:
      nextTile = tile(x - 1, y);
      break;
    case SOUTH_WEST:
      nextTile = tile(x - 1, y - 1);
      break;
    default:
      return false;
  }

  if ((nextTile & BITFLAG_IS_IMPASSABLE) == BITFLAG_IS_IMPASSABLE)
    return false;

  switch (t) {
    case SOUTH: {
      return (currtile & 0x02) == 0x02;
    }
    case SOUTH_EAST: {
      unsigned char southTile = tile(x, y - 1);
      unsigned char eastTile = tile(x + 1, y);
      return (southTile & 0x01) == 0x01 || (eastTile & 0x01) == 0x01;
    }
    case EAST: {
      return (currtile & 0x01) == 0x01;
    }
    case NORTH_EAST: {
      unsigned char northTile = tile(x, y + 1);
      return (northTile & 0x01) == 0x01;
    }
    case NORTH: {
      return (nextTile & 0x02) == 0x02;
    }
    case NORTH_WEST: {
      return (nextTile & 0x01) == 0x01 || (nextTile & 0x02) == 0x02;
    }
    case WEST: {
      return (nextTile & 0x01) == 0x01;
    }
    case SOUTH_WEST: {
      unsigned char westTile = tile(x - 1, y);
      return (westTile & 0x02) == 0x02;
    }
  }

  return false;
}

void Map::setPassable(const Point &pt, bool isPassable) {
  setPassable(pt.x(), pt.y(), isPassable);
}

void Map::setPassable(int x, int y, bool isPassable) {
  if (isPassable) {
    tile(x, y, tile(x, y) & (~BITFLAG_IS_IMPASSABLE));
  } else {
    tile(x, y, tile(x, y) | (~BITFLAG_IS_IMPASSABLE));
  }
}

bool Map::isSafetyZone(const Point &pt) {
  return isSafetyZone(pt.x(), pt.y());
}

bool Map::isSafetyZone(int x, int y) {
  return (tile(x, y) & (~BITFLAG_IS_IMPASSABLE) & 0x30) == 0x10;
}

bool Map::isCombatZone(const Point &pt) {
  return isCombatZone(pt.x(), pt.y());
}

bool Map::isCombatZone(int x, int y) {
  return (tile(x, y) & (~BITFLAG_IS_IMPASSABLE) & 0x30) == 0x20;
}

bool Map::isNormalZone(const Point &pt) {
  return isNormalZone(pt.x(), pt.y());
}

bool Map::isNormalZone(int x, int y) {
  return (tile(x, y) & (~BITFLAG_IS_IMPASSABLE) & 0x30) == 0x00;
}

bool Map::isArrowPassable(const Point &pt) {
  return isArrowPassable(pt.x(), pt.y());
}

bool Map::isArrowPassable(int x, int y) {
  return (tile(x, y) & (~BITFLAG_IS_IMPASSABLE) & 0x0e) != 0x00;
}

bool Map::isArrowPassable(const Point &pt, int t) {
  return isArrowPassable(pt.x(), pt.y(), t);
}

bool Map::isArrowPassable(int x, int y, int t) {
// 现在的位置
  unsigned char currtile = tile(x, y);

  // 移动后的位置
  unsigned char nextTile;
  switch (t) {
    case SOUTH: {
      nextTile = tile(x, y - 1);
      if (isExistDoor(x, y - 1))
        return false;
      break;
    }
    case SOUTH_EAST: {
      nextTile = tile(x + 1, y - 1);
      if (isExistDoor(x + 1, y - 1))
        return false;
      break;
    }
    case EAST: {
      nextTile = tile(x + 1, y);
      if (isExistDoor(x + 1, y))
        return false;
      break;
    }
    case NORTH_EAST: {
      nextTile = tile(x + 1, y + 1);
      if (isExistDoor(x + 1, y + 1))
        return false;
      break;
    }
    case NORTH: {
      nextTile = tile(x, y + 1);
      if (isExistDoor(x, y + 1))
        return false;
      break;
    }
    case NORTH_WEST: {
      nextTile = tile(x - 1, y + 1);
      if (isExistDoor(x - 1, y + 1))
        return false;
      break;
    }
    case WEST: {
      nextTile = tile(x - 1, y);
      if (isExistDoor(x - 1, y))
        return false;
      break;
    }
    case SOUTH_WEST: {
      nextTile = tile(x - 1, y - 1);
      if (isExistDoor(x - 1, y - 1))
        return false;
      break;
    }
    default:
      return false;
  }

  switch (t) {
    case SOUTH: {
      return (currtile & 0x08) == 0x08;
    }
    case SOUTH_EAST: {
      unsigned char southTile = tile(x, y - 1);
      unsigned char eastTile = tile(x + 1, y);
      return (southTile & 0x04) == 0x04 || (eastTile & 0x08) == 0x08;
    }
    case EAST: {
      return (currtile & 0x04) == 0x04;
    }
    case NORTH_EAST: {
      unsigned char northTile = tile(x, y + 1);
      return (northTile & 0x04) == 0x04;
    }
    case NORTH: {
      return (nextTile & 0x08) == 0x08;
    }
    case NORTH_WEST: {
      return (nextTile & 0x04) == 0x04 || (nextTile & 0x08) == 0x08;
    }
    case WEST: {
      return (nextTile & 0x04) == 0x04;
    }
    case SOUTH_WEST: {
      unsigned char westTile = tile(x - 1, y);
      return (westTile & 0x08) == 0x08;
    }
  }

  return false;
}

bool Map::isFishingZone(int x, int y) {
  return (tile(x, y) & (~BITFLAG_IS_IMPASSABLE)) == 0x10;
}

bool Map::isExistDoor(int x, int y) {
  return false;
}

unsigned char Map::tile(int x, int y) {
  if (!isInMap(x, y))
    return 0;

  return tiles_[(x - x_) + (y - y_) * width_];
}

void Map::tile(int x, int y, unsigned char value) {
  if (!isInMap(x, y))
    return;

  tiles_[(x - x_) + (y - y_) * width_] = value;
}