#numpy相比于py内置的数组运算，numpy更全能更高效
import numpy as np
list = [1,2,3,4,5]
numpy_arr = np.array(list)
print(numpy_arr,type(numpy_arr))

#二维或者多维
print(np.array([
    [1,2,3,4],
    [1,2,3,4]
]))

arr = np.array(
     [ [1,2,3,4],
    [1,2,3,4]]
)
arr_t = arr.T
print(arr_t,type(arr_t))#把数列倒置
print(arr.ndim)
print(arr_t.ndim)#维度：就是[]的层次

print(arr.dtype)
arr = arr.astype(np.float32)
print(arr.dtype)
print(arr.shape)
print(arr.shape[0])#行
print(arr.shape[1])#列
print(arr_t.shape)#x行x列

print(arr > 3)
# [[False False False  True]
#  [False False False  True]]

array =  np.array([
    [1,2,3],
    [4,5,6],
    [8,9,10],
    [11,12,13]
])
# print(array)
# print(array.shape)
# print(array.ndim)
print('testing :\n')
print(array[:1,:2])#左闭由开

#替换
array[:1,:2] = 0
print (array)
array [array > 4] = 0
print(array)

arr1 = np.array ([[1,2],[3,4]])
arr2 = np.array ([[5,6],[7,8]])
# print(np.hstack((arr1,arr2,arr1)))
print(np.hstack((arr1,arr2)))
print(np.concatenate((arr1, arr2), axis=1))#axis=1就是合并行
print(np.vstack((arr1,arr2)))#stack使成叠
print(np.concatenate((arr1, arr2), axis=0))#结果是一样的
