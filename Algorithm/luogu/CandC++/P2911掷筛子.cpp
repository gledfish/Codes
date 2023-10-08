#include <bits/stdc++.h>
using namespace std;

int main()
{
	int count = 0;
	int s1, s2, s3;
	cin >> s1 >> s2 >> s3;
	int sum_1[20000] = {0};
	for(int i = 1;i <= s1;i++)
	{
		for(int j = 1;j <= s2;j++)
		{
			for(int k = 1;k <= s3;k++)
			{
				sum_1[count] = i + j + k;
				count++;
			}
		}
	}
	int rate[20000] = {0};
	for(int sum = 3; sum <= s1 + s2 + s3; sum++)
	{
		for(int j = 0;j < s1 * s2 * s3;j++)
		{
			if(sum_1[j] == sum)
				rate[sum]++;
		}
	}
	int max_sum = 0, flag = 0;
	for(int i = 0; i < 100; i++)
	{
		if(rate[i] > max_sum)
		{
			max_sum = rate[i];
			flag = i;
		}
	}
	cout << flag <<endl;
	return 0;
}