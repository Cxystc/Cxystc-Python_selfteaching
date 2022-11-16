#include <stdio.h>
int main()
{   
    int sum = 0 , n ;
    scanf("%d",&n);
    do {
        if ((n/100)%10 == 3 ){
            sum += n; 
        }
        scanf("%d",&n);
    }while(n);
    printf("sum = %d\n",sum);
}
