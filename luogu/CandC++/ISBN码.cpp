
#include <iostream>

using namespace std;

int main()
{
	int i;
	int j = 1;
	char ch[13];
	for(i=0;i<13;i++)
	{
		cin >> ch[i];
	}
	int sum = ch[0];
	cout << sum;
	for(i=2;i<5;i++)
	{
		j++;
		sum +=  ch[i] * j;
	}
	for(i=6;i<11;i++)
	{
		j++;
		sum += ch[i] * j;
	}
	cout << sum;
/*	int out_num = sum%11;
	if(out_num==ch[12])
		cout << "Right";
	else
		{
			for(i=0;i<12;i++)
		   {
		   cout << ch[i];
		   }
		   cout << out_num;
		}*/
    return 0;
}
