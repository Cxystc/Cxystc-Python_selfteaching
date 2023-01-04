#include "initial.h"
#include "allinclude.h"
#include "function.h"
#include "setting.h"
int status = 0;
void menu(int, int, long long *, long long *, Workers *,int *);
void main()
{
    long long *ProductNumber = setting();                      //��ȡ��Ʒ�ı�ź�
    int *Price = Pricesetting();                               //��Ǯ
    long long *WorkersNumber = wsetting();                     //��ȡԱ�����
    Workers *head = creating(4, ProductNumber, WorkersNumber); //���������������ӿ�
    int n = 0;
    menu(n, 0, ProductNumber, WorkersNumber, head,Price);
    while (1)
    {
        if (kbhit())
        {
            char c = getch(); //��ȡ������û�лس�
            if (GetAsyncKeyState(VK_UP))
            {
                n--;
                if (n < 0)
                    n = 6;
                system("cls");
                menu(n, 0, ProductNumber, WorkersNumber, head,Price);
            }
            if (GetAsyncKeyState(VK_DOWN))
            {
                n++;
                if (n > 6)
                    n = 0;
                system("cls");
                menu(n, 0, ProductNumber, WorkersNumber, head,Price);
            }
            if (GetAsyncKeyState(VK_RETURN) & 0x8000)
            {
                system("cls");
                menu(n, 1, ProductNumber, WorkersNumber, head,Price);
                if (status == 1)
                    break;
                else
                {
                    system("cls");
                    menu(n, 0, ProductNumber, WorkersNumber, head,Price);
                }
            }
            Sleep(100);
        }
    }
}

void menu(int n, int flag, long long *ProductNumber, long long *WorkersNumber, Workers *head,int *Price)
{ //����λ��
    switch (n)
    {
    case 0:
        printf("\n=============�˵�=============\n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x70); //����
        printf("            дֽ��            ");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x07); //����
        printf("\n          ��Ա��ͳ��          ");
        printf("\n          ����Ʒͳ��          ");
        printf("\n         �޸ı�������");
        printf("\n         �޸�Ա������         ");
        printf("\n         �޸Ĳ�Ʒ���         ");
        printf("\n           �˳�ϵͳ");
        printf("\n==============================\n");
        if (flag == 1)
        {
            head = input(head, ProductNumber);
            if (head == NULL)
                return;
            time_t timep;
            time(&timep); //����
            char *date = getdate(timep);
            char *filename = getfilepath(date); //�����޸����ڵĽӿ�
            infile(head, filename);             //���� *
        }
        break;

    case 1:
        printf("\n=============�˵�=============");
        printf("\n            дֽ��            \n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x70); //����
        printf("          ��Ա��ͳ��          ");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x07); //����
        printf("\n          ����Ʒͳ��         ");
        printf("\n         �޸ı�������");
        printf("\n         �޸�Ա������         ");
        printf("\n         �޸Ĳ�Ʒ���         ");
        printf("\n           �˳�ϵͳ");
        printf("\n==============================\n");
        if (flag == 1)
        {
            long long wNumber;
            printf("������Ҫ��ѯ��Ա�����ţ�\n");
            scanf("%lld", &wNumber);

            //��ѯ�Ƿ�������ˣ�
            int flag = 0;
            for (int i = 0; i < 4; i++)
            {
                if (wNumber == WorkersNumber[i])
                {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0)
            {
                printf("δ�ҵ��˹��ţ�\n");
                system("pause");
                break;
            }

            Worker_Statistics *WS;
            WS = (Worker_Statistics *)malloc(sizeof(Worker_Statistics));
            int period;
            printf("������Ҫ��ѯ������\n");
            scanf("%d", &period);
            WS = Wstatistic(wNumber, period); //��Ա��ͳ��*
            //��ӡ�ĺ���
            Wprint(WS, ProductNumber,Price);
        }
        break;
    case 2:
        printf("\n=============�˵�=============");
        printf("\n            дֽ��            ");
        printf("\n          ��Ա��ͳ��         \n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x70); //����
        printf("          ����Ʒͳ��          ");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x07); //����
        printf("\n         �޸ı�������");
        printf("\n         �޸�Ա������         ");
        printf("\n         �޸Ĳ�Ʒ���         ");
        printf("\n           �˳�ϵͳ");
        printf("\n==============================\n");
        if (flag == 1)
        {
            long long pNumber;
            printf("������Ҫ��ѯ�Ĳ�Ʒ��ţ�\n");
            scanf("%lld", &pNumber);
            //��ѯ�Ƿ��������Ʒ
            int flag = 0;
            for (int i = 0; i < 5; i++)
            {
                if (pNumber == ProductNumber[i])
                {
                    flag = 1;
                }
            }
            if (flag == 0)
            {
                printf("δ�ҵ��˲�Ʒ��\n");
                system("pause");
                break;
            }
            Product_Statistics *PS;
            PS = (Product_Statistics *)malloc(sizeof(Product_Statistics));
            int period;
            printf("������Ҫ��ѯ������\n");
            scanf("%d", &period);
            PS = Pstatistic(pNumber, period, ProductNumber); // ����Ʒͳ�� *
            //��ӡ�Ĳ���
            Pprint(PS, WorkersNumber);
        }
        break;
    case 3:
        printf("\n=============�˵�=============");
        printf("\n            дֽ��            ");
        printf("\n          ��Ա��ͳ��         ");
        printf("\n          ����Ʒͳ��          \n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x70); //����
        printf("         �޸ı�������         ");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x07); //����
        printf("\n         �޸�Ա������         ");
        printf("\n         �޸Ĳ�Ʒ���         ");
        printf("\n           �˳�ϵͳ");
        printf("\n==============================\n");
        if (flag == 1)
        {
            kept_day(daysetting(1));
            printf("�޸ĳɹ���\n");
            system("pause");
        }
        break;
    case 4:
        printf("\n=============�˵�=============");
        printf("\n            дֽ��            ");
        printf("\n          ��Ա��ͳ��         ");
        printf("\n          ����Ʒͳ��          \n");
        printf("         �޸ı�������\n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x70); //����
        printf("         �޸�Ա������         ");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x07); //����
        printf("\n         �޸Ĳ�Ʒ���         \n");
        printf("           �˳�ϵͳ           ");
        printf("\n==============================\n");
        if (flag == 1)
        {
            WorkersNumber = rwsetting();
        }
        break;
    case 5:
        printf("\n=============�˵�=============");
        printf("\n            дֽ��            ");
        printf("\n          ��Ա��ͳ��         ");
        printf("\n          ����Ʒͳ��          \n");
        printf("         �޸ı�������\n");
        printf("         �޸�Ա������         \n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x70); //����
        printf("         �޸Ĳ�Ʒ���         ");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x07); //����
        printf("\n           �˳�ϵͳ           ");
        printf("\n==============================\n");
        if (flag == 1)
        {
            ProductNumber = resetting();
        }
        break;
    case 6:
        printf("\n=============�˵�=============");
        printf("\n            дֽ��            ");
        printf("\n          ��Ա��ͳ��         ");
        printf("\n          ����Ʒͳ��          \n");
        printf("         �޸ı�������\n");
        printf("         �޸�Ա������         ");
        printf("\n         �޸Ĳ�Ʒ���         \n");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x70); //����
        printf("           �˳�ϵͳ           ");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 0x07); //����
        printf("\n==============================\n");
        if (flag == 1)
        {
            status = 1;
            kept_day(daysetting(0)); //Ĭ��������
        }
        break;
    }
}
