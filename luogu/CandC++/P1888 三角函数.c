#include <stdio.h>
int judge1(int max, int b, int c);
void judge2(int * max, int * c);

const int NUM = 3;
int main(void)
{
	int num[NUM];
	scanf("%d %d %d", &num[0], &num[1], &num[2]);
	for(int i = 0; i < NUM - 1; i++)
		{
			for(int j = 0; j < NUM - i - 1; j++)
				{
					if(num[j] < num[j+1])
					{
						int temp;
						temp = num[j];
						num[j] = num[j+1];
						num[j+1] = temp;
					}
				}
		}
		if(judge1(num[0], num[1], num[2])) 
		{
			judge2(&num[0], &num[2]);
			printf("%d/%d", num[2], num[0]);
		}
	return 0;
}

int judge1(int max, int b, int c)
{
	if(b * b + c * c == max * max)
		return 1;
	else
		return 0;
}

void judge2(int * max, int * c)
{
	for(int i = 2;; i++)
	{
		if(* max % i == 0 && * c % i ==0)
		{
			* max = * max / i;
			* c = * c / i;
			i--;
		}
		if(i >= *c)
			break;
	}
}