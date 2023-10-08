#include <iostream>
#include <algorithm>

using namespace std;

int main()	
{
	int n, i;
	int nums[3], price[3], pay[3];
	cin >> n ;
	for(i=0;i<3;i++)
	{
		cin >> nums[i] >> price[i];
	}
	for(i=0;i<3;i++)
	{
		if(nums[i]%n==0)
			pay[i] = price[i] * (nums[i]/n);
		if(nums[i]%n!=0)
			pay[i] = price[i] * (nums[i]/n+1);
	}
	sort(pay,pay+2);
	cout << pay[0];
	return 0;
}