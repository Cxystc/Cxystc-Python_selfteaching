'''Author:Chen zikai
time : 2022年9月5日12点55分
参数的应用
'''

#可变长参数* 和 ** 

#可变长形参*
def testing (x,y,*args):#可变长形参,*args部分封装成为元组
    print(x,y,args)
testing(1,2,3,4)

#可变长实参*
def test (x,y):
    print(x,y)
test(*(2,3))#就是把他拆开来



def testing_1 (**kwargs):
    print(kwargs)#kwargs作为参数不用加**
testing_1(c = 2 ,b = 3 ,a =2)#把赋值语句变成字典的形式

def test_1 (x,y,**kwarges):#多出来的会定义成字典
    print(x,y,kwarges)
test_1(**{'x':2,'y':'3','z':'3'})#**把字典拆开来（以关键词键值的形式），而且要要和形参对应
test_1(*{'x':2,'y':'3'})



