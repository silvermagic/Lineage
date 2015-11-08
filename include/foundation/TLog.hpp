#ifndef TLOG_HPP_INCLUDED_
#define TLOG_HPP_INCLUDED_

#include <boost/log/core.hpp>
#include <boost/log/expressions.hpp>
#include <boost/log/attributes.hpp>
#include <boost/log/sinks.hpp>
#include <boost/log/utility/setup/file.hpp>
#include <boost/log/sources/severity_channel_logger.hpp>
#include <boost/log/sources/record_ostream.hpp>
#include <boost/format.hpp>

namespace Lineage{ namespace log {

namespace logging = boost::log;
namespace src = boost::log::sources;
namespace expr = boost::log::expressions;
namespace sinks = boost::log::sinks;
namespace attrs = boost::log::attributes;
namespace keywords = boost::log::keywords;

enum severity_level
{
  normal,
  notification,
  warning,
  error,
  critical
};

template< typename CharT, typename TraitsT >
inline std::basic_ostream< CharT, TraitsT >& operator<<(std::basic_ostream< CharT, TraitsT >& strm, severity_level lvl)
{
  static const char* const str[] =
  {
    "normal",
    "notification",
    "warning",
    "error",
    "critical"
  };

  if(static_cast< std::size_t >(lvl) < (sizeof(str) / sizeof(*str)))
    strm << str[lvl];
  else
    strm << static_cast< int >(lvl);

  return strm;
}

class TLog
{
public:
  TLog(std::string module, severity_level lvl = severity_level::normal) : _log(keywords::channel = module)
  {
    _sink = logging::add_file_log(keywords::file_name = module + "_%Y-%m-%d.%N.log",
                                  keywords::rotation_size = 10 * 1024 * 1024,
                                  keywords::time_based_rotation = sinks::file::rotation_at_time_point(0, 0, 0),
                                  keywords::filter = (expr::attr<std::string>("Channel") == module) && (expr::attr<severity_level>("Severity") >= lvl),
                                  keywords::format = "[%TimeStamp%]: %Message%");
  }
  virtual ~TLog()
  {
    logging::core::get()->remove_sink(_sink);
  }

  template<typename ...Args>
  void log(severity_level lvl, std::string value, Args... args)
  {
    boost::format fmt(value);
    BOOST_LOG_SEV(_log, lvl) << logNest(fmt, args...).str();
  }
  template<typename T>
  void log(severity_level lvl, T value)
  {
    BOOST_LOG_SEV(_log, lvl) << value;
  }

protected:
  template<typename T, typename ...Args>
  boost::format& logNest(boost::format& fmt, T value, Args... args)
  {
    fmt = fmt % value;
    return logNest(fmt, args...);
  }
  template<typename T, typename ...Args>
  boost::format& logNest(boost::format& fmt, T value)
  {
    return (fmt = fmt % value);
  }
private:
  src::severity_channel_logger<severity_level, std::string> _log;
  decltype(logging::add_file_log(keywords::file_name)) _sink;
};

class TLoggerMgr
{
};

}}
#endif
