#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//用动态内存分配来给5个学生判断有没有挂科的现象，有的话就输出这个同学的信息
int main()
{
    int *p = (int *)malloc(5 * sizeof(int));
    printf("please input the score of 5 students one by one (enter):\n");
    for (int i = 0; i < 5; i++)
    {
        scanf("%d45", &p[i]);
    }
    int flag = 0 ;
    for (int i = 0; i < 5; i++)
    {
        if (p[i] < 59 ) 
        {printf("Failed %d\n",p[i]);
        flag = 1;}
    }
    
    if (flag == 0) printf("God job!\nThey are all pass!!\n");
}   