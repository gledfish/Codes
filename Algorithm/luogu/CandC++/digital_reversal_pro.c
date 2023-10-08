/*
  name:digital_reversal.c
  author:gled fish
  time:2021/10/31
*/
#include <stdio.h>
int main()
{
	int a, b, c, d;
	char ch;
	scanf("%d%d%d%c%d", &a, &b, &c, &ch, &d);
	printf("%d%c%d%d%d",d,ch,c,b,a);
	return 0;
}
