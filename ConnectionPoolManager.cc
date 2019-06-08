//
// Created by 范炜东 on 2019/5/13.
//

#include <boost/format.hpp>
#include "Config.h"
#include "Logger.h"
#include "ConnectionPoolManager.h"

ConnectionPoolManager::ConnectionPoolManager() : connection_pool(Config::DB_POOL_SIZE) {
}

ConnectionPoolManager::~ConnectionPoolManager() {
}

bool ConnectionPoolManager::initialize()
{
  try {
    std::string connection_url = (boost::format("dbname=%s user=%s password=%s") % Config::DB_NAME % Config::DB_USER % Config::DB_PASSWORD).str();
    for (size_t i = 0; i < Config::DB_POOL_SIZE; ++i)
    {
      session & sql = at(i);
      sql.open(postgresql, connection_url.c_str());
    }
  } catch (std::exception &e) {
    LOG_ERROR << e.what();
    return false;
  }

  return true;
}