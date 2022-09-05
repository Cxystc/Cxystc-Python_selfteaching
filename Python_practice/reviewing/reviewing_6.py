'''Author:Chenzkai
time:21点55分，2022年9月5日
作用域在函数的定义阶段就已经确定'''
x= 1 
def fun():
    print(x)
def fun2():
    x = 2 
    fun()
fun2()
#得到结果 1

# #关键字声明
# a = 1 
# def fun_2():
#     a += 1 
#     print(a)
# fun_2()
# #local variable 'a' referenced before assignment

a = 1 
def fun_2():
    global a 
    a += 1 
    print(a)
fun_2()
print(a)#a已经被修改

#nonlocal
def fun_3():
    b = 1 
    def fun_3_(b):#需要传入参数
        b += 1 
        print('b=',b)
    fun_3_(b)
    print('b=',b)
fun_3()#此时b还是1

def fun_4():
    b = 1 
    def fun_5():
        nonlocal b
        b += 1 
        print('b =',b)
    fun_5()
    print('b =',b)#b已经变成了2
fun_4()


c = 3
def fun_7():
    nonlocal c
    c += 1
    print('c =',c)
fun_7()
        
