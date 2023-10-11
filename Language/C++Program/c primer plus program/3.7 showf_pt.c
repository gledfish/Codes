/*
  name:showf_pt.c
  author:gled fish
  time:2021/10/20
*/
#include <stdio.h>
int main(void)
{
	float about = 32000.0;
	double abet = 2.14e9;
	long double dip = 5.32e-5;
	printf("%f can be written %e\n",about,about);
	//下一行要求编译器支持c99或其中的相关特性。
	printf("And it's %a in hexadecima1,powers of 2 notation\n",about);
	printf("%f can be written %e\n",abet,abet);
	printf("%lf can be written %le\n",dip,dip);
	return 0;
}
