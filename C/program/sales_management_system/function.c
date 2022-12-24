#include "allinclude.h"
#include "function.h"
#include "initial.h"
#include "setting.h"

Workers *creating(int Workers_amount, long long *ProductNumber) //这里再传一个数组，可以自定义员工的工号
{
    Workers *p;
    Workers *pn;
    p = (Workers *)malloc(sizeof(Workers));
    Workers *head = p;
    for (int i = 0; i < Workers_amount; i++)
    {
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
        if (i != 4)
        {
            pn = p;
            p = p->Next;
            p = (Workers *)malloc(sizeof(Workers));
            pn->Next = p; //链接并开辟
        }
    }
    printf("Creating Successfully\n");
    return head;
}

Workers *input(Workers *head, long long *ProductNumber)
{
    long long workers;
    printf("Please input the workers Number : \n");
    scanf("%lld", &workers);
    Workers *p = head;
    int flag = 0;
    for (int i = 0; i < 4; p = p->Next)
    {
        i++;
        if (p->Number == workers)
        { // 达到了链表的位置
            flag = 1;
            printf("please input the amount you sold: \n");
            int P_num;
            for (int j = 0; j < 5; j++)
            {
                P_num = ProductNumber[j];
                switch (j)
                {
                case 0:
                    printf("%lld:", P_num);
                    scanf("%d", &p->Amount1);
                    break;
                case 1:
                    printf("%lld:", P_num);
                    scanf("%d", &p->Amount2);
                    break;
                case 2:
                    printf("%lld:", P_num);
                    scanf("%d", &p->Amount3);
                    break;
                case 3:
                    printf("%lld:", P_num);
                    scanf("%d", &p->Amount4);
                    break;
                case 4:
                    printf("%lld:", P_num);
                    scanf("%d", &p->Amount5);
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
    if (flag == 0)
    {
        printf("Your Numbers is invalid!\n");
    }
}

void infile(Workers *head, char *filename) //一口气直接，全部pull进去
{
    Workers *p;
    p = head;
    FILE *file = fopen(filename, "w+");
    for (int j = 0; j < 4; j++)
    {
        fprintf(file, "%lld\n", p->Number); //先打印员工的number
        for (int i = 0; i < 5; i++)
        {
            switch (i)
            {
            case 0:
                fprintf(file, "%lld\n", p->Amount1); //按顺序输入产品的销售额
                break;
            case 1:
                fprintf(file, "%lld\n", p->Amount2);
                break;
            case 2:
                fprintf(file, "%lld\n", p->Amount3);
                break;
            case 3:
                fprintf(file, "%lld\n", p->Amount4);
                break;
            case 4:
                fprintf(file, "%lld\n", p->Amount5);
                break;
            }
        }
        p = p->Next;
    }
    fclose(file);
    printf("saved complished!\n");
}

char *getfilepath(char *filename)
{ //修改数据存储地址也在这里,这个函数最后得到一个文件的绝对路径
    FILE *file;
    file = fopen("./setting.txt", "a+");
    char *buffer;
    buffer = (char *)malloc(sizeof(char) * 500);
    memset(buffer, 0, 500);
    buffer = fgets(buffer, 128, file);
    if (buffer[0] == '\0')
    {
        char path[128] = {0};
        printf("please input your path to save data :\n");
        scanf("%s", path);
        fwrite(path, sizeof(char), strlen(path), file);
        fclose(file);
        getfilepath(filename);
    }
    else
    {
        buffer = strcat(buffer, "/");
        buffer = strcat(buffer, filename);
        buffer = strcat(buffer, ".txt");
        return buffer;
    }
}

char *getdate(time_t timep) //把秒数变成日期的函数
{
    struct tm *p;
    p = gmtime(&timep);
    int ctime = p->tm_mday + (1 + p->tm_mon) * 100;
    char *date;
    date = (char *)malloc(sizeof(long) * 10);
    itoa(ctime, date, 10);
    return date;
}

void kept_day(int kept_day)
{
    // kept_day 保存的天数
    char *_date;
    _date = (char *)malloc(sizeof(char) * 10);
    time_t timep;
    time(&timep);
    timep -= (kept_day)*86400; //此时的日期就是开始删掉的日期
    _date = getdate(timep);

    //获取存放文件的路径
    while (1)
    {
        char *filepath;
        filepath = (char *)malloc(sizeof(char) * 100);
        filepath = getfilepath(_date);
        FILE *fp = fopen(filepath, "r");
        if (fp != NULL)
        {
            fclose(fp);
            remove(filepath);
            timep -= 86400;
            _date = getdate(timep);
        }
        else
        {
            break;
        }
    }
    printf("clear finished\n");
}

Product_Statistics *Pstatistic(long long Product_Number, int Period, long long *ProductNumber)
{
    int flag = 0;
    char *Number;
    Number = (char *)malloc(sizeof(char) * 128);

    lltoa(Product_Number, Number, 10);
    strcat(Number, "\n");
    Product_Statistics *Pstruct;
    Pstruct = (Product_Statistics *)malloc(sizeof(Product_Statistics));
    memset(Pstruct, 0, sizeof(Product_Statistics));
    Pstruct->ProductNumber = Product_Number;
    time_t timep;
    time(&timep); //今天的秒数
    for (int i = 0; i < Period; i++)
    {                       //在这个循环里就是同一个时期
        timep -= i * 86400; //得到对应天数
        char *date;
        date = (char *)malloc(sizeof(char) * 10);
        date = getdate(timep);
        char *filepath;
        filepath = (char *)malloc(sizeof(char) * 100);
        filepath = getfilepath(date);
        FILE *file = fopen(filepath, "r");
        Pstruct->ProductNumber = Product_Number;

        if (file != NULL)
        {
            for (int j = 1; j <= 5; j++)
            { //在这个循环里就是同一个文件
                char *buffer;
                buffer = (char *)malloc(sizeof(char) * 128);
                fgets(buffer, 128, file);
                memset(buffer, 0, 128);

                for (int z = 0; z < 5; z++)
                { //在这个循环里就是同一个小组5行

                    memset(buffer, 0, 128);
                    fgets(buffer, 128, file);
                    if (Product_Number == ProductNumber[z])
                    {
                        if (j == 1)
                        {
                            Pstruct->Amounta += atoi(buffer);
                            break;
                        }
                        if (j == 2)
                        {
                            Pstruct->Amountb += atoi(buffer);
                            break;
                        }
                        if (j == 3)
                        {
                            Pstruct->Amountc += atoi(buffer);
                            break;
                        }
                        if (j == 4)
                        {
                            Pstruct->Amountd += atoi(buffer);
                            break;
                        }
                    }
                }
            }
        }
        else
        {
            continue;
        }
    }
}

Worker_Statistics *Wstatistic(long long Worker_Number, int Period)
{
    char *Number;
    Number = (char *)malloc(sizeof(char) * 128);
    lltoa(Worker_Number, Number, 10);
    strcat(Number, "\n");
    Worker_Statistics *wstruct;
    wstruct = (Worker_Statistics *)malloc(sizeof(Worker_Statistics));
    memset(wstruct, 0, sizeof(Worker_Statistics));
    wstruct->WorkerNumber = Worker_Number;
    time_t timep;
    time(&timep); //今天的秒数
    for (int i = 0; i < Period; i++)
    {                       //同一个时期
        int flag = 0;       //标记
        timep -= i * 86400; //得到对应天数
        char *date;
        date = (char *)malloc(sizeof(char) * 10);
        date = getdate(timep);
        char *filepath;
        filepath = (char *)malloc(sizeof(char) * 100);
        filepath = getfilepath(date);
        FILE *file = fopen(filepath, "r");
        if (file != NULL)
        {
            do
            {
                char *line;
                line = (char *)malloc(sizeof(char) * 100);
                memset(line, 0, 100);
                fgets(line, 128, file);
                if (line[0] == '\0')
                    break;
                if (strcmp(line, Number) == 0)
                {
                    char *amount;
                    amount = (char *)malloc(sizeof(char) * 10);
                    memset(amount, 0, sizeof(char) * 10);
                    int a;

                    fgets(amount, 10, file);
                    a = atoi(amount);
                    wstruct->Amount1 += a;

                    memset(amount, 0, sizeof(char) * 10);
                    fgets(amount, 10, file);
                    a = atoi(amount);
                    wstruct->Amount2 += a;

                    memset(amount, 0, sizeof(char) * 10);
                    fgets(amount, 10, file);
                    a = atoi(amount);
                    wstruct->Amount3 += a;

                    memset(amount, 0, sizeof(char) * 10);
                    fgets(amount, 10, file);
                    a = atoi(amount);
                    wstruct->Amount4 += a;

                    memset(amount, 0, sizeof(char) * 10);
                    fgets(amount, 10, file);
                    a = atoi(amount);
                    wstruct->Amount5 += a;
                }
            } while (1);
        }
    }
}