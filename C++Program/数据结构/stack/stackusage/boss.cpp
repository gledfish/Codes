// 标题
// 魔王语言解释
// 时间限制
// 1 S
// 	内存限制 10000 Kb
// 		问题描述
// 			见P97习题2 .2 问题输入
// 				一组数据，数据为一个字符串，表示一个待翻译的字符串。
// 					问题输出
// 						将字符串按规则翻译后输出。
// 							输入样例
// 							B(pxyzABhij)
// B
// 	输出样例
// 		tsaedsaepjpiphptsaedsaepsaepzpypxptsaedsae
#include <iostream>
#include <stack>
#include <queue>
#include <string>
	using namespace std;
class str
{
public:
	int init(char x, string y)
	{
		base = x;
		next = y;
		lenth = y.size();
		return 0;
	}
	char base;
	string next;
	int lenth;
};
int main()
{
	class str a[10];
	int n = 2; // n种对应关系 默认为2
	/*cin >> n;
	for (int i = 0; i < n; i++) {//多种关系时使用
		char tox;
		string toy;
		cin >> tox >> toy;
		a[i].init(tox, toy);
	}*/
	a[0].init('B', "tAdA");
	a[1].init('A', "sae");
	string mowang;
	cin >> mowang;
	stack<char> s, s1, s2, s3;
	int temp = 0;
	for (int i = mowang.size() - 1; i >= 0; i--)
	{
		s.push(mowang[i]);	  //将魔王说的话倒序压入栈s中
		if (mowang[i] == '(') //记录括号的组数，几组括号进行几次循环
			temp++;
	}
	char flag;
	while (temp--)
	{
		while (s.top() != ')')
		{ //把s中数据压入S1中直到找到第一个右括号
			s1.push(s.top());
			s.pop();
		}
		s.pop();
		while (s1.top() != '(')
		{					   //把s1中数据压入s2中直到找到第一个左括号
			s2.push(s1.top()); //此时s2中存入的便是嵌套最深的括号的内容
			s1.pop();
		}
		s1.pop();
		flag = s2.top(); //此时的顶端是（θδ1δ2…δn)中的θ，单独保存
		s2.pop();
		while (!s2.empty())
		{
			s3.push(s2.top()); //将剩余的压入s3中
			s2.pop();
		}
		while (!s3.empty())
		{ //将s3中数据与θ交替插入
			s1.push(flag);
			s1.push(s3.top());
			s3.pop();
		}
		s1.push(flag);
	}
	while (!s.empty())
	{ //将剩余的插入
		s1.push(s.top());
		s.pop();
	}
	stack<char> result;
	while (!s1.empty())
	{
		result.push(s1.top());
		s1.pop();
	}
	string r;
	while (!result.empty())
	{
		r = r + result.top();
		result.pop();
	}
	while (n--)
	{ // n种关系处理n次,我就不信还能有miss
		for (int i = 0; i < r.size(); i++)
		{
			if (r[i] == a[0].base)
				r = r.substr(0, i) + a[0].next + r.substr(i + 1);
			if (r[i] == a[1].base)
				r = r.substr(0, i) + a[1].next + r.substr(i + 1);
		}
	}
	cout << r << endl;
	return 0;
}
