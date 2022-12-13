#include <iostream>

using namespace std;

int main()
{
	int nums[3];
	int i, j, temp;
	cin >> nums[0] >> nums[1] >> nums[2];
	for(i=0;i<2;i++)
	{
		for(j=0;j<3-i-1;j++)
		{
			if(nums[j]>nums[j+1])
			{
				temp = nums[j];
				nums[j] = nums[j+1];
				nums[j+1] = temp;
			}
		}
	}
	cout << nums[0] << " " << nums[1] << " " <<nums[2];
	return 0;
}
