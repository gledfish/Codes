//希尔排序 shellsort
#include <bits/stdc++.h>
#define MAXSIZE 100

using namespace std;

void printArray(int *nums, int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%d ", nums[i]);
    }
    printf("\n");
}

void insertSort(int *nums, int length)
{
    int insertNum;
    for (int i = 0; i < length - 1; i++)
    {
        // 遍历所有元素
        if (nums[i + 1] < nums[i])
        {
            // 找到需要插入的元素
            insertNum = nums[i + 1];
            for (int j = 0; j < i + 1; j++)
            {
                // 从左往右寻找插入位置
                if (insertNum <= nums[0])
                {
                    for (int k = i + 1; k > 0; k--)
                    {
                        // 从j + 1 开始向右移动一位，同时
                        nums[k] = nums[k - 1];
                    }
                    nums[0] = insertNum;
                    break;
                }
                if (insertNum >= nums[j] && insertNum <= nums[j + 1])
                {
                    // 找到插入位置为 j + 1
                    for (int k = i + 1; k > j + 1; k--)
                    {
                        // 从j + 1 开始向右移动一位，同时
                        nums[k] = nums[k - 1];
                    }
                    nums[j + 1] = insertNum;
                    break;
                    // 移动完成后插入j + 1,一趟完成
                }
            }
        }
        // printArray(nums, length);
    }
}

// 希尔排序
void shellSort(int* nums, int length)
{

    int d = length; // gap的值
    while (true)
    {
        d = d / 2; // 每次都将gap的值减半

        for (int x = 0; x < d; x++)
        { // 对于gap所分的每一个组
            for (int i = x + d; i < length; i = i + d)
            { // 进行插入排序
                int temp = nums[i];
                int j;
                for (j = i - d; j >= 0 && nums[j] > temp; j = j - d) {
                    nums[j + d] = nums[j];
                }
                nums[j + d] = temp;
            }
        }
        printArray(nums, length);
        break;
        // if (d == 1)
        // { // gap==1，跳出循环

        //     break;
        // }
    }
}


int main(void) {
    int nums[MAXSIZE];
    int length;
    // printf("请输入数组长度：");
    scanf("%d",&length);
    // printf("请输入数据：");
    for(int i = 0; i < length; i++){
        scanf("%d",&nums[i]);
    }
    shellSort(nums,length);
    return 0;
}