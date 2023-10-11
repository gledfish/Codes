/*
  name:fathm_ft.c(把2英尺转换成两英寸）
  author:gled fish
  time:2021/10/19
*/
#include <stdio.h> 
int main(void)
{
	int feet,fathoms;
	fathoms = 2;
	feet = 6 * fathoms;
	printf("There are %d feet in %d fathoms!\n",feet,fathoms);
	printf("Yes,I said %d feet!\n",6 * fathoms);
	return 0;
}
