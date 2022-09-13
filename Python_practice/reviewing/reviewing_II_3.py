#内置函数的掌握
#bytes()解码
res = '你好'.encode('utf-8')
print(res)
res = bytes('你好',encoding = 'utf-8')
print(res)
#结果是一样的

#ascll码
print(chr(65))#编码
print(ord('A'))#解码
# res_1 = bytes('A,',encoding = 'ascll')#encoding 无法识别ascll
# print(res_1)
# res_1 = 'A'.encode('ascll')#一样不行
# print(res_1)

#分栏：
print(divmod(20,3))#20除三，余数、
res = divmod(20,3) 
print(res[1])#通过这种方法可以获得余数

#带有索引的迭代
l = [1,2,3,4,5]
for i in enumerate(l):
    print(i)
#(0, 1)
# (1, 2)
# (2, 3)
# (3, 4)
# (4, 5)


#eval把字符串翻译成数据类型
dict = "{'a':1, 'b':2, 'c':3, 'd':4}"
print(eval(dict)['a'])
print(eval(dict))

#是否可以哈希
hashable = hash(1)
print(hashable)
#可以返回1

print(round(3.4))#3
print(round(3.45))

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])#('d', 'e')

print(a[slice(3,5)])#一样的
