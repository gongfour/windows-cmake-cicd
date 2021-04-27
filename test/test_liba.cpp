#include <iostream>
#include <libA/liba.h>

int main(int argc, char const *argv[])
{
    print("This is the first message.");

    const Node message{"This is the second message."};
    print(message);
    return 0;
}
