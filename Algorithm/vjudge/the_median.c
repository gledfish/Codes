/*
  name:the_median.c
  author:gled fish
  time:2021/11/3
*/
#include <stdio.h>
int main()
{
	int n, i, j, temp;
	scanf("%d", &n);
	int nums[10000];
	for(i=0;i<n;i++)
	{
		scanf("%d", &nums[i]);
	}
	for(i=0;i<n-1;i++)
		{
			for(j=0;j<n-1-i;j++)
			{
				if(nums[j]>nums[j+1])
			{
				temp = nums[j];
        nums[j] = nums[j+1];
        nums[j+1] = temp;
			}
			}
		}
		printf("%d", nums[(n-1)/2]);
		return 0;
}