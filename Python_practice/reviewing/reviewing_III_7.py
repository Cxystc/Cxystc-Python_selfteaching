M,N = input().split(' ')
cls = {}
cls_ = {}
std = {}
list_s = []
for i in range(0,int(M)):
    name,amount = input().split(' ')
    cls[name] = int(amount)    
for i in range(0,int(N)):
    list = []
    list = input().split(' ')
    list_s.append(list)

list_num = []
list_num = input().split(' ')

for key in cls.keys():
    li = []
    cls_[key] = li
    for i in range(0,int(N)):
        j = 0 
        for j in range(1,len(list_s[i])):
            if list_s[i][j] == key :
                cls_[key].append(int(list_s[i][0]))#学号
                cls_[key].append(int(list_s[i][j+1]))#分数
                break
            

for key in cls.keys():
    while len(cls_[key])/2 > cls[key]:
        min = 1
        flag = 0
        for i in range(1,len(cls_[key])):
            if cls_[key][i] < cls_[key][min]:
                min = i 
                flag  = 1
        if flag == 1:
            del cls_[key][min]
            del cls_[key][min-1]#删掉对应元素
            continue
        else :
            min = 0 
            for i in range(0,len(cls_[key]),2):
                if cls_[key][i] < cls_[key][min]:
                    min = i
            del cls_[key][min]
            del cls_[key][min+1]

for num in range(0,len(list_num)):
    flag1 = 0 
    for key in cls.keys():
        if(int(list_num[num]) in cls_[key]):
            print(key,end=' ')
            flag1 = 1 
    if flag1 == 0 :
        print("None",end=' ')
    if (num != len(list_num)):
        print(end = '\n')