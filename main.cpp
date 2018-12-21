//
// Created by 范炜东 on 2018/11/19.
//

#include <iostream>

#include "GameServer.h"

namespace Lineage {

using Poco::Exception;

int main(int argc, char **argv) {
    try {
        GameServer app;
        return app.run(argc, argv);
    }
    catch (Exception &exc) {
        std::cerr << exc.displayText() << std::endl;
        return Application::EXIT_SOFTWARE;
    }
}

}