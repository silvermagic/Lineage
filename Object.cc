//
// Created by 范炜东 on 2019/6/17.
//

#include "Common.h"
#include "Object.h"

Object::Object(int id) : id_(id), destroy_(false), range_(0) {
}

void Object::onNotify(std::shared_ptr<Object> obj, bool enter) {
}

void Object::onWatch(std::shared_ptr<Object> obj, bool enter) {
}

int Object::id() {
  return id_;
}

int Object::type() {
  return OBJECT_TYPE_UNKNOWN;
}

bool Object::destroy() {
  return destroy_;
}

int Object::range() {
  return range_;
}

std::string Object::toString() {
  return "";
}