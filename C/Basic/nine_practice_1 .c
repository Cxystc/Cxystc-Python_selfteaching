#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
	char *p;
	char str[100] = {0}; // 用来临时储存输入的数
	gets(str);
	int i = strlen(str)+1, j = 0;
	p = (char *)malloc(1);
	for (; str[0] != '\0';)
	{
		realloc(p, i);
		strcpy(p + j, str);

		memset(str, 0, sizeof(str));
		gets(str);
		i = i + strlen(str);
		j = j + strlen(str);
	}
	puts(p);
}