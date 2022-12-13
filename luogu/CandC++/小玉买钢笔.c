#include <stdio.h>
int main()
{
	int num_1, num_2;
	scanf("%d %d", &num_1, &num_2);
	int num = num_1 * 10 + num_2;
	int nums = num/19;
	printf("%d", nums);
	return 0;
}