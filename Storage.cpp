//
// Created by 范炜东 on 2018/12/10.
//

#include "Storage.h"

namespace Lineage {

SINGLETON_INIT(Storage);

Storage::Storage(LayeredConfiguration &cfg) : pool_(cfg.getString("DB.type"),
                                                    Poco::format(
                                                            "host=%s;port=%d;user=%s;password=%s;db=%s;compress=true;auto-reconnect=true",
                                                            cfg.getString("DB.host", "0.0.0.0"),
                                                            cfg.getInt("DB.port", 3306),
                                                            cfg.getString("DB.user", "root"),
                                                            cfg.getString("DB.password", "root"),
                                                            cfg.getString("DB.name", "l1jdb")),
                                                    cfg.getInt("DB.min", 1),
                                                    cfg.getInt("DB.max", 32),
                                                    cfg.getInt("DB.idle", 60)) {
}

Storage::~Storage() {
    pool_.shutdown();
}

Session Storage::get() {
    return pool_.get();
}

}