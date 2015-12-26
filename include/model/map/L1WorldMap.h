#ifndef L1WorldMap_H
#define L1WorldMap_H

#include <map>
#include <memory>
#include <Poco/Mutex.h>
#include <Poco/Logger.h>

using Poco::Mutex;
using Poco::Logger;

class L1Map;
class L1WorldMap
{
public:
  L1WorldMap();
  virtual ~L1WorldMap() {};

  static std::shared_ptr<L1WorldMap> getInstance();
  void addMap(std::shared_ptr<L1Map> map);
  std::shared_ptr<L1Map> geL1Map(int mapId);
  void removeMap(int mapId);

protected:
  std::map<int, std::shared_ptr<L1Map>> _maps;
  static Mutex _mapMtx;
  static std::shared_ptr<L1WorldMap> _instance;
  static Logger& _log;
};

#endif // L1WorldMap_H
