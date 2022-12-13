#include <bits/stdc++.h>

using namespace std;

int main(void){
    int * foo;
    foo = new int;
    *foo = 4;
    // cout << *foo << endl;
    delete foo;

    int * foo2 = new int;
    foo2[0] = 4;
    cout << foo2[0] << endl;
    cout << *foo2 << endl;
    cout << foo2[1] << endl; //没有赋值。所以是随机值
    cout << foo2 << endl;//地址
    foo2[1] = 5;
    cout << foo2[1] << endl;//赋值后，为赋值的结果
    cout << foo2++ << endl;//指针右移，输出第二个元素的地址
    cout << foo2 <<endl;//此时foo2指针指向第二个元素
    cout << foo2[-1] << endl;//此时foo2指向的上一个元素为4；
    delete foo2;
    return 0;
}