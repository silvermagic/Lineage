//
// Created by 范炜东 on 2018/12/13.
//

#ifndef LINEAGE_WORLDMAP_H
#define LINEAGE_WORLDMAP_H

#include <map>
#include <memory>
#include <Poco/Runnable.h>
#include <Poco/Util/LayeredConfiguration.h>
#include "Module/Map.h"
#include "Singleton.h"

namespace Lineage {

using Poco::Runnable;
using Poco::Util::LayeredConfiguration;

// 地图数据读取线程
class MapReader : public Runnable {
public:
    MapReader(int rindex);

    void run() override;

protected:
    int rindex_;
};

class WorldMap : public Singleton<WorldMap> {
public:
    // 地图数据初始化
    bool initialize(LayeredConfiguration& cfg);

    // 获取地图信息
    Map& operator[](int id);

protected:
    // 生成缓存
    bool buildCache();

    // 加载缓存
    bool loadCache();

    // 加载数据库
    bool loadDB();

protected:
    friend class MapReader;

protected:
    std::map<int, Map> maps_; // 游戏地图信息
};

}

#endif //LINEAGE_WORLDMAP_H
