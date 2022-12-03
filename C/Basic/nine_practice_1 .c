#include <stdio.h>
#include <string.h>
#include <math.h>
int main()
{
	void delete_string(char str[], char ch);
	int result(int *s, int n);
	int action1(int x, int y);
	int action2(int x, int y);
	int action3(int x, int y);
	int action4(int x, int y);
	char s[] = "12345* 789";
	// gets(s);
	char a1 = ' ';
	delete_string(s, a1);

	//	printf("%s\n",s);

	int i, j = 0, n;
	int a[100], b[100];
	for (i = 0; i < strlen(s); i++)
	{
		if (s[i] >= '0' && s[i] <= '9')
			a[j++] = s[i] - '0';
		if (s[i] < '0' || s[i] > '9')
			n = i;
	}

	//	printf("%d\n",strlen(s));
	for (j = 0, i = n + 1; i < strlen(s); i++)
	{
		b[j++] = s[i] - '0';
	}
	// printf("a[]=");
	// for (int l = 0; l < n; l++)
		//		printf("%d",a[l]);
		//		printf("\n");
		// printf("b[]=");
	// for (int l = 0; l < strlen(s) - n - 1; l++)////////////////
		//		printf("%d",b[l]);
		//		printf("\n");
		//		printf("%d\n",n);
    int A, B;
	A = result(a, n);
	B = result(b, strlen(s) - n - 1);
	//	printf("%d\n",A);
	//	printf("%d\n",B);
	//	printf("add%c\n",s[n]);
	switch (s[n])
	{
	case 'X':
	case 'x':
	case '*':
	    action3(A, B);
		break;
	case '/':
		action4(A, B);
		break;
	case '+':
		action1(A, B);
		break;
	case '-':
		action2(A, B);
		break;
	default:
		printf("enter data error!");
	}
	//	return 0;
}

int result(int *s, int f) //定义一个函数，用于将数字数组转化为数字
{
	int result = 0, i;
	for (i = 0; i < f; i++)
	{
		result = result * 10 + s[i];
	}
	return result;
}

void delete_string(char str[], char ch) //定义一个函数，用于删除字符串中的空格
{
	int i, j;
	for (i = j = 0; str[i] != '\0'; i++)
		if (str[i] != ch)
			str[j++] = str[i];
	str[j] = '\0';
}

int action1(int x, int y) //定义四个函数进行四则运算
{
	printf("%d+%d=%d\n", x, y, x + y);
}

int action2(int x, int y)
{
	printf("%d+%d=%d\n", x, y, x - y);
}

int action3(int x, int y)
{
	printf("%d+%d=%d\n", x, y, x * y);
}

int action4(int x, int y)
{
	printf("%d/%d=%d\n", x, y, x / y);
}
