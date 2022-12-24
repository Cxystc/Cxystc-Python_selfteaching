#include "initial.h"
#include "allinclude.h"
#include "function.h"
#include "setting.h"
//宏定义产品的长度
// 定义结构体,员工导向
void main()
{
    // 初始化链表；
    Workers* head = creating(4); //保留输入接口
    memset(head,0 ,sizeof(Workers));
    long long * ProductNumber = setting();
    head = input(head,ProductNumber);
}