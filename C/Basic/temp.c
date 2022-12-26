void main()
{
    // 初始化链表；

    head = input(head, ProductNumber); //输入对应工号的人的销售额 *

    time_t timep;
    time(&timep); //秒数
    char *date = getdate(timep);
    char *filename = getfilepath(date); //保留修改日期的接口
    infile(head, filename);             //保存 *

    printf("Finished\n");
    kept_day(10); //保留可以留下的天数；清理缓存 *

    long long wNumber = 2222222222;
    Worker_Statistics *WS;
    WS = (Worker_Statistics *)malloc(sizeof(Worker_Statistics));
    WS = Wstatistic(wNumber, 5); //按员工统计 *

    long long pNumber = 5;
    Product_Statistics *PS;
    PS = (Product_Statistics *)malloc(sizeof(Product_Statistics));
    PS = Pstatistic(pNumber, 5, ProductNumber); //按产品统计 *
}