#include <bits/stdc++.h>
#define OK 0
using  namespace std;

int calculator(int a, int b){
    return a + b;
}
double calculator(double a, double b){
    return a + b;
}
int main(void) {
    cout << calculator(2,3) << endl;
    cout << calculator(2.5, 3.0);
    return OK;
}