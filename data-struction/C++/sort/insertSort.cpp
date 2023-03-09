//直接插入排序
#include <bits/stdc++.h>
#define MAX_SIZE 100
using namespace std;

//打印数组
void printArray(int* nums, int length){
    for(int i = 0; i < length; i++){
        printf("%d ", nums[i]);
    }
    printf("\n");
}

void insertSort(int* nums, int length){
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
        printArray(nums, length);
        if (i == 2)
            break;
    }
}
int main(void){
    int nums[MAX_SIZE];
    int length = 0;
    // printf("请输入数组的长度："); 
    scanf("%d", &length);
    // printf("请输入数组元素：");
    if(length < 4 || length > MAX_SIZE)
        return 0;
    for(int i = 0; i < length; i++){
        scanf("%d", &nums[i]);
    }
    insertSort(nums, length);
    return 0;
}