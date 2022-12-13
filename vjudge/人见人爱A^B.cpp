#include <iostream>

using namespace std;

int main()
{
	long long int a, b;
	long long int c = 1;
	cin >> a >> b;
		while(b!=0&&a!=0)
	   {
	      	if(b%2==1)
			c = (c * a)%1000;
		    a = (a * a)%1000;
		    b = b/2;  
	      if(b==0)
	     {
	   	  cout << c <<"\n";
	   	  c = 1;
	   	  cin >> a >>b;
	     }                                                 
	   }
}
