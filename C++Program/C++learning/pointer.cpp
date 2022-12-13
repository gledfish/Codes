#include <bits/stdc++.h>

using namespace std;

int main(void){
    int num;
    int * p;
    p = &num;
    *p  = 10;
    cout << *p << endl;
    cout << num << endl;

    cout << *(p++)<< endl;
    return 0;
}