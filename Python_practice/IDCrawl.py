import Download
def IDCrawl():
    retryTime = 5
    import itertools
    for page in itertools.count(1):
        url = 'https://www.jianshu.com/p/a34509dd98c4-&d'%page
        html = Download (url) 
        if html == None:
            print('Retrying:',retryTime-1)
            retryTime -= 1
            if retryTime==0:
                print ('Crawl Rrror')
                break