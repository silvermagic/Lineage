#ifndef TWORLDMAP_H
#define TWORLDMAP_H

#include <map>
#include <memory>
#include "Poco/Mutex.h"
#include "Poco/Logger.h"

using Poco::Mutex;
using Poco::Logger;

class TMap;
class TWorldMap
{
public:
  TWorldMap();
  virtual ~TWorldMap() {};

  static std::shared_ptr<TWorldMap> getInstance();
  void addMap(std::shared_ptr<TMap> map);
  std::shared_ptr<TMap> getMap(int mapId);
  void removeMap(int mapId);

protected:
  std::map<int, std::shared_ptr<TMap>> _maps;
  static std::shared_ptr<TWorldMap> _instance;
  static Mutex _mapMtx;
  static Logger& _log;
};

#endif // TWORLDMAP_H
