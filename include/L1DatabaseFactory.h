#ifndef L1DATABASEFACTORY_H
#define L1DATABASEFACTORY_H

#include <memory>
#include "Poco/Data/Session.h"
#include "Poco/Data/SessionPool.h"
#include "Poco/Logger.h"
#include "Poco/Data/MySQL/Connector.h"

using Poco::Logger;
using Poco::Data::Session;
using Poco::Data::SessionPool;
using namespace Poco::Data;

class AutoRegister
{
public:
  AutoRegister() { MySQL::Connector::registerConnector(); }
  virtual ~AutoRegister() { MySQL::Connector::unregisterConnector(); }
};

class L1DatabaseFactory
{
public:
	L1DatabaseFactory();
	virtual ~L1DatabaseFactory();

  static L1DatabaseFactory& getInstance();
  Session getConnection();//获取数据库连接
	void shutdown();//关闭数据库连接池
protected:
	SessionPool _pool;
	static std::shared_ptr<L1DatabaseFactory> _instance;
	static Logger& _log;
	static AutoRegister _auto;
};

#endif // L1DATABASEFACTORY_H
