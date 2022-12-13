#include <stdio.h>
int main(void)
{	
	int nums[3];
	char ch[3];
	int i, j, temp;
	for(i=0;i<3;i++)
	{
		scanf("%d", &nums[i]);
	}
	getchar();
	for ( i = 0; i < 3; i++)
	{
		scanf("%c", &ch[i]);
	}
	getchar();
	for(i=0;i<2;i++)
	{
		for(j=0;j<3-i-1;j++)
		{
			if(nums[j]>nums[j+1])//从小到大排序
			{
				temp = nums[j];
				nums[j] = nums[j+1];
				nums[j+1] = temp;
			}

		}
	}
	if(ch[0]=='A')
	{
		if(ch[1]=='B')
			printf("%d %d %d", nums[0], nums[1], nums[2]);
		if(ch[1]=='C')
			printf("%d %d %d", nums[0], nums[2], nums[1]);
	}
	if(ch[0]=='B')
	{
		if(ch[1]=='A')
			printf("%d %d %d", nums[1], nums[0], nums[2]);
		if(ch[1]=='C')
			printf("%d %d %d", nums[1], nums[2], nums[0]);
	}
	if(ch[0]=='C')
	{
		if(ch[1]=='A')
			printf("%d %d %d", nums[2], nums[0], nums[1]);
		if(ch[1]=='B')
			printf("%d %d %d", nums[2], nums[1], nums[0]);
	}
	return 0;
}