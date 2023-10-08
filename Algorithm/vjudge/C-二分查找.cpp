#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
   int num, i, times, m, j;//num为整数个数，times为查询次数，m为被查询数
   int k = 0;
   cin >> num;
   int nums[100000];
   for(i=0;i<100000;i++)
   {
   	cin >> nums[i];
   	if(i>= num-1)
   		break;
   }
   sort(nums,nums+num-1);
   cin >> times;
   for(i=1;i<=times;i++)
   {
   	cin >> m;
   	int left = 0;
   	int right = num-1;
    while(left<=right)
    {
   	    int mid = (left + right)/2;
   	    if(nums[mid]>m)
   		right = mid-1;
   	    else if(nums[mid]<m)
   		left = mid+1;
   	    else if(nums[mid]==m)
   	    cout << "Yes" << "\n";
    }
    if(left>right)
    	cout << "No" << "\n";
   }
   return 0;
}