#include "TMapReader.h"
#include "model/map/TTextMapReader.h"
#include "configure/TConfig.h"

extern TConfig Config;

std::shared_ptr<TMapReader> getDefaultReader()
{
	/*if (Config.LOAD_V2_MAP_FILES)
	{
		return std::make_shared<V2MapReader>();
	}
	if (Config.CACHE_MAP_FILES)
	{
		return std::make_shared<CachedMapReader>();
	}*/
	return std::make_shared<TTextMapReader>();
}
