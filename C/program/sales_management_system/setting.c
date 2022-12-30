#include "initial.h"
#include "setting.h"
#include "allinclude.h"

int Savedays;
int daysetting(int flag)
{
    if (flag == 1)
    {
        FILE *f = fopen("./saved_days.txt", "w+");
        char *buffer;
        buffer = (char *)malloc(sizeof(char) * 5);
        memset(buffer, 0, sizeof(char) * 5);
        printf("������Ҫ�����������\n");
        scanf("%d", &Savedays);
        itoa(Savedays, buffer, 10);
        fputs(buffer, f);
        fclose(f);
        printf("�ѱ���!\n");
        return Savedays;
    }
    if (flag == 0)
    {
        FILE *f = fopen("./saved_days.txt", "a+");
        char *buffer;
        buffer = (char *)malloc(sizeof(char) * 5);
        memset(buffer, 0, sizeof(char) * 5);
        fgets(buffer, 5, f);
        if (buffer[0] == '\0')
        {
            printf("�״�ʹ�ã����������ݱ����������\n");
            scanf("%d", &Savedays);
            itoa(Savedays, buffer, 10);
            fputs(buffer, f);
            fclose(f);
            printf("�ѱ���!\n");
            return Savedays;
        }
        else
        {
            Savedays = atoi(buffer);
            return Savedays;
        }
    }
}

long long ProductNumber[5] = {0};
long long *setting()
{
    FILE *f = fopen("./PNumber.txt", "a+");
    char *buffer;
    buffer = (char *)malloc(sizeof(char) * 50);
    memset(buffer, 0, sizeof(char) * 50);
    fgets(buffer, 50, f);

    if (buffer[0] == '\0')
    { //���û�����ݾ��¼�������
        printf("�״�ʹ�ã���������Ĳ�Ʒ��� \n");
        for (int i = 0; i < 5; i++)
        {
            scanf("%lld", &ProductNumber[i]);
            fputs(lltoa(ProductNumber[i], buffer, 10), f);
            fputc('\n', f);
        }
        fclose(f);
        return ProductNumber;
    }
    else
    {
        for (int i = 0; i < 5; i++)
        {
            ProductNumber[i] = atoll(buffer);
            memset(buffer, 0, sizeof(char) * 50);
            fgets(buffer, 50, f);
        }
        fclose(f);
        return ProductNumber;
    }
}

long long *resetting()
{
    FILE *f = fopen("./PNumber.txt", "w+");
    char *buffer;
    buffer = (char *)malloc(sizeof(char) * 50);
    memset(buffer, 0, sizeof(char) * 50);
    fgets(buffer, 50, f);

    //���û�����ݾ��¼�������
    printf("����������Ĳ�Ʒ��� \n");
    fflush(stdin);
    for (int i = 0; i < 5; i++)
    {
        scanf("%lld", &ProductNumber[i]);
        fputs(lltoa(ProductNumber[i], buffer, 10), f);
        fputc('\n', f);
    }
    fclose(f);
    printf("�޸ĳɹ���\n");
    system("pause");
    return ProductNumber;
}

long long WorkersNumber[4] = {0};
long long *wsetting()
{
    FILE *f = fopen("./WNumber.txt", "a+");
    char *buffer;
    buffer = (char *)malloc(sizeof(char) * 50);
    memset(buffer, 0, sizeof(char) * 50);
    fgets(buffer, 50, f);

    if (buffer[0] == '\0')
    { //���û�����ݾ��¼�������
        printf("�״�ʹ�ã�������Ա������ : \n");
        for (int i = 0; i < 4; i++)
        {
            scanf("%lld", &WorkersNumber[i]);
            fputs(lltoa(WorkersNumber[i], buffer, 10), f);
            fputc('\n', f);
        }
        fclose(f);
        return WorkersNumber;
    }
    else
    {
        for (int i = 0; i < 5; i++)
        {
            WorkersNumber[i] = atoll(buffer);
            memset(buffer, 0, sizeof(char) * 50);
            fgets(buffer, 50, f);
        }
        fclose(f);
        return WorkersNumber;
    }
}

long long *rwsetting()
{
    FILE *f = fopen("./WNumber.txt", "w+");
    char *buffer;
    buffer = (char *)malloc(sizeof(char) * 50);
    memset(buffer, 0, sizeof(char) * 50);
    fgets(buffer, 50, f);

    //�¼�������
    printf("��������Ա������: \n");
    fflush(stdin);
    for (int i = 0; i < 4; i++)
    {
        scanf("%lld", &WorkersNumber[i]);
        fputs(lltoa(WorkersNumber[i], buffer, 10), f);
        fputc('\n', f);
    }
    fclose(f);
    printf("�޸ĳɹ���\n");
    system("pause");
    return WorkersNumber;
}

int Price[5];
int *Pricesetting()
{
    FILE *f = fopen("./Price.txt", "a+");
    char *buffer;
    buffer = (char *)malloc(sizeof(char) * 10);
    memset(buffer, 0, sizeof(char) * 10);
    fgets(buffer, 50, f);

    if (buffer[0] == '\0')
    {
        printf("�״�ʹ�������������Ʒ�۸�\n");
        for(int i= 0 ; i< 5; i++)
        {
            int price;
            scanf("%d", &price);
            Price[i] = price;
            fputs(itoa(price,buffer,10),f);
            fputc('\n',f);
        }
        fclose(f);
        printf("����ɹ���\n");
        system("pause");
        return Price;
    }
    
    else{
        for(int i= 0 ; i < 5;i++){
            Price[i] = atoi(buffer);
            memset(buffer,0,sizeof(buffer));
            fgets(buffer,50,f);
        }
        fclose(f);
        return Price;
    }
}