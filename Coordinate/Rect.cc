//
// Created by 范炜东 on 2019/6/24.
//

#include <boost/format.hpp>
#include "Rect.h"

Rect::Rect(int x, int y, int width, int height) : x_(x), y_(y), width_(width), height_(height) {
}

Rect::Rect(const Point &pt, int width, int height) : x_(pt.x()), y_(pt.y()), width_(width), height_(height) {
}

bool Rect::contains(int x, int y) {
  int dist = x - x_;
  if (dist < 0 || dist > width_)
    return false;
  dist = y - y_;
  if (dist < 0 || dist > height_)
    return false;
  return true;
}

bool Rect::contains(const Point &pt) {
  return contains(pt.x(), pt.y());
}

bool Rect::operator==(const Rect& r) {
  return (x_ == r.x() && y_ == r.y() && width_ == r.width() && height_ == r.height());
}

bool Rect::operator!=(const Rect& r) {
  return (x_ != r.x() || y_ != r.y() || width_ != r.width() || height_ != r.height());
}

std::string Rect::toString() {
  return std::move((boost::format("(%1, %2, %3, %4)") % x_ % y_ % width_ % height_).str());
}

int Rect::x() const {
  return x_;
}

void Rect::x(int value) {
  x_ = value;
}

int Rect::y() const {
  return y_;
}

void Rect::y(int value) {
  y_ = value;
}

int Rect::width() const {
  return width_;
}

void Rect::width(int value) {
  width_ = value;
}

int Rect::height() const {
  return height_;
}

void Rect::height(int value) {
  height_ = value;
}