#include <stdio.h>

struct courseNode {
    int cID;
    char name[10];
    float credit ; 
    int semester ; 
    struct courseNode *next;
};



int main ()
{
    struct courseNode Target = {
        1111,
        "target",
        0.5,
        8  
    };
    struct courseNode*  courseChange (struct courseNode *,int , float );
    const int a = 3 ; 
    const float b = 0.5;
    struct courseNode * target = & Target;
    courseChange (target,a,b);

}
struct courseNode*  courseChange ( struct courseNode * Lc ,int c ,float t)
{
    struct courseNode *p = Lc ;
    if (p == NULL) return 0 ;
    while (1) {
    if (p->cID == c){
      if (p  == NULL)break;         
      p->credit = t ;  
      p = p-> next ; 
      if (p  == NULL)break;   
    }
  }
  return Lc;

}