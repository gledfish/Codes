#include <bits/stdc++.h>

using namespace std;

// int func(int n)
//     return n;函数必须要块标识
int value_transfer(int num){
    num = 5;
    return 0;
}
int pointer_transfer(int& num){
    num = 5;
    return 0;
}
int pointer_copy_transfer(int *pointer_transfer){
    *pointer_transfer = 10;
    return 0;
}
int func4(const int &n){
    // n = 6;can't be changed
    return 0;
}

int main(void){
    int n = 2;
    // value_transfer(n);
    // cout << n << endl;//2, not changed
    pointer_transfer(n);
    cout << n << endl;//5,changed
    pointer_copy_transfer(&n);
    cout << n << endl;//10,changed
    return 0;
}