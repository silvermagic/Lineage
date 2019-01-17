//
// Created by 范炜东 on 2018/12/13.
//

#include <cmath>
#include <algorithm>
#include <Poco/Format.h>
#include "Point.h"

namespace Lineage {

Point::Point() : x(0), y(0) {
}

Point::Point(int xPos, int yPos) : x(xPos), y(yPos) {
}

Point::~Point() {
}

void Point::backward(Towards t) {
    x -= TOWARDS_TABLE_X[t];
    y -= TOWARDS_TABLE_Y[t];
}

void Point::forward(Towards t) {
    x += TOWARDS_TABLE_X[t];
    y += TOWARDS_TABLE_Y[t];
}

double Point::getLineDistance(const Point &pt) {
    long diffX = pt.x - x;
    long diffY = pt.y - y;
    return std::sqrt(diffX * diffX + diffY * diffY);
}

int32_t Point::getTileDistance(const Point &pt) {
    int diffX = pt.x - x;
    int diffY = pt.y - y;
    return std::max(std::abs(diffX), std::abs(diffY));
}

int32_t Point::getTileLineDistance(const Point &pt) {
    int diffX = pt.x - x;
    int diffY = pt.y - y;
    return std::abs(diffX) + std::abs(diffY);
}

int32_t Point::hashCode() {
    return 7 * x + y;
}

bool Point::isInScreen(const Point &pt) {
    int dist = getTileDistance(pt);
    // 首先使用平行距离进行判断，过滤掉那些太远影响近似计算的点
    if (dist > 17) {
        return false;
    } else if (dist <= 13) // 简化判断
    {
        return true;
    } else {
        // 判断两点间的直线距离是否在范围内的近似算法，首先以当前坐标为原点建立坐标系，
        // 然后计算沿着X轴和Y轴移动到目标的距离
        int diffX = pt.x - (x - 15);
        int diffY = pt.y - (y - 15);
        int dist = std::abs(diffX) + std::abs(diffY);
        if (17 <= dist && dist <= 43)
            return true;
    }

    return false;
}

bool Point::operator==(const Point &pt) {
    return (pt.x == x && pt.y == y);
}

bool Point::operator!=(const Point &pt) {
    return (pt.x != x || pt.y != y);
}

std::string Point::toString() {
    return Poco::format("(%d, %d)", x, y);
}

}