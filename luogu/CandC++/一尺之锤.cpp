#include <bits/stdc++.h>

using namespace std;

int main()
{
	int length;
	int i = 1;
	cin >> length;
	while(i>=1)
	{
		length /= 2;
		i++;
		if(length == 1)
		{
			cout << i;
			break;
		}
	}
	return 0;
}