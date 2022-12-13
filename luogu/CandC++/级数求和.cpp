#include <bits/stdc++.h>

using namespace std;

int main()
{
	int k, i;
	double sum;
	cin >> k;
	for(i=0,sum=0;sum<=k;)
	{
		i++;
		sum += 1.0/i;
	}
	cout << i;
	return 0;
}