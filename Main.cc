#include <iostream>
#include "Config.h"
#include "Logger.h"
#include "GameServer.h"

int main(int argc, char *argv[]) {
  try {
    Config::load(argc, argv);
    LOG_INFO << "Loading configuration is finished";
    GameServer srv;
    srv.run();
  }
  catch (std::exception &e) {
    std::cerr << e.what();
  }
  return 0;
}