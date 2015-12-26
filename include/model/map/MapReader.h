#ifndef MapReader_H
#define MapReader_H

#include <map>
#include <memory>

class L1Map;

class MapReader
{
public:
	MapReader() {};
	virtual ~MapReader() {};

	virtual std::map<int, std::shared_ptr<L1Map>> read() = 0;
	virtual std::shared_ptr<L1Map> read(int id) = 0;
};

#endif // MapReader_H
