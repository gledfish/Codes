#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
   int num, i, times, m, j;//num为整数个数，times为查询次数，m为被查询数
   int k = 0;
   cin >> num >> "\n";
   int nums[100000];
   for(i=0;i<100000;i++)
   {
   	cin >> nums[i] >> "\n";
   	if(i>=num-1)
   		break;
   }
   sort(nums,nums+num-1)
   cin >> times >>"\n";
   for(i=1;i<=times;i++)
   {
   	cin >> m >>"\n";
   	for(j=0;j<num;j++)
   	{
   		if(nums[j] == m)
   		{
   			k = 1;
   			break;
   		}
   	    cout << "Yes" << "\n";
   		if(k == 0)
   		cout << "No" << "\n";
   	}
   }
   return 0;
}