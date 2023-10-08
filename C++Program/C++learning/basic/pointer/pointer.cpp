#include <bits/stdc++.h>

using namespace std;

int main(void){
    int num;
    // 声明指针
    int * p;
    // 在C++中，int *是一种复合类型，是指向int的指针。
    p = &num;
    *p  = 10;
    cout << *p << endl;
    cout << num << endl;

    long* fellow; //声明指针变量，但并没有分配地址
    // *fellow = 22l; 没有地址不能存储值

    int * pointer = new int;// 使用 new 在声明时自动分配内存
    /*
    常规变量的值存储在栈中
    而 new 从被称为 heap 或者 自由存储区的内存区域里分配内存*/
    delete pointer; //释放内存，但并不会删除指针变量

    // 使用 new 创建动态结构
    int * psome = new int[10];
    // inflatable * ps = new inflatable;
    delete [] psome;
    // 不能修改数组名的值，但指针是变量，可以修改
    // 使用动态数组

    // 将指针变量加1后，增加的量等于它指向的类型的字节数

    cout << *(p++)<< endl; //?
    return 0;
}