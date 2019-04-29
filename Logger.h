//
// Created by 范炜东 on 2019/4/24.
//

#ifndef PROJECT_LOGGER_H
#define PROJECT_LOGGER_H

#include <boost/log/trivial.hpp>
#include <boost/log/sources/global_logger_storage.hpp>

#define LOG(severity) BOOST_LOG_SEV(boost::log::trivial::logger::get(), boost::log::trivial::severity)
#define LOG_TRACE   LOG(trace)
#define LOG_DEBUG   LOG(debug)
#define LOG_INFO    LOG(info)
#define LOG_WARNING LOG(warning)
#define LOG_ERROR   LOG(error)
#define LOG_FATAL   LOG(fatal)

#endif //PROJECT_LOGGER_H
