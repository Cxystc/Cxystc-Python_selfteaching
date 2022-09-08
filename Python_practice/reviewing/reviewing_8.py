'''Author:chenzikai
Time:2022年9月7日21点03分
迭代器，三元推导式，列表推导式，字典生成式，生成器
'''
#\_\_iter\_\_方法，有这个方法的都是可迭代对象
#这个方法返回的是迭代器对象
from ast import Try
from typing import Iterable


print('nick'.__iter__())
print([1,2,3,4,5,6,7,8,9,10,11].__iter__())
print((1,2,3,4,5,6,7,).__iter__())
print({'name':'nick','birthday':'0217'}.__iter__())
# <method-wrapper '__iter__' of str object at 0x000001C068F16E70> 没有加括号的错误输出
# <method-wrapper '__iter__' of list object at 0x000001C068F0EB00>
# <method-wrapper '__iter__' of tuple object at 0x000001C068EC20A0>
# <method-wrapper '__iter__' of dict object at 0x000001C065E92980>
# <str_iterator object at 0x00000224192BCFD0>  正确输出
# <list_iterator object at 0x00000224192BCFD0>
# <tuple_iterator object at 0x00000224192BCFD0>
# <dict_keyiterator object at 0x00000224192B5B80> 
#\_\_next\_\_方法返回的是迭代后的内容
#这个方法必须是对迭代器使用
# while True:
#     try:
#         print('Hello,world'.__next__())#会报错
#     except StopIteration:
#         break
Iter = "Hello world".__iter__()#记得加上括号
while True:
    try:
        print(Iter.__next__())
    except StopIteration:
        break

# 三元表达式
x = 20
y = 30
print(x if x > y else y)#哪个大打印哪个

#列表推导式
Iterable1 = [1,23,24,25,26,27]
print ([i for i in Iterable1])
#注意上面输出的是一个列表
#i是在迭代，但是print没有迭代，使用print打出的是一个迭代器，如果加上[]就是列表中迭代

for i in Iterable1:
    print(i)
#print和i都在迭代，所以可以打印

#字典生成式
list1 = [1,23,24,25,26,27]
list2 = [1,23,44,55,66,77,78,]
print({a:b for a in list1 for b in list2})

#zip 压缩
c = [1,2,3]
d = [11,22,33]
res = zip (c,d)
print (res)#<zip object at 0x0000021599AF0140>
dict = {e:f for e,f in res}
print(dict)#{1: 11, 2: 22, 3: 33}
res_1 = zip(dict.keys(),dict.values())
print(res_1)
if res_1 == res:
    print('yes')
elif res_1 is res:
    print('yes')
else:print('\nNo,they are difference')
dict1  = {x:y for x,y in res_1}
print(dict)


if dict1 == dict:
    print('yes')#dict == dict1
if dict1 is dict:
    print('yes')#dict isn't dict1
else:print('\nNo,they are difference')

#生成器：其实就是一个生成迭代器的函数，只能做迭代操纵，每次遇到yield都会暂停并且保存当前状态，下一次运行next就从此开始
def fibonacci(m):
    a,b,n = 0,1,0
    while True:
        if n > m:
            return 
        yield a
        a,b = b,a+b
        n += 1

f  = fibonacci (10)
while True :
    try:
        print(next(f),'\n')
    except StopIteration :
        break

def generator():
    print('1')
    yield 2
    print('3')
    yield 4
    print('5')
    yield 6
    print('7')
    yield 8

generation = generator()
for i in generation:
    print(i)

#同样的结果还可以表示为
def Ud_generator():
    yield from range(1,9)

F = Ud_generator()
for i in Ud_generator():
    print(i)

def test(val):
    while True:
        y = yield val#首次运行的时候先运行赋值语句的右侧
        val = y 
t = test(19)
print(next(t))
print(next(t))
# 19
# None               #所以第二次运行的时候y根本没有被赋值，知道迭代器重启，yield = None 才赋值，所以会返回None

def test(val):
    while True:
        y = yield val#首次运行的时候先运行赋值语句的右侧
        val = y 
t = test(19)
print(next(t))
print(t.send(20))
# 19
# 20

#生成器的三元表达式
gen  = (i for i in range(19))

#相当于
# def gen_(val):
#     a = 0
#     n = 0 
#     while True:
#         if n > val:
#             return
#         yield a 
#         a += 1 
#         n += 1 
# gen_1 = gen_(19)
# for a in gen_1:
#     print(a)

for a in gen:
    print(a)
