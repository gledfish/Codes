#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n, i, j;
	long long sum = 0, num = 1;
	cin >> n;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=i;j++)
		{
			num *= j;
		}
		sum += num;
		num = 1;
	}
	cout << sum;
	return 0;
}