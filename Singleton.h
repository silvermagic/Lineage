//
// Created by 范炜东 on 2019/5/13.
//

#ifndef PROJECT_SINGLETON_H
#define PROJECT_SINGLETON_H

#include <mutex>
#include <memory>
#include <boost/core/noncopyable.hpp>

template<class T>
class Singleton : boost::noncopyable {
public:
  static T& instance() {
    static std::once_flag flag;
    std::call_once(flag, [&]() {
      instance_ = std::make_shared<T>();
      if (!instance_->initialize())
        instance_ = nullptr;
    });

    assert(instance_);
    return *instance_;
  }

protected:
  static std::shared_ptr<T> instance_;
};

template<class T>
std::shared_ptr<T> Singleton<T>::instance_ = nullptr;

#endif //PROJECT_SINGLETON_H
