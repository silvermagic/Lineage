//
// Created by 范炜东 on 2019/6/19.
//

#include "Logger.h"
#include "ConnectionPoolManager.h"
#include "Templates/Map.h"
#include "Map.h"

namespace db {
namespace oper {

std::vector<std::shared_ptr<def::Map>> Map::query() {
  LOG_DEBUG << "Map::query";
  session sql(ConnectionPoolManager::instance());
  std::vector<std::shared_ptr<def::Map>> maps;
  rowset <row> rs = (sql.prepare << "select id, note, x, y, width, height, underwater, markable, teleportable, escapable, resurrection, painwand, penalty, take_pets, recall_pets, usable_item, usable_skill from maps");
  for (rowset<row>::const_iterator iter = rs.begin(); iter != rs.end(); ++iter) {
    const row &r = *iter;
    int id;
    std::string note;
    int x, y, width, height, underwater, markable, teleportable, escapable, resurrection, painwand, penalty, take_pets, recall_pets, usable_item, usable_skill;
    r >> id >> note >> x >> y >> width >> height >> underwater >> markable >> teleportable >> escapable >> resurrection
      >> painwand >> penalty >> take_pets >> recall_pets >> usable_item >> usable_skill;
    maps.push_back(std::make_shared<def::Map>(id, note, x, y, width, height, underwater != 0, markable != 0, teleportable != 0, escapable != 0,
            resurrection != 0, painwand != 0, penalty != 0, take_pets != 0, recall_pets != 0, usable_item != 0, usable_skill != 0));
  }
  LOG_DEBUG << "Map::query -> " << maps.size();
  return maps;
}

}
}