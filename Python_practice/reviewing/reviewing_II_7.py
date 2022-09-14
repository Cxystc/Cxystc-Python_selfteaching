import sys
print(sys.version)
print(sys.platform)
print(sys.exec_prefix)

import json
struct_data = {'name': 'json', 'age': 23, 'sex': 'male'}
print(struct_data,type(struct_data))#dict

data = json.dumps(struct_data)#有s的，data是Dinary
print(data,type(data))#str

data = json.loads(data)
print(data,type(data))#dict
#只要data的格式满足json格式（就是要用双引号）json都可以加载，不一定要是dumps出来的

#  #序列化
with open("D:/My_code/Cxystc-Python_selfteaching-1/Python_practice/reviewing/data/testing_data2",'w') as fw:#a是附加
    json.dump(struct_data,fw)#没有s的是储存到文件中#dumps将dict转化为str，dump会加上文件操作

# #反序列化，就是把data从文件的str格式变回来
with open("D:/My_code/Cxystc-Python_selfteaching-1/Python_practice/reviewing/data/testing_data2") as fr:
    data = json.load(fr)#loads 把str转化为dict，load加上了文件处理
print(data,type(data))


#pickle python特有的序列化模块，它可以储存所有的python类型，包括对象，但是可能会有跨版本不兼容的问题，只能用于储存不重要的内容
# import pickle
# pickle 的调用方式和json几乎一模一样 pickle.dumpd(data),pickle.dump(date,file) 但是load有点不同：pickel.loads(file)

#值得注意的是，pickle要用二进制储存和读取，wb(write,brinary) rb
