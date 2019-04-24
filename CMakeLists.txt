### cmake的最低版本
cmake_minimum_required(VERSION 2.8)
### 工程名
project(Lineage)

### 设置编译参数
set(CMAKE_CXX_FLAGS  "-Wall -std=c++11 -DBOOST_LOG_DYN_LINK")
set(CMAKE_CXX_FLAGS_DEBUG  "-g")

### 可执行文件名、源文件列表
file(GLOB SRC "${CMAKE_CURRENT_SOURCE_DIR}/*.cc")
add_executable(l1j ${SRC})

### 设置链接库
target_link_libraries(l1j -lboost_system -lboost_program_options -lboost_log_setup -lboost_log -lboost_thread -lpthread)