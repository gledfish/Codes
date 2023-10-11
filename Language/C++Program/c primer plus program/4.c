/*
  name:skip2.c
  author:gled fish
  time:2021/10/28
*/
#include <stdio.h>
int main(void)
{
	int n;
	printf("Please enter three integers:\n");
	scanf("%*d %*d %d",&n);
	printf("The last integar was %d\n",n);
	return 0;
}
