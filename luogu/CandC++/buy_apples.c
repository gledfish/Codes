/*
  name:buy_apples.c
  author:gled fish
  time:2021/10/31
*/
#include <stdio.h>
int main()
{
	int num, people;
	scanf("%d %d", &num, &people);
	int sum = num * people;
	printf("%d\n", sum);
	return 0;
}