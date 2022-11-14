#建立堆
#逐个出数
#直到堆空

def sift (list,low,high):
    temp = list[low]#堆的根结点
    i = low
    j = 2*i + 1 
    while (j <= high):
        if (j+1 <= high and list[j+1] > list[j] ):
            j += 1 
        if temp < list[j] : 
            list[i] = list[j] #如果temp不够格，那么就让现在的j上去补位，空出现在的j
            i = j
            j = 2*i + 1  
        else: 
            break
    list[i] = temp#不论如何总会出来这里接手的


def heap_sort (list):
#建立堆： 
    n = len ( list )
    for i in range((n-2)//2 ,-1 ,-1 ):#若最后一个下标 i : (i-1) / 2就是父节点 ；i = n - 1 ; 故有 
        sift (list,i,n-1) 
    #把最后堆元素提上来，然后做一次向下调整，直到堆空排序完成；
    for i in range (n-1,-1,-1):
        list[0] ,list [i] = list[i],list[0] 
        sift ( list , 0 ,i -1 ) 
    print(list)

    
list = [5,6325,168,514,987,526,256,46,145,845,145,846,15,9586,134,856,125,4215]
print(list)
heap_sort(list)

