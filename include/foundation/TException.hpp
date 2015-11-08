#ifndef TEXCEPTION_HPP_INCLUDED_
#define TEXCEPTION_HPP_INCLUDED_

#include <exception>
#include <boost/format.hpp>
#include "foundation/exceptTag.h"

namespace Lineage{ namespace execption {

class TExecption : public std::exception
{
public:
  TExecption() = delete;
  template<typename ... Args> TExecption(exceptTag tag, Args... args) throw()
  {
    boost::format fmt(exceptFormat[tag]);
    format(fmt, args...);
    _exception_message = fmt.str();
  }
  TExecption(std::string message)
  {
    _exception_message = message;
  }

  TExecption(const TExecption& ex) throw() : _exception_message(ex._exception_message) {}
  TExecption& operator= (const TExecption& ex) throw()
  {
    _exception_message = ex._exception_message;
    return *this;
  }

  virtual ~TExecption() throw() {}

  const char* what() const throw() {
    return _exception_message.c_str();
  }

protected:
  template<typename T> void format(boost::format &fmt, const T &t) throw()
  {
    fmt = fmt % t;
  }

  template<typename T, typename ... Args> void format(boost::format &fmt, const T &t, Args... args) throw()
  {
    fmt = fmt % t;
    format(fmt, args...);
  }

protected:
  std::string _exception_message;
};

}}
#endif
