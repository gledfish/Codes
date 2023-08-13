/*
  name:nums_sum.c
  author:gled fish
  time:2021/10/24
*/
#include <stdio.h>
int main()
{-
	int nums[9] = {-2,1,-3,4,-1,2,1,-5,4};
	int i,j;
	int n = 9,max = nums[0],sum = 0;
	for(i=0;i<n;i++) 
	{
		sum = nums[i];
		for(j=i+1;j<n;j++)
		{
			sum = sum  + nums[j];
			if(sum>max)
				max = sum;
		}
	}
	printf("%d",max);
	return 0;
}
