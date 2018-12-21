//
// Created by 范炜东 on 2018/12/10.
//

#ifndef LINEAGE_STORAGE_H
#define LINEAGE_STORAGE_H

#include <Poco/Data/RecordSet.h>
#include <Poco/Data/SessionPool.h>
#include <Poco/Util/LayeredConfiguration.h>
#include "Singleton.h"

namespace Lineage {

using Poco::Data::Session;
using Poco::Data::SessionPool;
using Poco::Data::Statement;
using Poco::Data::RecordSet;
using Poco::Data::Keywords::into;
using Poco::Data::Keywords::use;
using Poco::Data::Keywords::now;
using Poco::Util::LayeredConfiguration;

class Storage : public Singleton<Storage> {
public:
    Storage(LayeredConfiguration& cfg);

    ~Storage();

    bool initialize();

    // 获取数据库操作句柄
    Session get();

protected:
    SessionPool pool_;
};

}

#endif //LINEAGE_STORAGE_H
