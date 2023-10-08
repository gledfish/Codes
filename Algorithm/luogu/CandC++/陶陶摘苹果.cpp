#include <bits/stdc++.h>
using namespace std;

int main()
{
	int height[10], max_height, i;
	int n = 10, j = 0;
	for(i=0;i<n;i++)
		cin >> height[i];
	cin >> max_height;
	max_height += 30;
	for(i=0;i<n;i++)
		j += (height[i]<=max_height);
	cout << j;
	return 0;
}