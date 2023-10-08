#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n, i;
	cin >> n;
	double fn[50];
	fn[0] = 0;
	fn[1] = 1;
	fn[2] = 1;
	for(i=3;i<=n;i++)
	{
		fn[i] = fn[i-1] + fn[i-2];
	}
	printf("%.2lf", fn[n]);
	return 0;
 }
