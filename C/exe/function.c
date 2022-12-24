#include "allinclude.h"
#include "function.h"
#include "initial.h"
#include "setting.h"

Workers *creating(int Workers_amount)
{
    long long *ProductNumber = setting();
    Workers *p;
    Workers *head = p ; 
    for (int i = 0; i < Workers_amount; i++)
    {
        p = (Workers *)malloc(sizeof(Workers));
        memset(p, 0, sizeof(Workers));
        // 随便写点工号 //后期可修改
        p->Product1 = ProductNumber[0];
        p->Product2 = ProductNumber[1];
        p->Product3 = ProductNumber[2];
        p->Product4 = ProductNumber[3];
        p->Product5 = ProductNumber[4];
        if (i == 0)
        {
            p->Number = 1111111111;
        }
        if (i == 1)
        {
            p->Number = 2222222222;
        }
        if (i == 2)
        {
            p->Number = 3333333333;
        }
        if (i == 3)
        {
            p->Number = 4444444444;
        }
        if (i == 4)
        {
            p->Next = NULL;
        }
        p = p->Next;
    }
    printf("Creating Successfully");
    return head;
}

Workers *input(Workers *head,long long *ProductNumber)
{
    int workers;
    printf("Please input the workers Number : \n");
    scanf("%d", &workers);
    Workers *p = head;
    for (int i = 0; i < 4; i++)
    {
        if (p->Number == workers)
        { // 达到了链表的位置
            printf("please input the amount you sold: \n");
            int P_num;
            for (int j = 0; j < 5 ;j++){
                P_num = ProductNumber[j];
                switch (j) {
                    case 0:
                        printf("%lld:\n",&P_num);
                        scanf("%d",&p->Amount1);
                        break;
                    case 1:
                        printf("%lld:\n",&P_num);
                        scanf("%d",&p->Amount2);
                        break;
                    case 2:
                        printf("%lld:\n",&P_num);
                        scanf("%d",&p->Amount3);
                        break;
                    case 3:
                        printf("%lld:\n",&P_num);
                        scanf("%d",&p->Amount4);
                        break;
                    case 4:
                        printf("%lld:\n",&P_num);
                        scanf("%d",&p->Amount5);
                        break;                                                                        
                }
            }
            return head;
            if (i != 4)
            {
                p = p->Next;
            }
        }
    }
}

