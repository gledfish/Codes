/*
  name:nums_sum_pro.c
  author:gled fish
  time:2021/10/24
*/
#include <stdio.h>
int main()
{
	int nums[10];
	int m,i,j;
	int n = 10,max = nums[0],sum = 0;
	for(m=0;m<n;m++)
	{
		scanf("%d",&nums[m]);
	}
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

	
