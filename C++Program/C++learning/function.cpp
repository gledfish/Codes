#include <bits/stdc++.h>

using namespace std;

// int func(int n)
//     return n;函数必须要块标识
int func(int n){
    n = 5;
    return 0;
}
int func2(int &n){
    n = 5;
    return 0;
}
int func3(int *n){
    *n = 10;
    return 0;
}
int func4(const int &n){
    // n = 6;can't be changed
    return 0;
}

int main(void){
    int n = 2;
    func(n);
    cout << n << endl;//2, not changed
    func2(n);
    cout << n << endl;//5,changed
    func3(&n);
    cout << n << endl;//10,changed
    return 0;
}