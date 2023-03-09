#include <bits/stdc++.h>

using namespace std;

int bubbleSort(int* nums, int length){
    int count = 0;
    for(int i = 0; i < length; i++){
        for(int j = 0; j <= length - i - 1;j++){
            if(nums[j] < nums[j - 1]){
                int temp;
                temp = nums[j];
                nums[j] = nums[j - 1];
                nums[j - 1] = temp;
                count++;
            }
        }
    }
    return count;
}
int main(void){
    int length = 0;
    scanf("%d",&length);
    int nums[length];
    for(int i=0; i<length; i++){
        scanf("%d",&nums[i]);
    }
    printf("%d\n", bubbleSort(nums, length));

    return 0;
}