#include <stdio.h>
#include <string.h>

int main()
{
    char a[10];
    char b[10];
    char c[10];
    char d[10];
    int i, e = 0, f = 0, g = 0;
    scanf("%s", a);
    getchar();
    scanf("%s", b);
    getchar();
    scanf("%s", c);
    e = strlen(a);
    f = strlen(b);
    g = strlen(c);

    for (i = 0; i < e; i++)
    {
        d[i] = a[i];
    }
    for (i = 0; i < f; i++)
    {
        d[i + e] = b[i];
    }
    for (i = 0; i < g; i++)
    {
        d[i + e + f] = c[i];
    }
    printf("%s ", d);
}