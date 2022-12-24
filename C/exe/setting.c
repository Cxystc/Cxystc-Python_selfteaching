#include "initial.h"
#include "setting.h"
#include "allinclude.h"

extern long long ProductNumber[4]; 
long long * setting(){
    printf("Please input your product numbers \n");
    for (int i = 0 ; i < 4 ; i++){
        scanf("%lld",ProductNumber[i]);
    }
    return ProductNumber;
}