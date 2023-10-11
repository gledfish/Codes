/*
  name:altnames.c
  author:gled fish
  time:2021/10/20
*/
#include <stdio.h>
int main(void)
{
	int me32;
	me32 = 45933945;
	printf("First,assume int32_t is int:");
	printf("me32 = %d\n",me32);
	printf("Next,let's not make any assumptions.\n");
	printf("Instead,use a \"macro\"from inttypes.h:");
	printf("me32 = %PRID32\n",me32);
	return 0;
}
