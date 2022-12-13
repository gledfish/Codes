#include <bits/stdc++.h>

using namespace std;

int main(void){
    char str[] = {'h', 'e', 'l', 'l', 'o'};
    cout << str[4] << endl;
    string str2 = "hello";//dymatic memory
    cout << str2 << endl;
    str2[0] = 'o';//changed
    cout << str2 << endl;
    // str2 = str;
    // cout << str2;
    
    char str3[10] = {};
    cout << str2.c_str();
    return 0;
}