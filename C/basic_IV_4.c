//实现动态链表函数，删除增加清空和遍历；
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Struction
{
    int data;
    struct Struction *next;
}

main()
{
    struct Struction *Creating();                             //创建一个动态链表
    struct Struction *RunThrough(struct Struction *);         //遍历链表
    struct Struction *Adding(struct Struction *, int data);   //向链表中添加节点
    struct Struction *Removing(struct Struction *, int data); //删除列表的某个节点
    struct Struction *Clear(struct Struction *);              //清空列表
    struct Struction *Free(struct Struction *);               //销毁列表

    struct Struction *flexible_struction = Creating();
    RunThrough(flexible_struction);
}

struct Struction *Creating()
{
    struct Struction *head;    //头指针
    struct Struction *p1, *p2; //辅助指针

    head = malloc(sizeof(struct Struction));
    printf("Please input your data:\n");
    scanf("%d", &head->data);
    p1 = head; //初始化链表

    while (1)
    {
        p2 = malloc(sizeof(struct Struction)); //开辟空间//p2重新赋值
        printf("Please input your data ,use '-1'to break the loop:\n");
        scanf("%d", &p2->data); //这样才行为什么呢

        /*
        int dt;
        scanf("%d",&dt);
        p2->date = dt ; 这样给dt赋值-1，p2->data 却是1为什么*/

        if (p2->data == -1)
        {
            p1->next = p2; // 最后一个节点也要连起来，不然就会出现野指针
            p2->next = NULL;
            break; //判断退出
        }

        p1->next = p2; // 连接前面和后面
        p1 = p2;       // p1指针移动
    }
    return head;
}

struct Struction *RunThrough(struct Struction *a) //遍历链表
{
    struct Struction *p1;
    p1 = a;
    while (1) //不能读空指针//Segmentation fault
    {
        if (p1->next == NULL) // Segmentation fault
            break;
        else
        {
            printf("%d\n", p1->data);
            p1 = p1->next;
        }
    }
}