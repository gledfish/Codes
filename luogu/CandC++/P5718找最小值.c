#include <stdio.h>
int main(void)
{
	int array_num;
	scanf("%d", &array_num);
	int array[100];
	for (int i = 0; i < array_num; ++i)
	{
		scanf("%d", &array[i]);
	}
	for(int i = 0; i < array_num - 1; i++)//排序次数：元素数目-1
	{
		for(int j = 0; j < array_num -1 - i; j++)//常用往后冒泡：j=0;j< ;j++;
		{                                        //往前冒泡：j = max; j =0/1;i--;
			if(array[j] > array[j+1]){//正序还是逆序
			int temp;
			temp = array[j+1];
			array[j+1] = array[j];
			array[j] = temp;
		}
		}
	}
	printf("%d", array[0]);
}