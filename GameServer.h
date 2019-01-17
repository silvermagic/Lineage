//
// Created by 范炜东 on 2018/11/19.
//

#ifndef LINEAGE_GAMESERVER_H
#define LINEAGE_GAMESERVER_H

#include <Poco/Util/ServerApplication.h>
#include <Poco/Util/Option.h>
#include <Poco/Util/OptionSet.h>

namespace Lineage {

using Poco::Util::ServerApplication;
using Poco::Util::Application;
using Poco::Util::Option;
using Poco::Util::OptionSet;

class GameServer : public ServerApplication {
public:
    GameServer();

    ~GameServer();

protected:
    void initialize(Application &self) override;

    void uninitialize() override;

    void defineOptions(OptionSet &options) override;

    void handleOption(const std::string &name, const std::string &value) override;

    int main(const std::vector<std::string> &args) override;

    void displayHelp();

private:
    bool help_;
};

}

#endif //LINEAGE_GAMESERVER_H
