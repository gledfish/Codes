#include <stdio.h>
int main(void)
{
	int num;
	int i = 0;
	scanf("%d", &num);
	if(num%2==0)
		i = i + 1;
	if(num>4&&num<=12)
		i = i + 1;
	if(i == 2)
		printf("1 ");
	else
		printf("0 ");
	if(i==2||i==1)
		printf("1 ");
	else
		printf("0 ");
	if(i==1)
		printf("1 ");
	else
		printf("0 ");
	if(i==0)
		printf("1");
	else
		printf("0");
	return 0;
}
