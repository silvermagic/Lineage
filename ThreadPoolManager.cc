//
// Created by 范炜东 on 2019/6/18.
//

#include <boost/asio.hpp>
#include "Config.h"
#include "ThreadPoolManager.h"

ThreadPoolManager::ThreadPoolManager() : boost::asio::thread_pool(Config::POOL_SIZE) {
}

bool ThreadPoolManager::initialize() {
  return true;
}