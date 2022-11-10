#选择排序


def select_sort(li):
    li_new = [] 
    for i in range(len(li)):
        min_val = min(li)
        li_new.append (min_val)
        li.remove (min_val)
    return li_new
#这种做法很容易理解但是不是原地排序，复杂度高而且波坏了原来的数组


def select_sort_b (li):
    for i in range (len(li)-1):
        min_loc = i#可以扣一点，从i+1开始
        for j in range (i+1,len(li)):#前包后不包
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc] , li[i]
        print(li)
        #注意无序区的位置

li = [3,2,5,1,4,3,6,4]
# print(select_sort(li))
select_sort_b (li)
print(li)
