#ifndef TextMapReader_H
#define TextMapReader_H

#include <list>
#include <boost/multi_array.hpp>
#include <Poco/Logger.h>
#include "model/map/MapReader.h"

using Poco::Logger;

class TextMapReader : public MapReader
{
public:
	TextMapReader();
	virtual ~TextMapReader();

  std::list<int> lisL1MapIds();
  std::map<int, std::shared_ptr<L1Map>> read();
	std::shared_ptr<L1Map> read(int id);
	boost::multi_array<unsigned char,2> read(int mapId, int xSize, int ySize);

protected:
  static Logger& _log;
};

#endif // TextMapReader_H
