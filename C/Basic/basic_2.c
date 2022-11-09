//递归逆
#include <stdio.h>
void change()
{
    char a;
    a = getchar();
    if (a != '\n'){
        change();
    }
    else
        return;
printf("%c", a);

}
int main(void)
{
    char a;
    printf("Please input :");
    change();
}