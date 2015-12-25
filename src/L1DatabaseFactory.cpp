#include "Poco/Data/SessionFactory.h"
#include "Poco/Data/DataException.h"
#include "L1DatabaseFactory.h"
#include "configure/TConfig.h"

using Poco::Data::ConnectionFailedException;
using Poco::Data::DataException;

Logger& L1DatabaseFactory::_log = Logger::get("lineage.L1DatabaseFactory");
std::shared_ptr<L1DatabaseFactory> L1DatabaseFactory::_instance;
AutoRegister _cr;

extern TConfig CONFIG;

L1DatabaseFactory::L1DatabaseFactory() : _pool(MySQL::Connector::KEY, CONFIG.DB_CONN,10,32,10)
{
	try
	{
		_pool.get().close();
	}
	catch (ConnectionFailedException &e)
	{
		_log.error("数据库连接失败.");
		// 重新抛出异常
		e.rethrow();
	}
	catch (DataException &e)
	{
		_log.error("数据库连接失败.");
		throw ConnectionFailedException("无法初始化DB连接: ", e);
	}
}

L1DatabaseFactory::~L1DatabaseFactory()
{
  shutdown();
}

L1DatabaseFactory& L1DatabaseFactory::getInstance()
{
	if (!_instance)
	{
		_instance = std::make_shared<L1DatabaseFactory>();
	}
	return *_instance;
}

Session L1DatabaseFactory::getConnection()
{
  return _pool.get();
}

void L1DatabaseFactory::shutdown()
{
	try
	{
		_pool.shutdown();
	}
	catch (DataException &e)
	{
		_log.information(e.what());
	}
}
