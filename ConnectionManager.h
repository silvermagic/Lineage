//
// Created by 范炜东 on 2019/4/25.
//

#ifndef PROJECT_CONNECTIONMANAGER_H
#define PROJECT_CONNECTIONMANAGER_H

#include <set>
#include <memory>

class Connection;
class ConnectionManager {
public:
  ConnectionManager();

  // 添加连接并启动
  void start(std::shared_ptr<Connection> c);

  // 停止连接
  void stop(std::shared_ptr<Connection> c);

  // 停止所有连接
  void stop();

protected:
  std::set<std::shared_ptr<Connection>> connections_;
};

#endif //PROJECT_CONNECTIONMANAGER_H
