#include <stdio.h>
int main()
{
	float t;
	int n;
	scanf("%.1f %d", &t, &n);
	int num = 2 * n;
	float average = t/(float)n;
	printf("%.3f %d", average, num);
	return 0;
}