#include <libA/liba.h>
#include <iostream>

void foo()
{
    std::cout << __func__ << std::endl;
}

void print(const std::string &message)
{
    std::cout << __func__ << " : " << message << std::endl;
}

void print(const Node &node)
{
    std::cout << __func__ << node.name << std::endl;
}