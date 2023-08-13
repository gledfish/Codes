#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
	int T, i;//T测试用例的数目。
	float x, left_equation;
	cin >> T;
	int nums[100];
	for(i=0;i<T;i++)
	{
		cin >> nums[i];
		float left = 0;
		float right = 100;
		float dis = right - left;
		while(dis >= pow(10,-6))
		{
			float mid = (left + right)/2;
		    x = mid;
		    left_equation =4 * pow(x,4) + 7 * pow(x,3) + 2 * pow(x,2) + 3 * x + 6;
			if(abs(left_equation-nums[i]) >= pow(10,-6))
			{
				if(left_equation>nums[i])
				{
					right = mid;
					dis = right - left;
					x = mid;
					left_equation =4 * pow(x,4) + 7 * pow(x,3) + 2 * pow(x,2) + 3 * x + 6;
				}
			    if(left_equation<nums[i])
				{
					left = mid;
				    dis = right - left;
				    x = mid;
				    left_equation =4 * pow(x,4) + 7 * pow(x,3) + 2 * pow(x,2) + 3 * x + 6;

				}
			}
			if(abs(left_equation-nums[i]) < pow(10,-6))
				cout << setiosflags(ios::fixed) << setprecision(4) << x <<"\n"; 
		}
		if(dis < pow(10,-6))
			cout << "No solution!" <<"\n";
	}
	return 0;
}