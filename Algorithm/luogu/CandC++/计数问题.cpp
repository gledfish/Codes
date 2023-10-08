#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n, x, i, j, k, count = 0;
	cin >> n >> x;
	for(i=1;i<=n;i++)
	{
		k = i;
		while(k>0)
		{
			j = k%10;
			if(j == x)
				count ++;
			k /= 10;
		}
	}
	cout << count;
	return 0;
}