#include <stdio.h>
int max_out;
int max(int a,int b);
int main()
{
    int m, t, s;
	scanf("%d %d %d", &m, &t, &s);
	if(t==0)
		{
		printf("%d\n", t);
		}
	else if(t!=0)
	{
		int out = m-(s/t);
		if(s%t==0)
		{
			max(out,0);
		    printf("%d\n", max_out);
		}
	    if(s%t!=0)
	   {
	   	 	max(out-1,0);
		    printf("%d\n", max_out);
	   }
	}
	return 0;
}
int max(int a, int b)
	{
    if(a>b)
		max_out = a;
	if(a<=b)
		max_out = b;
	return 0;
	}
