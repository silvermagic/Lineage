//
// Created by 范炜东 on 2019/4/25.
//

#include "Connection.h"
#include "Logger.h"
#include "ConnectionManager.h"

ConnectionManager::ConnectionManager() : connections_() {

}

void ConnectionManager::start(std::shared_ptr<Connection> c) {
  // TODO: 双开检测
  auto r = connections_.insert(c);
  if (r.second) {
    LOG_DEBUG << c->address() << " connect";
    c->start();
  }
}

void ConnectionManager::stop(std::shared_ptr<Connection> c) {
  if (connections_.erase(c) > 0) {
    LOG_DEBUG << c->address() << " disconnect";
    c->stop();
  }
}

void ConnectionManager::stop() {
  for (auto c: connections_)
    c->stop();
  connections_.clear();
}