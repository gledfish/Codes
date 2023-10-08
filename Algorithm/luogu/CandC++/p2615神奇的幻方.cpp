#include<bits/stdc++.h>
using namespace std;

long s[10001][10001];
int n;
int sum=1, i, j;//i表示层，j表示列，sum计数 

int main()
{
	cin>>n;
	i=1, j=n/2+1;//因为1是从n/2+1列开始，所以以此为j 
	
	while(sum<=n*n)
	{//到n*n就停 
		s[i][j]=sum;//开始赋值 
		
		if(sum%n==0)
		{//如果为n的倍数 
			++i;//就往下走 
			
			if(i==n+1)// 到头了 
			i=1;
		}
		else
		--i, ++j;//其他点往右上方走
		if(i==0) 
			i=n;
		if(j==n+1)
		 j=1;//如果向右向上到了头 
	    ++sum;   
	}
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
		cout<<s[i][j]<<" ";
		cout<<endl;
	}//白给的输出 
    return 0;
}