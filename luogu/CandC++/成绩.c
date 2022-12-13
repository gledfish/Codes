#include <stdio.h>
int main()
{
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);
	float score = A * 0.2 + B * 0.3 + C * 0.5;
	int out = (int)score;
	printf("%d\n", out);
	return 0;
}