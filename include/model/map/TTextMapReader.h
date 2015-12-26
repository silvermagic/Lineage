#ifndef TTEXTMAPREADER_H
#define TTEXTMAPREADER_H

#include <list>
#include <boost/multi_array.hpp>
#include <Poco/Logger.h>
#include "model/map/TMapReader.h"

using Poco::Logger;

class TTextMapReader : public TMapReader
{
public:
	TTextMapReader();
	virtual ~TTextMapReader();

  std::list<int>&& listMapIds();
  std::map<int, std::shared_ptr<TMap>>&& read();
	std::shared_ptr<TMap> read(int id);
	boost::multi_array<unsigned char,2> read(int mapId, int xSize, int ySize);

protected:
  static Logger& _log;
};

#endif // TTEXTMAPREADER_H
