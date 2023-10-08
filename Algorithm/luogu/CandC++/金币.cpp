#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n, i, j;
	long long num = 0, day = 0;
	cin >> n;
	for(i=1;;i++)
	{
		for(j=1;j<=i;j++)
		{
			if(day >= n)
		{
			cout << num;
			return 0;
		}
		else
		{
			num += i;
			day++;
		}
	}
	}
	return 0;
}