#include <iostream>

using namespace std;

int main()
{
	int i; 
	long long int a[5], b[5], out;
	long long int c[5] = {1,1,1,1,1};
	for(i=0;i<5;i++)
	{
		cin >> a[i] >> b[i];
		if(a[i]==0&&b[i]==0)
		break;
	}
	for(i=0;i<5;i++)
	{
		while(b[i]!=0&&a[i]!=0)
	   {
		if(b[i]%2==1)
			c[i] = (c[i] * a[i])%1000;
		a[i] = (a[i] * a[i])%1000;
		b[i] = b[i]/2;
	    }
	    if(!(a[i]==0&&b[i]==0))
	    cout << c[i] <<"\n";
	    if(a[i]==0&&b[i]==0)
	    break;
	}
}
