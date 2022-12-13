#include <stdio.h>
#include <ctype.h>
int main(void)
{
	char ch;

	printf("Give me a letter of the alphabet, and I will give ");
	printf("an animal name \n beginning with that letter.\n");
	while((ch = getchar()) != '#')
	{
		if('\n' == ch)
			continue;
		if(islower(ch))
			switch (ch)
		{
			case'a':
			printf("argali, a wild sheep of Asia\n");
			break;

			case'b':
			printf("babirusa, a wild pig of Malay\n");
			break;

			case'c':
			printf("coati, racoonlike mammal\n");
			break;

			default:
			printf("That's a stumper!\n");
		}
		else
			printf("I recognize only lowercase letters.\n");
		while(getchar() != '\n')
			continue;
		printf("Please type anothor letter or a #.\n");
	}
	printf("Bye!\n");

	return 0;
}