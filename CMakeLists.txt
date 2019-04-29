### cmake的最低版本
cmake_minimum_required(VERSION 2.8)
### 工程名
project(Lineage)

### 设置编译参数
#set(CMAKE_CXX_FLAGS  "-Wall -std=c++11 -DBOOST_LOG_DYN_LINK -DBOOST_ASIO_ENABLE_HANDLER_TRACKING")
set(CMAKE_CXX_FLAGS  "-Wall -std=c++11 -DBOOST_LOG_DYN_LINK")
set(CMAKE_CXX_FLAGS_DEBUG  "-g")

### 设置头文件路径
include_directories(${CMAKE_SOURCE_DIR} /usr/include/soci)

### 可执行文件名、源文件列表
add_subdirectory("ClientPackets")
add_subdirectory("ServerPackets")
add_subdirectory("Tables")
add_subdirectory("Templates")
file(GLOB SRC "${CMAKE_CURRENT_SOURCE_DIR}/*.cc")
add_executable(l1j ${SRC} $<TARGET_OBJECTS:ClientPackets> $<TARGET_OBJECTS:ServerPackets> $<TARGET_OBJECTS:Tables> $<TARGET_OBJECTS:Templates>)

### 设置链接库
target_link_libraries(l1j -lboost_system -lboost_program_options -lboost_log_setup -lboost_log -lboost_thread -lpthread -lsoci_core -lsoci_empty -lsoci_postgresql)