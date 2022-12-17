#include <stdio.h>
#include <string.h>


int main()
{   
    void inverse(char a[50] , int n );
    char a[50] = {0};
    int n, i;
    scanf("%s", a);
    n = strlen(a);
    inverse(a, n); // 这里引用数组的名字，只传递地址
    for (i = 0; i < n; i++)
        printf("%c", a[i]);
    return 0;
}
void inverse(char a[50], int n)
{
    int i;
    char term;
    for (i = 0; i < n / 2; i++)
    {
        term = a[i];
        a[i] = a[n - i - 1];
        a[n - i - 1] = term;
    }
}

