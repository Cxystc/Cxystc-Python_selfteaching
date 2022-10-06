#include <stdio.h>
int main()
{      
    char a[10];//声明一个字符串
    printf("Please input your string:\n");
    scanf("%s",a);//a本身就是一个地址不用加&
    printf("%s\n",a);
    return 0;
}