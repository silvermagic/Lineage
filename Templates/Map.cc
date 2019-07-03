//
// Created by 范炜东 on 2019/6/19.
//

#include "Map.h"

namespace db {
namespace def {

Map::Map(int id, std::string note, int x, int y, int width, int height,
         bool underwater, bool markable, bool teleportable, bool escapable, bool useResurrection,
         bool usePainwand, bool enabledDeathPenalty, bool takePets,
         bool recallPets, bool usableItem, bool usableSkill) :
        id_(id),
        note_(note),
        x_(x),
        y_(y),
        width_(width),
        height_(height),
        is_underwater_(underwater),
        is_markable_(markable),
        is_teleportable_(teleportable),
        is_escapable_(escapable),
        is_use_resurrection_(useResurrection),
        is_use_painwand_(usePainwand),
        is_enabled_death_penalty_(enabledDeathPenalty),
        is_take_pets_(takePets),
        is_recall_pets_(recallPets),
        is_usable_item_(usableItem),
        is_usable_skill_(usableSkill) {
}

int Map::id() {
  return id_;
}

std::string Map::note() {
  return note_;
}

int Map::x() {
  return x_;
}

int Map::y() {
  return y_;
}

int Map::width() {
  return width_;
}

int Map::height() {
  return height_;
}

bool Map::isUnderwater() {
  return is_underwater_;
}

bool Map::isMarkable() {
  return is_markable_;
}

bool Map::isTeleportable() {
  return is_teleportable_;
}

bool Map::isEscapable() {
  return is_escapable_;
}

bool Map::isUseResurrection() {
  return is_use_resurrection_;
}

bool Map::isUsePainwand() {
  return is_use_painwand_;
}

bool Map::isEnabledDeathPenalty() {
  return is_enabled_death_penalty_;
}

bool Map::isTakePets() {
  return is_take_pets_;
}

bool Map::isRecallPets() {
  return is_recall_pets_;
}

bool Map::isUsableItem() {
  return is_usable_item_;
}

bool Map::isUsableSkill() {
  return is_usable_skill_;
}

}
}