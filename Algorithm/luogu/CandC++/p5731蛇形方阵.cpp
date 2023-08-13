#include <bits/stdc++.h>
using namespace std;

int main()
{	
	int array[10][10];
	int n;
	int num_0 = 0;
	int num= 1;
	cin >> n;
	int num_2 = n;
	while(num <= n * n)
{
	for(int i = num_0; i < num_2; i++)
	{
		array[num_0][i] = num;
		num++;
	}
	for(int i = num_0+1; i < num_2; i++)
	{
		array[i][num_2-1] = num;
		num++;
	}
	for(int i = num_2 - 2;i >= num_0;i--)
	{
		array[num_2-1][i] = num;
		num++;
	}
	for(int i = num_2 - 2;i >= num_0+1;i--)
	{
		array[i][num_0] = num;
		num++;
	}
	num_0++;
	num_2--;
}
    for(int i = 0;i < n;i++)
    {
    	for(int j = 0;j < n;j++)
    	{
    		printf("%3d", array[i][j]);
    	}
    	cout <<endl;
    }
	return 0;
}