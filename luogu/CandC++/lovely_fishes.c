/*
  name:lovely_fishes.c
  author:2021/10/31
  time:2021/10/31
*/
#include <stdio.h>
int main()
{
	int n, i, j;
	scanf("%d", &n);
	int num[100];
	int nums[100]= {0};
	for(i=0;i<n;i++)
	{
		scanf("%d", &num[i]);
	}
	for(i=n-1;i>=1;i--)
	{
		for(j=i-1;j=0;j--)
		{
			if(num[i]>num[j])
			nums[i]=nums[i] + 1;
		}
	}
	for(i=1;i<n;i++)
	{
		if(i==0)
		printf("0");
		else
		printf("%d",nums[i]);
	}
	return 0;
 } 
