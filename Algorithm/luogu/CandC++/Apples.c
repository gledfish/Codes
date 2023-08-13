#include <stdio.h>
int main()
{
	int x;
	scanf("%d", &x);
	if(x==0||x==1)
		printf("Today, I ate %d apple.", x);
	if(x>1)
		printf("Today, I ate %d apples.", x);
	return 0;
}