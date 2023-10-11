/*
  name:typesize.c
  author:gled fish
  time:2021/10/20
*/
#include <stdio.h>
int main(void)
{
	printf("type int has a size of %zd bytes.\n",sizeof(int) );
	printf("type char has a size of %zd bytes.\n",sizeof(char));
	printf("type long has a size of %zd bytes.\n",sizeof(long) );
	printf("type long long has a size of %zd bytes.\n",sizeof(long long) );
	printf("type double has a size of %zd bytes.\n",sizeof(double));
	printf("type long double has a size of %zd bytes.\n",sizeof(long double) );
	return 0;
}
