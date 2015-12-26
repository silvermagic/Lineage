#ifndef TMAPREADER_H
#define TMAPREADER_H

#include <map>
#include <memory>

class TMap;

class TMapReader
{
public:
	TMapReader() {};
	virtual ~TMapReader() {};

	virtual std::map<int, std::shared_ptr<TMap>>&& read() = 0;
	virtual std::shared_ptr<TMap> read(int id) = 0;
};

#endif // TMAPREADER_H
