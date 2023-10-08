#include <iostream>

using namespace std;

// 结构体声明
struct inflatable
{
    char name[20];
    float volume;
    double price;
};

int main()
{

    // 结构体初始化
    inflatable guest = {
        "gled fish",
        1.88,
        29.99};
    inflatable guest{ //C++ 11
        "gled fish",
        1.88,
        29.99}; 

    // 结构体数组初始化
    inflatable guests[2] = {
        {"name1", 0.5, 21.99},
        {"name2", 2000, 565.99}
    };
    // 也可以为结构体的成员指定存储的字节数
    struct torgle_register {
        unsigned int SN:4; // 4 个字节
    };
    return 0;
}