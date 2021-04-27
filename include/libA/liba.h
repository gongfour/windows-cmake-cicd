#pragma once

#include <string>
#include <liba_export.h>

struct Node
{
    std::string name;
};

LIBA_EXPORT void foo();
LIBA_EXPORT void print(const std::string &message);
LIBA_EXPORT void print(const Node &node);