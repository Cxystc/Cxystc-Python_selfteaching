# 快速排序
def recursing(list, Left, Right):
    if (Left < Right):  # 判断至少有两个元素，才有继续排序的必要
        mid = reposition(list, Left, Right)
        recursing(list, Left, mid-1)
        recursing(list, mid + 1, Right)
# 这是一个递归


def reposition(list, left, right):  # 归位函数
    temp = list[left]  # 保存start值，空出灵活位置
    while left < right:  # 只要两个还没有相遇
        while (list[right] >= temp and right > left):  # 找严格list[right] < temp 放到temp左边
            right -= 1
        list[left] = list[right]

        while (list[left] <= temp and left < right):  # 找严格list[left] > temp 放掉temp右边
            left += 1
        list[right] = list[left]
        # 巧妙极了

    list[left] = temp  # 最后记得放回来
    return left  # 返回的时候left = right

def quick_sort ( list ,start = 0 ,end = 10 ) :
    print("Before :", list)
    recursing( list , start , end) 
    print("Finished : ",list)

list = [9, 8, 6, 5, 4, 3, 2, 11, 313]
list2 = [9, 8, 6, 5, 4, 3, 2, 11, 313]
quick_sort(list,0,len(list)-1)
quick_sort(list2,4,7)#部分排序