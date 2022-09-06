'''Author : Chenzikai
2022年9月6日14点41分
装饰器学习'''

def decoration(func):#装饰器就是把一个函数包裹起来,这个是包装，而不是包的函数,装饰器实际上是一个闭包
    def decorator ():
        print('1111Now we start to decorate your function')
        func()
        print('33333Now,we have finished decorating your function')
    return decorator#返回内部函数

def function_need_decorate():
    print('22222I am the function that need to be decorated')

testing = decoration(function_need_decorate)
testing()#这是一种表达方式

@decoration#这是语法糖的表达方式
def function_need_decorate():
    print('22222I am the function that need to be decorated')
function_need_decorate()


