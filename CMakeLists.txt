cmake_minimum_required(VERSION 3.13.0)
project(windows-cmake-cicd)
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})