#include <iostream>

using namespace std;

int main()
{
   	int day_0, day;
   	long long distance; 
   	cin >> day_0 >> day;
   	int times = (day + day_0 - 8)/7;
   	int left_time = (day + day_0 - 8)%7;
   	if(day_0>=1&&day_0<=5)
   	{
   		if(left_time == 0)
   			distance = 250 * 5 * times + 250 * (6 - day_0);
   	    if(left_time>=1&&left_time<=5)
   	        distance = 250 * 5 * times + 250 * (6 - day_0) +250 * left_time;
   	    if(left_time>=6)
   	    	distance = 250 * 5 * times + 250 * (6 - day_0) +250 * 5;
   	}
   	if(day_0>=6)
   	{
   		 if(left_time==0)
   		 	distance = 250 * 5 * times;
   		 if(left_time>=1&&left_time<=5)
   		 	distance = 250 * 5 * times + 250 * left_time;
   		 if(left_time>=6)
   	    	distance = 250 * 5 * times + 250 * 5;
   	}
   	cout << distance; 
   	return 0;
}