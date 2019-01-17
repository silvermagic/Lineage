//
// Created by 范炜东 on 2018/12/7.
//

#ifndef LINEAGE_SINGLETON_H
#define LINEAGE_SINGLETON_H

#include <Poco/Bugcheck.h>

namespace Lineage {

template <typename T>
class Singleton
{
protected:
    static T* singleton_;

public:
    Singleton(void)
    {
        singleton_ = static_cast<T*>(this);
    }

    ~Singleton(void) { poco_assert(singleton_);  singleton_ = 0; }

    static T& getSingleton(void) { poco_assert(singleton_);  return (*singleton_); }
};

#define SINGLETON_INIT(TYPE) template<> TYPE* Singleton<TYPE>::singleton_ = 0;

}


#endif //LINEAGE_SINGLETON_H
