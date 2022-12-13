#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, i, j, k;
	cin >> n;
	int sum = 0;
	int target_nums[100];
	int out_nums[100] ={0};
	for(i=0;i<7;i++)
	{
		cin >> target_nums[i];
	}
	int nums[100];
	for(i=0;i<n;i++)
	{
		for(j=0;j<7;j++)
		{
			cin >> nums[j];
			for(k=0;k<7;k++)
			{
				if (nums[j] == target_nums[k])
				sum++;
			}
		}
		switch(sum)
		{
			case 1:
			  out_nums[6] ++;
			  break;
			case 2:
			  out_nums[5] ++;
			  break;
			case 3:
			  out_nums[4] ++;
			  break;
			case 4:
			  out_nums[3] ++;
			  break;
			case 5:
			  out_nums[2] ++;
			  break;
			case 6:
			  out_nums[1] ++;
			  break;
			case 7:
			  out_nums[0] ++;
			  break;
			default:
			  break;
		}
		sum = 0;
	}
	for(i=0;i<7;i++)
	{
		cout << out_nums[i] << " ";
	}
	return 0;
}