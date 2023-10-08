#include <stdio.h>
int main()
{
	int i, j, num;
	int nums_1[7];
	int nums_2[7];
	int nums_sum[7];
	for(i=0;i<7;i++)
	{
		scanf("%d", &nums_1[i]);
		scanf("%d", &nums_2[i]);
		nums_sum[i] = nums_1[i] + nums_2[i];
	}
	int max = 0;
	for(j=0;j<7;j++)
	{
		if(nums_sum[j]>max)
		{
			max = nums_sum[j];
		    num = j + 1;
		}
	}
	if(max<=8)
		printf("0");
	if(max>8)
		printf("%d\n", num);
	return 0;
}