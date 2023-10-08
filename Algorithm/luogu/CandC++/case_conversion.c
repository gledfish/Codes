/*
  name:case_conversion.c
  author:gled fish
  time:2021/10/31
*/
#include <stdio.h>
int main()
{
	char ch;
	scanf("%c", &ch);
	ch = ch - 32;
	printf("%c", ch);
	return 0;
}
