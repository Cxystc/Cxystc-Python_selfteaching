list = []
for i in range(5):
    a = int(input ("输入数字:"))
    list.append(a)
    list.sort()
    # list = sorted(list)#都可以
for i in list:
    print(i,end = " ")
 

a = input ("请输入5个数字，用空格隔开")
list_1 = a.split(" ")
for i in list_1:
    i = int(i)

list_1.sort()
for i in list_1:
    print(i, end = " ")
