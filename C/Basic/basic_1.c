#include <stdio.h>
int main()
{
    int a[10] = {1, 23};
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", a[i]);
    }

    int b[2][3] = {{1, 2, 3}, {1, 23, 5}};
    int c = b[2][1]; //可以这样子获取二维数组
    printf("%d", b);

    // 3维4维以此类推
    //没学指针这行不管，定义了数组a之后，a这个数组名就是一个指针，指向第一个元素；

    //字符数组：
    char name[15] = "Guoyongtong";
    printf("\n%s\n", name);

    //声明但是不定义
    char name1[15] = {"dilsidlfidsdifld" };//里面有16个字符 报错：最后一个结束符是\0所以实际上只有15个位置
    char name2[2][15] = {"Guoyongtong","hhhh"};
}