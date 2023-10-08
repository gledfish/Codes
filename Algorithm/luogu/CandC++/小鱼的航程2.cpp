#include <bits/stdc++.h>

using namespace std;
int main()
{
	long long day_max, dist = 0;
	int day;
	int i;
	cin >> day >> day_max;
	for(i=0;i<day_max;i++)
	{
		if(day!=6&&day!=7)
			dist += 250;
		if(day==7)
			day = 1;
		else
			day++;
	}
	cout << dist;
	return 0;
}