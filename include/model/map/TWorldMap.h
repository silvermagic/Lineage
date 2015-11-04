#ifndef TWORLDMAP_H
#define TWORLDMAP_H

#include <map>
#include <memory>

class TMap;

class TWorldMap
{
public:
  TWorldMap();
  virtual ~TWorldMap();
protected:
private:
  std::map<int, std::shared_ptr<TMap>> m_maps;
};

#endif // TWORLDMAP_H
