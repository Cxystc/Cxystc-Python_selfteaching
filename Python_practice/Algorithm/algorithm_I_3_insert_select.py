#插入排序

list = [9,8,7,6,5,4,3,2,1,0]
def insert_select(li):
    for x in range (1,len(list)):#range前包后不包
        j = x-1 
        i = j+1
        temp = list[i] #会被右移动的j牌占位
        while (j >= 0 and temp < list[j]):#while得到一个空位置和下标
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = temp 
        print(list)

print(list)
insert_select(list)