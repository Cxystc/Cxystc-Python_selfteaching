#include <stdio.h>

int main(){
    int array[4] = {4,3,2,1};
    for ( int i = 0 ; i < 3; i++){
        for (int j = 0 ; j < 3 - i ; j++){
            printf("%d,",array[j+1]);
        }
    }
    return 0;
    
}