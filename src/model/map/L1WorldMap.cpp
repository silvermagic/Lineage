#include <iostream>
#include "utils/TPerformanceTimer.h"
#include "model/map/L1Map.h"
#include "model/map/L1WorldMap.h"

Mutex L1WorldMap::_mapMtx;
std::shared_ptr<L1WorldMap> L1WorldMap::_instance;
Logger& L1WorldMap::_log = Poco::Logger::get("lineage.L1WorldMap");

L1WorldMap::L1WorldMap()
{
	TPerformanceTimer timer;
	std::cout << "╔》正在读取 Map..." << std::endl;

	try
	{
		//_maps = MapReader.getDefaultReader().read();
		if (_maps.empty())
		{
			throw std::runtime_error("地图档案读取失败...");
		}
	}
	/*catch (std::runtime_error &e)
	{
		std::cout << "提示: 地图档案缺失，请检查330_maps.zip是否尚未解压缩。" << std::endl;
		exit(0);
	}*/
	catch (std::exception &e)
	{
		// 没有回报
		_log.error(e.what());
		exit(0);
	}
	std::cout << "完成!\t\t耗时: " << timer.elapsedTimeMillis() << "\t毫秒" << std::endl;
}

std::shared_ptr<L1WorldMap> L1WorldMap::getInstance()
{
	Mutex::ScopedLock lock(_mapMtx);
	if (!_instance)
	{
		_instance = std::make_shared<L1WorldMap>();
	}
	return _instance;
}

void L1WorldMap::addMap(std::shared_ptr<L1Map> map)
{
	Mutex::ScopedLock lock(_mapMtx);
	_maps[map->getId()] = map;
}

std::shared_ptr<L1Map> L1WorldMap::geL1Map(int mapId)
{
	std::shared_ptr<L1Map> map = _maps[mapId];
	if (map == NULL)   // 没有地图信息
	{
		map = L1Map::newNull(); // 返回一个没有任何信息的Map。
	}
	return map;
}

void L1WorldMap::removeMap(int mapId)
{
	Mutex::ScopedLock lock(_mapMtx);
	_maps.erase(mapId);
}
