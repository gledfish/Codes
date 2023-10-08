#include <stdio.h>
void squeeze(char s1[],char s2[])
{
	char temp[100];
	int i, j, k=0;
	for(i=0;s1[i];i++)
	{
		char c = s1[i];
		for(j=0;s2[j]&&c!=s2[j];j++)
		{
			if(s2[j]==0)
				temp[k++]=c;
		}
		for(i=0;i<k;i++)
		{
			s1[i] = temp[i];
		}
		s1[i]='\0';
	}
}
	int main()
	{
		char s1[] = "abcdefghijkl",s2[] = "dhj";
		printf("s1=%s,s2=%s\n",s1,s2);
		squeeze(s1,s2);
		printf("s1=%s\n",s1);
		return 0;
	}

