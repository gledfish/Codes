#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n, i, j;
	int count = 0;
	cin >> n;
	int chinese[2000], math[2000], english[2000];
	for(i=1;i<=n;i++)
	{
		cin >> chinese[i] >> math[i] >> english[i];
	}
	for(i=1;i<=n-1;i++)
	{
		for(j=i+1;j<=n;j++)
		{
			if(abs(chinese[i]-chinese[j])<=5&&
			   abs(math[i]-math[j])<=5&&
			   abs(english[i]-english[j])<=5&&
			   abs(chinese[i]+math[i]+english[i]-chinese[j]-math[j]-english[j])<=10)
			   count++;
		}
	}
	cout << count;
	return 0;
}