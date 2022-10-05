//计算累加100
#include <stdio.h>
#include <math.h>
#include <string.h>
main ()
{
    int sum = 0 ;
    int i  = 1 ;
    while (i<= 100)
    {
        sum = sum + i ; 
        i ++; 
        printf("%d\n",i);
    }
    printf("The sum of 1 to 100 is %d\n",sum);
    return 0;
}