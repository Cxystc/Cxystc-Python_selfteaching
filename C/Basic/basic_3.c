#include <stdio.h>
#include <stdlib.h>

int x = 1;
int y = 2;
int main(void)
{   
  const char b = 'D';
  const int a = '\010';
  x = y = 100;
  printf("%d%d\n",x,y);
}