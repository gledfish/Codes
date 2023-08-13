#include <stdio.h>
int main()
{
	int num;
	scanf("%d", &num);
	int time_1 = 5 * num;
	int time_2 = 11 + 3 * num;
	if(time_1<time_2)
		printf("Local");
	else
		printf("Luogu");
	return 0;
}