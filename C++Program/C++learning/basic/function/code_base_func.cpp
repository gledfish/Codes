#include <iostream>
/*
函数式编程
1. 量化目标
2. 拆解目标为不同的函数
3. 实现各个函数*/
// 例：输入两个数，计算两个数的和，分为两个函数，1.获得两个数，2. 求和
using namespace std;

// 获得计算的数据
int* getNum(int count);
// 计算和
int calculate(int* nums, int count);


int main(){
    int count = 3;
    int* nums = getNum(count);
    int sum = calculate(nums, count);
    cout << count << "个数的和为" << sum <<endl;
    return 0;
}

int calculate(int* nums, int count){
    int sum = 0;
    for(int i = 0; i < count; i++){
        sum += nums[i];
    }
    return sum;
}

int* getNum(int count){
    /*获得两个数，并返回这两个数组成的数组
    count ： 数的个数*/
    
    int* num_arr = new int[count];
    for(int i = 0; i < count; i++){
        cout << "请输入一个整数：\n";
        cin >> num_arr[i];
    }
    return num_arr;
}