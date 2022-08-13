'''Author : Erytos
created date : 2022，0811 11点01分'''
import abc


msg = '    lllHello worldlll    '
print(msg[1:4:2])
print(msg)
print(msg.strip())
print(msg.strip('l'))
print(msg.strip('l '))

print(msg.lstrip())
print(msg.rstrip())

msg_2 = 'Erytos'
print(msg_2.upper())
print(msg_2.lower())

msg_3 = 'E:r:y:t:o:s'
print(msg_3.split(':'))
print(msg_3.split(':',3))
print(msg_3.rsplit(':',3))

msg_4 = msg_3.split(':')
print(':'.join(msg_4))
print(''.join(msg_4))

msg_5 = '1 + 1 = 1'
print(msg_5.replace('1','2'))#没有改变原来的数据

print(msg_5.isdigit())

msg_6 = 'abc'
msg_7 = msg_6.capitalize()
print(msg_7.swapcase())
print(msg_6.count('a'))

str1 = "this"
str2 = str1.zfill(10)
print(str2)

str1 = "this"
str2 = str1.center(10,"#")#居中并且填充到10个字符
print(str2)

str1 = "this"
str2 = str1.ljust(10,"$")#居左同rjust
print(str2)

str_1 = "this is a test"
trans_tab = str.maketrans('is','IS',"a")#（找对象，换掉的‘备胎’）
print(trans_tab)#相当于创建一个表格对应（映射）
print(str_1.translate(trans_tab))


name_list = [1,2,3,4,5,1]
# name_list.clear()
print(name_list)
#clear 不会创建新列表
name_list.remove(3)
print(name_list)
del name_list[2]
print(name_list)
name_list.pop()
print(name_list)
print(name_list.count(1))
print(name_list.index(1))#找第一个出现的位置

dic = {'a': 1 ,'b': 2 ,'c' : 3}
print(dic['a'])
abc = dic.get('a')#返回值
print(abc)
# dic.fromkeys(一个关于键的元组，指定值)
seq = ('d','e','f')
value = [1,12,1]
dic_1 = dic.fromkeys(seq,value)#产生新的字典每一个键对应的值是一样的
dic.update(dic_1)#合并
print(dic)
print(dic_1)

s='hello tank tank say hello sb sb'
dic = {}
for item in s.split():#item 就是键值
    if item in dic:
        dic[item] += 1 #dic[item]才是值
    else:
        dic[item] = 1 
print(dic)




