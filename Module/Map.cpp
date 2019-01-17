//
// Created by 范炜东 on 2018/12/13.
//

#include "Map.h"

namespace Lineage {

static const char BITFLAG_IS_IMPASSABLE = 128;

bool Map::isInMap(int x, int y) {
    return (leftTop.x <= x && x <= rightBottom.x && leftTop.y <= y && y <= rightBottom.y);
}

bool Map::isPassable(const Point &pt) {
    return isPassable(pt.x, pt.y);
}

bool Map::isPassable(int x, int y) {
    return isPassable(x, y - 1, NORTH) || isPassable(x + 1, y, WEST) || isPassable(x, y + 1, SOUTH) ||
           isPassable(x - 1, y, EAST);
}

bool Map::isPassable(const Point &pt, Towards t) {
    return isPassable(pt.x, pt.y, t);
}

bool Map::isPassable(int x, int y, Towards t) {
    // 现在的位置
    char currtile = tile(x, y);

    // 移动后的位置
    int nextTile;
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
            char southTile = tile(x, y - 1);
            char eastTile = tile(x + 1, y);
            return (southTile & 0x01) == 0x01 || (eastTile & 0x01) == 0x01;
        }
        case EAST: {
            return (currtile & 0x01) == 0x01;
        }
        case NORTH_EAST: {
            char northTile = tile(x, y + 1);
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
            char westTile = tile(x - 1, y);
            return (westTile & 0x02) == 0x02;
        }
    }

    return false;
}

void Map::setPassable(const Point &pt, bool isPassable) {
    setPassable(pt.x, pt.y, isPassable);
}

void Map::setPassable(int x, int y, bool isPassable) {
    if (isPassable) {
        tile(x, y, tile(x, y) & (~BITFLAG_IS_IMPASSABLE));
    } else {
        tile(x, y, tile(x, y) | (~BITFLAG_IS_IMPASSABLE));
    }
}

bool Map::isSafetyZone(const Point &pt) {
    return isSafetyZone(pt.x, pt.y);
}

bool Map::isSafetyZone(int x, int y) {
    return (tile(x, y) & 0x30) == 0x10;
}

bool Map::isCombatZone(const Point &pt) {
    return isCombatZone(pt.x, pt.y);
}

bool Map::isCombatZone(int x, int y) {
    return (tile(x, y) & 0x30) == 0x20;
}

bool Map::isNormalZone(const Point &pt) {
    return isNormalZone(pt.x, pt.y);
}

bool Map::isNormalZone(int x, int y) {
    return (tile(x, y) & 0x30) == 0x00;
}

bool Map::isArrowPassable(const Point &pt) {
    return isArrowPassable(pt.x, pt.y);
}

bool Map::isArrowPassable(int x, int y) {
    return (tile(x, y) & 0x0e) != 0x00;
}

bool Map::isArrowPassable(const Point &pt, Towards t) {
    return isArrowPassable(pt.x, pt.y, t);
}

bool Map::isArrowPassable(int x, int y, Towards t) {
    // 现在的位置
    char currtile = tile(x, y);

    // 移动后的位置
    char nextTile;
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
            char southTile = tile(x, y - 1);
            char eastTile = tile(x + 1, y);
            return (southTile & 0x04) == 0x04 || (eastTile & 0x08) == 0x08;
        }
        case EAST: {
            return (currtile & 0x04) == 0x04;
        }
        case NORTH_EAST: {
            char northTile = tile(x, y + 1);
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
            char westTile = tile(x - 1, y);
            return (westTile & 0x08) == 0x08;
        }
    }

    return false;
}

bool Map::isFishingZone(int x, int y) {
    return true;
}

bool Map::isExistDoor(int x, int y) {
    return true;
}

char Map::tile(int x, int y) {
    if (!isInMap(x, y))
        return 0;

    int row = y - leftTop.y;
    int col = x - leftTop.x;
    return tiles[row * width + col];
}

void Map::tile(int x, int y, char value) {
    if (!isInMap(x, y))
        return;

    int row = y - leftTop.y;
    int col = x - leftTop.x;
    tiles[row * width + col] = value;
}

}