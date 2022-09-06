'''Author:Chenzkai
time:21点55分，2022年9月5日
作用域在函数的定义阶段就已经确定
闭包函数，装饰器
'''
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


# c = 3
# def fun_7():
#     nonlocal c
#     c += 1
#     print('c =',c)
# fun_7()
        
#匿名函数
function_1 = lambda x : x**4
function_1(10) #function_1 就是 lambda  需要一个参数
#用函数封装匿名函数
def function_2(a):
    #到这里要有同可作用域中的a
    return lambda x : x**a#匿名函数需要x
function_3 = function_2(2)
print(function_3(4))
    
function_4 = lambda x : x * 2 
print (function_4(2))

# y = 2 
# function_5 = lambda y : y * 2 
# print (function_5())
#<lambda>() missing 1 required positional argument: 'y'

#闭包函数
#1，实现直接调用内层函数
def xiaoai ():
    print('123')
    def greeting ():
        print("Hello")
    return greeting#返回函数的引用

function_2 = xiaoai()
function_2()#相当于xiaoai()()

#2，实现对外层变量的使用
def outer (a):
    b = 10#到这里为止outer中的ab都是局部变量
    def inner ():
        print(a+b)#局部变量被内部函数引用
    return inner#返回的是内部函数的引用
Outer = outer(5)#面向对象变成思想，和类的异曲同工？
Outer_1 = outer (6)
Outer()#15
Outer_1()#16,闭包可以识别不一样的局部临时变量a



