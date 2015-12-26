#include <iostream>
#include "utils/TPerformanceTimer.h"
#include "model/map/TMap.h"
#include "model/map/TWorldMap.h"

Mutex TWorldMap::_mapMtx;
std::shared_ptr<TWorldMap> TWorldMap::_instance;
Logger& TWorldMap::_log = Poco::Logger::get("lineage.TWorldMap");

TWorldMap::TWorldMap()
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

std::shared_ptr<TWorldMap> TWorldMap::getInstance()
{
	Mutex::ScopedLock lock(_mapMtx);
	if (!_instance)
	{
		_instance = std::make_shared<TWorldMap>();
	}
	return _instance;
}

void TWorldMap::addMap(std::shared_ptr<TMap> map)
{
	Mutex::ScopedLock lock(_mapMtx);
	_maps[map->getId()] = map;
}

std::shared_ptr<TMap> TWorldMap::getMap(int mapId)
{
	std::shared_ptr<TMap> map = _maps[mapId];
	if (map == NULL)   // 没有地图信息
	{
		map = TMap::newNull(); // 返回一个没有任何信息的Map。
	}
	return map;
}

void TWorldMap::removeMap(int mapId)
{
	Mutex::ScopedLock lock(_mapMtx);
	_maps.erase(mapId);
}
