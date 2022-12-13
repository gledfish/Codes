#include <stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	if(n>=3&&n<=10^5)
	{
		int out = n * (n-1) * (n-2) * (n-3)/24;
	    printf("%d\n", out);
	}
	return 0;
}