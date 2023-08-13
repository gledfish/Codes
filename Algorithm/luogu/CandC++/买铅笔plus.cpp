#include <cstdio>

using namespace std;

int 

int main()
{
	scanf("%d", &nums);
	for(i=0;i<3;i++)
	{
		scanf("%d %d", &price, &num);
		m = price, n = num;
		while(num<nums)
		{
			num<<=1;
			price<<=1;
		}
		while(num>nums)
		{
			num = num - n;
			price = price - m;
		}
		while(num<nums)
		{
			num = num + n;
			price = price + m;
		}
		if(k<ans||ans==0)
			ans = k;
	}
	printf("%d\n",ans);
	return 0;
}