#include <bits/stdc++.h>

using namespace std;

int main()
{
	int nums[200];
	int i, j, k, n;
	cin >> n;
	int count = 0;
	for(i=0;i<n;i++)
	{
		cin >> nums[i];
	}
	for(k=0;k<n;k++)
	{
		for(i=0;i<n-1;i++)
		{
			if(i==k)
				continue;
			for(j=i+1;j<n;j++)
			{
				if(j==k)
					continue;
				if(nums[k] == nums[i] + nums[j])
				{
					count++;
					break;
				}
			}
			if(nums[k] == nums[i] + nums[j])
			    break;
		}
	}
	cout << count;
	return 0;
}