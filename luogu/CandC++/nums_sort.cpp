#include <iostream>

using namespace std;

int main()
{
	int nums[3];
	int i, j, temp;
	cin >> nums[1] >> nums[2] >> nums[3];
	for(i=1;i<3;i++)
	{
		for(j=1;j<=3-i;j++)
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