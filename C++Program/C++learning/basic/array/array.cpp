#include <bits/stdc++.h>
#define OK 1
#define FALSE 0
using namespace std;

int func(int args[], int length){
    /*
    输出数组中所有值，返回一个bool类型值
    args:整数数组
    leng:数组长度*/
    for(int i = 0; i < length; i++){
        cout << args[i] << endl;
    }
    return OK;
}
int func2(int args[][5], int length)
{
    /*
    输出二维数组每个值，返回一个bool值
    args：二维整数数组
    leng：数组长度*/
    for (int i = 0; i < length; i++)
    {
        cout << args[i][0] << " ";
        cout << args[i][1] << " ";
        cout << args[i][2] << " ";
        cout << args[i][3] << " ";
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
    return 0;
}