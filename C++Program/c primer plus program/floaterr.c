/*
  name:floaterr.c
  author:gled fish
  time:2021/10/20
*/
#include <stdio.h>
int main()
{
	float a,b;
	b =2.0e20 + 1.0;
	a = b -2.0e20;
	printf("%f\n",a);
	return 0;
}
