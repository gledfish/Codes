#include <bits/stdc++.h>
using namespace std;

int main()
{
    int M, N;
	cin >> M >> N;
	int count_array[10] = {0};
	for(int i = M;i <= N; i++)
	{
		int j = i;
		while(j>0)
		{
			int temp_num = j%10;
			count_array[temp_num]++;
			j /= 10;
		}
	}
	for(int i = 0;i < 10; i++)
	{
		cout << count_array[i] <<" ";
	}
	return 0;
}