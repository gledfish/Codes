#include <iostream>
#include <string>

using namespace std;

int main(){
    // 没有以空字符结尾的规定
    // 采用动态内存分配
    string str1;
    string str2 = "string";// string str2("string")
    return 0;

    // 可以将一个string对象赋给另一个string对象（深拷贝）
    str1 = str2;

    // 可以更快捷地进行字符串的拼接
    string str3 = str1 + str2;

}