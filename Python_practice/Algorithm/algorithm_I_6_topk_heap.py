# 得到一个列表的topk
# 对heap进行一点点修改
# heap排序中我们建立的是大根堆，这里我们要建立小根堆
# 小根堆就是根最小的堆


import random


def sift(list, low, high):  # 这是一个小根堆遍历
    i = low
    j = 2 * i + 1
    temp = list[low]
    while j <= high:  # 在规定的范围内
        if j + 1 <= high and list[j+1] < list[j]:  # 这里与排序不同，这里是选择小的子
            j += 1
        if temp > list[j]:  # 如果更小就
            list[i] = list[j]
            i = j
            j = 2 * i + 1
            # 这一个代码块是发现这个省长还是不够格的时候继续向下走，在此题中，什么是不够格呢： 就是这个省长还是比子要大
        else:
            break
        list[i] = temp


def topk(list, k):
    # 用前k项建立堆
    heap = list[0:k]
    n = len(list)
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k - 1)  # k-1作为一个下界
    # 遍历原列表：
    for i in range(k, n-1):  # 前k个数所以list[k]就是第k+1项
        if list[i] > heap[0]:
            heap[0] = list[i]
            sift(heap, 0, k - 1)
    # 挨个出数
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)  # 对得到的小堆排序
    return heap


list = list(range(1000))
random.shuffle(list)
print(topk(list, 10))
print(list)
