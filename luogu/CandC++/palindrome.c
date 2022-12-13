#include <stdio.h>
#include <string.h>
int huiwen(char s[])
{
	int i = 0,j = strlen(s)-1;
	while(i<j&&s[i]==s[j])
	{
		i++;
		j--;
	}
	return i>=j;
}