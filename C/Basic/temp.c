#include <stdio.h>
#include <string.h>
#include <math.h>
int main()
{
    void delete_string(char str[], char ch);
    int result(int *s, int n);


    char s[] = "12345* 789";
    // gets(s);
    char a1 = ' ';

    delete_string(s, a1);

    printf("%s\n", s);

    int i, j = 0, n;
    int a[100], b[100];
    for (i = 0; i < strlen(s); i++)
    {
        if (s[i] >= '0' && s[i] <= '9')
            a[j++] = s[i] - '0';
        if (s[i] < '0' || s[i] > '9')
            n = i;
    }
    printf("%d\n", strlen(s));
    for (j = 0, i = n + 1; i < strlen(s); i++)
    {
        b[j++] = s[i] - '0';
    }
    printf("a[]=");
    for (int l = 0; l < n; l++)
    printf("%d", a[l]);
    printf("\n");
    printf("b[]=");
    for (int l = 0; l < strlen(s) - n - 1; l++)
        printf("%d", b[l]);
    printf("\n");
    printf("%d\n", n);
    int a2, b2;

    a2 = result(a, 5);
    b2 = result(b, 3);
    printf("%d\n", a2);
    printf("%d\n", b2);
    return 0;
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
