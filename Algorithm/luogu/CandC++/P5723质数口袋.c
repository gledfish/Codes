#include <stdio.h>
int judge(int n);
int main(void){
	int targetNum;
	int array[100000];
	scanf("%d", &targetNum);
	int sum = 0, count = 0;
	if(targetNum < 2)
	{
		printf("%d\n", count);
		return 0;
	}
	else{
	for(int i = 2;;i++)
	{
		if(judge(i))
		{
			sum += i;
			array[count] = i;
			count++;
		}
		if(sum >= targetNum)
			break;
	}
	for(int i = 0;i < count;i++)
	{
		printf("%d\n", array[i]);
	}
	printf("%d\n", count);
	return 0;
}
}
int judge(int n){
	int flag = 1;
	if(n == 2||n == 3)
		return flag;
	for(int i = 2;i <= n / 2;i++)
	{
		if(n % i == 0){
			flag = 0;
			break;
		}
	}
	return flag;
}