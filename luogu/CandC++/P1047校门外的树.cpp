#include <bits/stdc++.h>

using namespace std;

int main()
{
	int length, num, i, j;
	int sum = 0;
	int left[100], right[100];
	cin >> length >> num;
	for(i=0;i<num;i++)
	{
		cin >> left[i] >> right[i];
	}
	for(j=0;j<=length;j++)
	{
		for(i=0;i<num;i++)
		{
			if(j>=left[i]&&j<=right[i])
			{
				sum++;
				break;
			}	
		}
	}
	cout << length + 1 - sum;
	return 0;
}