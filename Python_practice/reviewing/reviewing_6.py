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