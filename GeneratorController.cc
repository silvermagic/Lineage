//
// Created by 范炜东 on 2019/5/15.
//

#include "Common.h"
#include "Logger.h"
#include "ConnectionPoolManager.h"
#include "GeneratorController.h"

GeneratorController::GeneratorController() {
}

GeneratorController::~GeneratorController() {
}

bool GeneratorController::initialize() {
  try {
    session sql(ConnectionPoolManager::instance());
    int id;
    sql << "select max(id)+1 from "
           "(select id from goods "
           "union all select id from character_teleport "
           "union all select id from character_warehouse "
           "union all select id from characters "
           "union all select id from clan "
           "union all select id from clan_warehouse "
           "union all select id from pets) t", use(id);
    id_ = id;
  } catch (std::exception &e) {
    LOG_ERROR << e.what();
    return false;
  }

  return true;
}

int GeneratorController::next() {
  return id_++;
}
