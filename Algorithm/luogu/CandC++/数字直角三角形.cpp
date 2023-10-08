#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n, i, j;
	cin >> n;
	int integer = 0;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n-i+1;j++)
		{
			printf("%02d", ++integer);
			if(j==n-i+1)
				cout << endl;
		}
	}
	return 0;
}