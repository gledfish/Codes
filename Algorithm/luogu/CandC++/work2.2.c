/*
  name:cosx.c
  author:gled fish
  time:2021/10/31
*/
#include <stdio.h>
#include <graphics.h>
#include <conio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
	initgraph(800,700);
	setbkcolor(white);
	setlinecolar(black);
	cleardevice();
	setorigin(400,350);
	line(-400,00,400,00);
	line(0,350,0,-350);
	for(int i = -500;i<=500;i++)
	{
		line(s * i,0,s * i, -10);
		if(i%5==0)
			line(s*i,0,s*i,-15);
		line(0,s * i,10,s*i);
		if(i%5==0)
			line(0,s*i,15,s*i);
	}
	double x,y;
	for(x=-100;x<=100;x=x+0.001)
	{
		y = cos(x);
		putpixel(s*x,-s*y,black);
	}
	system("pause");
	return 0;
 } 