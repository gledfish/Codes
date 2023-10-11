#include <bits/stdc++.h>
using namespace std;

int main(void)
{
   int a, b;
   cout << "请输入值" << endl;
   cin >> a >> b;
   cout << a << endl << b << endl;
   string s;
   getline(cin, s);
   stringstream(s) >> a;
   cout << a;
   return 0;
}