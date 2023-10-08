/*
  name:numbers sum.c
  author:gled fish
  time:2021/10/23
*/
#include <stdio.h>
int main(void)
{
	int nums[4] = {2,7,11,15};
	int target = 9,n=4;
	int i,j,sum;
	for(i=0;i<n-1;i++)
	{
		for(j=i+1;j<n;j++)
		{
			sum = nums[i] + nums[j];
		    if(sum == target)
		    printf("[%d,%d]",i,j);
		    break;
		}	
	}
	return 0;
}
