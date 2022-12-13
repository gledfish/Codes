#include <bits/stdc++.h>
using namespace std;
//结构体指针
struct student
{
	string name;
	int age;
	int score;
};
int main()
{
	student s1 = {"张三", 18, 100};
	//指针指向结构体变量
	student *p = &s1;
	cout << "姓名： " << p->name << " 年龄： " << p->age << " 分数： " << p->score << endl;
 	return 0;
}