#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
	int T, i;//T测试用例的数目。
	float x, left_equation;
	scanf("%d", &T);
	int nums[100];
	for(i=0;i<T;i++)
	{
		scanf("%d", &nums[i]);
		float left = 0;
		float right = 100;
		float dis = right - left;
		while(dis >= pow(10,-6))
		{
			float mid = (left + right)/2;
		    x = mid;
		    left_equation =4 * pow(x,4) + 7 * pow(x,3) + 2 * pow(x,2) + 3 * x + 6;
			if(left_equation>nums[i])
				{
					right = mid;
					dis = right - left;
				}
			if(left_equation<nums[i])
				{
					left = mid;
				    dis = right - left;
				}
			if(left_equation==nums[i])
				printf("%.4f\n", x);
		}
		if(dis < pow(10,-5))
			printf("No solution\n");
	}
	return 0;
}