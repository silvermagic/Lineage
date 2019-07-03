//
// Created by 范炜东 on 2019/6/18.
//

#ifndef PROJECT_THREADPOOLMANAGER_H
#define PROJECT_THREADPOOLMANAGER_H

#include <boost/asio.hpp>
#include "Singleton.h"

class ThreadPoolManager : public Singleton<ThreadPoolManager>, public boost::asio::thread_pool {
public:
  ThreadPoolManager();

  // 初始化
  bool initialize();
};

#endif //PROJECT_THREADPOOLMANAGER_H
