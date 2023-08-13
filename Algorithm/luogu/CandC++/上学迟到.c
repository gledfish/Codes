#include <stdio.h>
int main()
{
	int s, v, t_1, t_2, t_3, t_4;
	scanf("%d %d", &s, &v);
	t_4 = s%v;
	if(t_4==0)
	t_1 = s/v +10;
    if(t_4!=0)
    t_1 = s/v +11;

	t_2 = t_1/60;
	t_3 = t_1%60;
	if(t_2>=8&&t_3!=0)
	printf("%02d:%02d", 32-t_2-1, 60-t_3);

	if(t_2>8&&t_3==0)
	printf("%02d:%02d", 32-t_2, t_3);

	if(t_2<8&&t_3!=0)
	printf("0%d:%02d", 8-t_2-1, 60-t_3);

	if(t_2<=8&&t_3==0)
	printf("%02d:%02d", 8-t_2, t_3);
	return 0;
}