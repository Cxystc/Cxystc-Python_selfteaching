# 1.获取数据：request
# 2.解析数据；BeautifulSoup
# 3.提取数据；BeautifulSoup
# 4.存储数据：SNV EXECL
import requests
import time
from bs4 import BeautifulSoup 

#    html = requests.get(self.URL,params = {'start':start},headers = self.header)
header =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

r = requests.get('https://s.weibo.com/top/summary',headers = header )
check_num = int(r.status_code)  
print (check_num)

html = r.text
soup = BeautifulSoup (html ,"lxml")
'''用：find_all
    items = soup.find_all('td',class_ = "td-02")'''

'''用section： pl_top_realtimehot > table > tbody > tr:nth-child(2) > td.td-02 > a
#   names = soup.select("#content > div > div.article > ol > li > div > div.info > div.hd > a > span")'''
items = soup.select()

for item in items :
    print (item.get_text())
    time.sleep (0.1)
#         # soup = BeautifulSoup(html.content,"lxml")