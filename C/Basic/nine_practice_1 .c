#include <stdio.h>
#include <string.h>

int main()
{
    char a[4] = "1234";
    char b[5] = "ABCDE";
    char A[50] = "abcdefgh123456xy123xyxy1234";
    int i = 0; // flag 改成1并放到下面去，保证每次while循环flag初始值都是1，不然一旦falg变为0，就会一直执行更换的操作
    while (A[i] != '\0')    //遍历A
    {   
        int flag = 1; 
        if (A[i] == '1') //如果根本没有达到这个条件，flag 也应该是1
        {
            flag = 0; //出现了 "1"的时候就给flag标记为 0
            for (int j = 0; j < 4; j++)
            {
                if (A[i + j] != a[j])//要用if
                {
                    flag = 1;
                } //发现这个1不是要替换的，就标记falg为1
            }
        }

        if (flag == 0)
        {
            for (int z = 26; z >= i; z--)//for (int z = 27; z <= i; z--)你这里就只有一次啊，如果是z--的话第二个表达式应该是z>= 0 ,然后数组有27个元素，最后一个元素的下标应该是26，而不是27 
            {
                A[z+1] = A[z]; // A[j] = A[j + 1]这是左移，因为复制是从右往左赋值的
            }
            for (int s = 0; s < 5; s++)
            {
                A[i + s] = b[s];
            }
        }
        flag = 1 ;//执行完之后要记得重置
        i++;
    }
    printf("%s", A);
}