//
// Created by 范炜东 on 2019/5/10.
//

#include <boost/algorithm/clamp.hpp>
#include "Common.h"
#include "Character.h"

namespace db {
namespace def {

int Character::access_level() {
  return access_level_;
}

void Character::access_level(int v) {
  access_level_ = v;
}

int Character::max_hp() {
  return max_hp_;
}

void Character::max_hp(int v) {
  max_hp_ = boost::algorithm::clamp(v, 0, 32767);
}

int Character::cur_hp() {
  return cur_hp_;
}

void Character::cur_hp(int v) {
  cur_hp_ = boost::algorithm::clamp(v, 1, max_hp_);
}

int Character::max_mp() {
  return max_mp_;
}

void Character::max_mp(int v) {
  max_mp_ = boost::algorithm::clamp(v, 0, 32767);
}

int Character::cur_mp() {
  return cur_mp_;
}

void Character::cur_mp(int v) {
  cur_mp_ = boost::algorithm::clamp(v, 1, max_mp_);
}

int Character::ac() {
  return ac_;
}

void Character::ac(int v) {
  ac_ = boost::algorithm::clamp(v, -128, 127);
}

int Character::str() {
  return str_;
}

void Character::str(int v) {
  str_ = boost::algorithm::clamp(v, 1, 127);
}

int Character::dex() {
  return dex_;
}

void Character::dex(int v) {
  dex_ = boost::algorithm::clamp(v, 1, 127);
}

int Character::con() {
  return con_;
}

void Character::con(int v) {
  con_ = boost::algorithm::clamp(v, 1, 127);
}

int Character::men() {
  return men_;
}

void Character::men(int v) {
  men_ = boost::algorithm::clamp(v, 1, 127);
}

int Character::wis() {
  return wis_;
}

void Character::wis(int v) {
  wis_ = boost::algorithm::clamp(v, 1, 127);
}

int Character::cha() {
  return cha_;
}

void Character::cha(int v) {
  cha_ = boost::algorithm::clamp(v, 1, 127);
}

int Character::face() {
  return face_;
}

void Character::face(int v) {
  face_ = boost::algorithm::clamp(v, SOUTH, SOUTH_WEST);
}

int Character::justice() {
  return justice_;
}

void Character::justice(int v) {
  justice_ = boost::algorithm::clamp(v, -32768, 32767);
}

}
}