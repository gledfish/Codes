#include <stdio.h>
int main()
{
	char s[]="Hello,world";
	int i = 0;
	while(s[i]!='\0')
	{
		++i;
	}
	printf("数组长度为%d",i);
	return 0;
}