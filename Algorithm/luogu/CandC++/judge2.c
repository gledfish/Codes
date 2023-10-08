#include <stdio.h>

void judge2(int * max, int * c);
int main(void){
	int num1 = 10;
	int num3 = 6;
	judge2(&num1, &num3);
	printf("%d/%d", *&num3, *&num1);
}
void judge2(int * max, int * c)
{
	for(int i = 2; i <= * c; i++)
	{
		if(* max / i == 0 && * c / i ==0)
		{
			* max = * max / i;
			* c = * c / i;
		}
	}
}