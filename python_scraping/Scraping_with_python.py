# #  用beautifulsoup写python爬虫
# # coding=utf-8
# import requests#导入requests包
# from bs4 import BeautifulSoup#从bs4导入beautifulsoup包
 
# # 获取html文档的函数，下面会调用
# def get_html(url):
#     """get the content of the url"""
#     response = requests.get(url)#从链接获取所有的网页源码
#     response.encoding = 'utf-8'#转化编码模式为utf-8
#     return response.text#返回转化之后的源码
    
# # 获取笑话的函数，下面会调用
# def get_certain_joke(html):
#     """get the joke of the html"""
#     soup = BeautifulSoup(html, 'lxml')#使用lxml解析器对网页进行解析（可以使用默认解析器，但是lxml解析器功能更加强大）
#     joke_content = soup.select('a[class="recmd-content"]')[0].get_text()#获取标签为a，属性class为"recmd-content"的内容，取第一条的内容（可以查看网页源码之后确定搜索的内容）
#     return joke_content#返回得到的内容
 
# url_joke = "https://www.qiushibaike.com"#网页地址
# html = get_html(url_joke)#获取网页源码
# joke_content = get_certain_joke(html)#获取内容
# print (joke_content)#打印获取的内容




# --codeing :utf - 8
# --author : Chenzikai 


import requests
from bs4 import BeautifulSoup
class Douban:
    def __init__ (self):
        self.URL = "https://movie.douban.com/top250?start-0"
        self.start_num = []

        for start_num in range (0,251,250):
            self .start_num.append(start_num)
        self.header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51start-0: "
            }

    
    def get_top250 (self):
        for start in self.start_num:
            start = str (start)

        html = requests.get(self.URL,params = {'start':start},headers = self.header)
        soup = BeautifulSoup(html.content,"lxml")
        # Soup = BeautifulSoup(wb_data.content, 'lxml', from_encoding='utf-8')
        names = soup.select("#content > div > div.article > ol > li > div > div.info > div.hd > a > span") 
        if names:
            for name in names :
                print("there is something here")
        else :
            print ("no conten in this page")
if __name__ == "__main__":
    cls = Douban()
    cls.get_top250()