//处理整形变量的位数
#include <stdio.h>
int main ()
{
    int a = 12345;
    int b = a %1000;
    int c = a/100*100;
    printf ("a = %d , b = %d , c = %d\n", a, b, c);
}