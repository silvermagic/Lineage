//
// Created by 范炜东 on 2019/5/13.
//

#ifndef PROJECT_CONNECTIONPOOLMANAGER_H
#define PROJECT_CONNECTIONPOOLMANAGER_H

#include <iostream>
#include <string>
#include <exception>
#include <ctime>
#include <soci.h>
#include <postgresql/soci-postgresql.h>
#include "Singleton.h"

using namespace soci;

class ConnectionPoolManager : public Singleton<ConnectionPoolManager>, public connection_pool {
public:
  ConnectionPoolManager();
  ~ConnectionPoolManager();

  // 初始化
  bool initialize();
};

#endif //PROJECT_CONNECTIONPOOLMANAGER_H
