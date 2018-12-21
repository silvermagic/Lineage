//
// Created by 范炜东 on 2018/12/13.
//

#ifndef LINEAGE_POINT_H
#define LINEAGE_POINT_H

namespace Lineage {

/**
      朝向
*/
enum Towards
{
    SOUTH = 0,
    SOUTH_EAST = 1,
    EAST = 2,
    NORTH_EAST = 3,
    NORTH = 4,
    NORTH_WEST = 5,
    WEST = 6,
    SOUTH_WEST = 7
};

const int TOWARDS_TABLE_X[] = { 0, 1, 1, 1, 0, -1, -1, -1 };
const int TOWARDS_TABLE_Y[] = { -1, -1, 0, 1, 1, 1, 0, -1 };

class Point
{
public:
    Point();
    Point(int xPos, int yPos);
    virtual ~Point();

    // 向后移动
    void backward(Towards t);

    // 向前移动
    void forward(Towards t);

    // 计算到目标的直线距离
    double getLineDistance(const Point& pt);

    // 计算沿着X轴和Y轴移动到目标的距离
    int getTileDistance(const Point& pt);

    // 计算到目标的平行距离, 即移动到与目标X轴或Y轴水平时两点的直线距离中的较大值
    int getTileLineDistance(const Point& pt);

    // 计算坐标的哈希值
    int hashCode();

    /*
      如果返回指定坐标在屏幕中是否可见。玩家坐标为(0, 0)，则可见范围的坐标为
      左上(-2, 15)右上(15, -2)左下(-15, 2)右下(2, -15)，被聊天文本框遮挡的不可见的部分也
      包含在屏幕中。
    */
    bool isInScreen(const Point& pt);

    // 等值运算符重载
    bool operator==(const Point& pt);
    bool operator!=(const Point& pt);

    // 返回坐标的字符串表示
    virtual std::string toString();

    template<class Archive>
    void serialize(Archive & ar, const unsigned int version) {
        ar & x;
        ar & y;
    }

public:
    int x;
    int y;
};

}

#endif //LINEAGE_POINT_H
