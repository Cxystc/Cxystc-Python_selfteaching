from bs4 import BeautifulSoup
import requests 

header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
html = requests.get ("https://blog.csdn.net/",headers = header)


# 在这里html是requests对象，无法直接用BeautifulSoup（用字符串形式才可解析）解析
# 故用html.content
Things = html.content
print (Things)
# 是:.text not .text()
soup = BeautifulSoup(Things,'lxml')


# 用标签名查找
response = soup.select('script')
print (response)
# print(len(response.text))resonpse已经是一个列表，不能用.text函数
# html = r.text
# soup = BeautifulSoup (html ,"lxml")

# 用类名查找注意哦有一个".""
response_1 = soup.select('.currents')
print(response_1)

# 用id名查找注意有一个井号#
response_2 = soup.select('#Feed-iconfontcolor39')
print (response_2)
# [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

# 组合查找
response_3 = soup.select('li a .current')
print (response_3)
#子标签查找
response_4 = soup.select('li > a ')
print (response_4 )


#属性查找
response_5 = soup.select ('li a[href="/nav/watchers"]')
print (len(response_5))
#<a class="current" href="/nav/watchers" target="">动态</a>



