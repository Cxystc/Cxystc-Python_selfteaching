'''Author:chenzikai
time:2022年9月11日09点32分
lambda 匿名函数
'''

dict = {
    'jason': 100,
    'jaker':1000,
    'susan':2000,
    'tony':500
}

print(max(dict,key = lambda name : dict[name]))#max函数默认是比较keys
print(sorted(dict.values()))#排序了但是打印的是values
print(sorted(dict,key = lambda name : dict[name]))#排序了而且打印的也是keys

dict = sorted(dict,key = lambda name: dict[name])
print(dict)#效果是一样的

# filter(function#判断函数，为真就留下,list)
list1 =  ['jason','tank','susan','joker']
filted_list = filter(lambda name : name.endswith('n'),list1)#返回的是一个fiter对象
print(f'filted list:{list(filted_list)}')
print(f'filted list:{filted_list}')