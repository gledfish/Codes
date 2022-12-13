#include <bits/stdc++.h>

using namespace std;

int main()
{
	int i;
	int money = 0, remain = 0;
	int demoneys[12];
	int n = 12;
	for(i=0;i<n;i++)
	{
		cin >> demoneys[i];
		if(remain + 300 - demoneys[i]<0)
		{
		cout << - i - 1;
		break;
	    }
		money += (remain + 300 - demoneys[i])/100;
		remain = (remain + 300 - demoneys[i])%100;
		if(i == 11)
		cout << money * 120 + remain;
	}
	return 0; 
}