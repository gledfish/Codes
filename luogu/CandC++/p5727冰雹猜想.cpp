#include <bits/stdc++.h>
using namespace std;

int main()
{
    int num;
	cin >> num;
	int i = 1;
	int nums[10000];
	nums[0] = num;
	while(num!=1)
	{
		if(num%2==1)
		{
			num = num * 3 + 1;
			nums[i] = num;
			i++;
		}
		if(num%2==0)
		{
			num /= 2;
			nums[i] = num;
			i++;
		}
	}
	for(i=i-1;i>=0;i--)
	{
		cout << nums[i] <<" ";

	}
	return 0;
}