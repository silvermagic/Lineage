cmake_minimum_required(VERSION 2.6)
project(Lineage "CXX")

set(LINEAGE_VERSION_MAJOR 1)
set(LINEAGE_VERSION_MINOR 0)

set(CMAKE_INSTALL_PREFIX "/usr/local/")
SET(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set(CMAKE_CXX_FLAGS "-Wall -std=c++0x ${CMAKE_CXX_FLAGS}")

SET(Boost_NO_BOOST_CMAKE ON)
SET(Boost_USE_STATIC_LIBS OFF)
SET(Boost_USE_MULTITHREADED ON)
SET(Boost_USE_STAITC_RUNTIME OFF)
FIND_PACKAGE(Boost REQUIRED COMPONENTS system program_options random date_time thread filesystem log log_setup)
IF (Boost_FOUND)
    INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS})
    MESSAGE(STATUS "boost libraries ${Boost_LIBRARIES}")
ENDIF(Boost_FOUND)

INCLUDE_DIRECTORIES("${CMAKE_CURRENT_SOURCE_DIR}/include")
LINK_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/libs)

file(GLOB CONFIGURE_SRC "${CMAKE_CURRENT_SOURCE_DIR}/src/configure/*.cpp")
file(GLOB TYPES_SRC "${CMAKE_CURRENT_SOURCE_DIR}/src/types/*.cpp")
file(GLOB_RECURSE MODEL_SRC "${CMAKE_CURRENT_SOURCE_DIR}/src/model/*.cpp")

ADD_LIBRARY(configure ${CONFIGURE_SRC})
ADD_LIBRARY(types ${TYPES_SRC})
ADD_LIBRARY(model ${MODEL_SRC})
TARGET_LINK_lIBRARIES(model types)

MESSAGE("cflag for Lineage: ${CMAKE_CXX_FLAGS}")
add_executable(Lineage "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp")
target_link_Libraries(Lineage model configure ${Boost_LIBRARIES})

install(TARGETS Lineage RUNTIME DESTINATION bin)

#
# 用法例 cmake28 ..
#
