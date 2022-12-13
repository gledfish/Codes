#include <stdio.h>
int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	if(a+b<=c||a+c<=b||b+c<=a)
		printf("Not triangle\n");
	if(a+b>c&&a+c>b&&c+b>a)
	{
		int A = a^2, B = b^2, C = c^2;
		if(A==B+C||C==B+A||B==C+A)
			printf("Right triangle\n");
		if(A<B+C||C<B+A||B<C+A)
			printf("Acute triangle\n");
		if(A>B+C||C>B+A||B>C+A)
			printf("Obtuse triangle\n");
		if(a==b||a==c||b==c)
			printf("Isosceles triangle\n");
		if(a==b&&b==c)
			printf("Equilateral triangle\n");
	}
	return 0;
}