//
// Created by kyle on 2020/12/16.
//

#ifndef KGE_SINGLETON_H
#define KGE_SINGLETON_H

#include <memory>
#include <boost/core/noncopyable.hpp>

namespace kge {

template <typename T>
class Singleton : boost::noncopyable {
public:
  Singleton(void) {
    instance_ = static_cast< T* >(this);
  }

  static T& instance(void) { assert(instance_);  return (*instance_); }
protected:
  static std::shared_ptr<T> instance_;
};

#define KGE_SINGLETON_INIT(TYPE) TYPE* Singleton<TYPE>::instance_ = nullptr;

}

#endif //KGE_SINGLETON_H
