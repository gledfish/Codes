#include <bits/stdc++.h>

using namespace std;

int main()
{
	double target;
	cin >> target;
	double i = 2;
	int count = 0;
	double length = 0;
	while(length<target)
	{
		count++;
		length += i;
		i = i/100 * 98;
	}
	cout << count << endl;
	return 0;
}