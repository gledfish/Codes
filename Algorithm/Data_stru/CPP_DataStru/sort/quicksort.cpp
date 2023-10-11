#include <bits/stdc++.h>

using namespace std;


void swap(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}
void quick_sort_recursive(int arr[], int start, int end)
{
    if (start >= end)
        return;
    int mid = arr[end];//选择枢轴量
    int left = start, right = end - 1;//交换数据的范围
    while (left < right)
    {
        while (arr[left] < mid && left < right)
            left++;
        while (arr[right] >= mid && left < right)
            right--;
        swap(&arr[left], &arr[right]);
    }
    // if (arr[left] > arr[end])
    //     swap(&arr[left], &arr[end]);
    // else
    //     left++;
    //进行第二轮
    // if (left)
    // {
    //     quick_sort_recursive(arr, start, left - 1);
    // }
    // quick_sort_recursive(arr, left + 1, end);
}


void printArray(int* src, int length){
    for(int i = 0; i < length; i++){
        cout << src[i] <<endl;
    }
}
int main(void){
    int length = 9;
    
    int nums[length] = {5, 9, 1, 9, 5, 3, 7, 6, 1}; 
    quick_sort_recursive(nums, 0, 8);
    printArray(nums, length);
    return 0;
}