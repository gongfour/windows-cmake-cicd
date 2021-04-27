cmake_minimum_required(VERSION 3.13.0)
project(windows-cmake-cicd)

###########################################
# Setting
###########################################
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD 17)

## test
include(CTest)
enable_testing()

## export
include(GenerateExportHeader)

## SHARED_LIB
option(BUILD_SHARED_LIBS "build_shared_libs" ON)

###########################################
# Library
###########################################
set(SRCS source/liba.cpp)
add_library(liba ${SRCS})
target_include_directories(liba PUBLIC 
    ${CMAKE_BINARY_DIR}    
    include
)

generate_export_header(liba)

###########################################
# Tests
###########################################
add_subdirectory(test)