#include <stdio.h>
#include <stdbool.h>
int main(void)
{
	long num;
	long sum = 0;
	bool input_is_good;

	printf("Please enter an integer to be summed");
	printf("(q to quit): ");
	input_is_good = (scanf("%ld", &num) == 1);
	while(input_is_good)
	{
		sum = sum + num;
		printf("Please enter next integer (q to quit): ");
		input_is_good = (scanf("%ld", &num) == 1);
	}
	printf("Those integars sum to %ld.\n", sum);

	return 0;
}