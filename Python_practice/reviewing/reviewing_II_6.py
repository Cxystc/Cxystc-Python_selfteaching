#random 模块
import random

for i in range(40):
    print(random.random())
# 大于0且小于1之间的小数

for i in range(40):
    print(random.uniform(1,3))
    #左开右开


for i in range(10):
    print(random.randint(1,3))#左闭右也闭

for i in range(10):
    print(random.randrange(1,3))#左闭右开

for i in range(10):
    print(random.choice([1,{'my friends':'tony'},2,[1,2,3]]))#多选一，其中是一个列表

#任意两个元素的组合random.sample([],k（元素数）)
for i in range(10):
    print(random.sample([1,2,'c',[1,2,3],3],3))

#洗牌
list = [1,2,3,4,5,6,7,8,8]
print(random.shuffle(list))#None这个函数return None 但是原来的list发生了变化
print(list)#[8, 2, 1, 5, 4, 7, 8, 3, 6]


