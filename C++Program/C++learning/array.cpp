#include <bits/stdc++.h>
#define OK 0
using namespace std;

int func(int args[], int leng){
    for(int i = 0; i < leng; i++){
        cout << args[i] << endl;
    }
    return OK;
}
int func2(int args[][5], int leng)
{
    for (int i = 0; i < leng; i++)
    {
        cout << args[i][0] << endl;
        cout << args[i][1] << endl;
        cout << args[i][2] << endl;
        cout << args[i][3] << endl;
        cout << args[i][4] << endl;
    }
    return OK;
}
int main(){
    int array[5] = {};
    array[0] = 5;
    cout << array[0] << endl;//5
    cout << array[1] << endl;//0
    
    int array2[3][5] = {};
    array2[0][0] = 4;
    array2[2][3] = 4;
    // func(array, 5);
    func2(array2, 3);