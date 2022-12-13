#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, m, i, j, temp_sum = 0, sum = 0;
	int nums[5000];
	cin >> n >> m;
	for(i=0;i<n;i++)
	{
		cin >> nums[i];
	}
	for(i=0;i<m;i++)
	{
		sum += nums[i];
	}
	for(i=0;i<n-m+1;i++)
	{
		for(j=i;j<i+m;j++)
		{
			temp_sum += nums[j];
		}
		if(temp_sum<sum)
		{
			sum = temp_sum;
		}
		temp_sum = 0;
	}
	cout << sum;
	return 0;
}