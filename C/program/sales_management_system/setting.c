#include "initial.h"
#include "setting.h"
#include "allinclude.h"

long long ProductNumber[5] = {0} ; 
long long * setting(){
    printf("Please input your product numbers : \n");
    for (int i = 0 ; i < 5 ; i++){
        scanf("%lld",&ProductNumber[i]);
    }
    printf("Setting acomplished!\n");
    return ProductNumber;
}
