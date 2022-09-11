'''
Author:Chenzikai
time:2022年9月9日15点21分
递归的运用 recursive'''

# a = 1 // 2 
# print (a)不够被2整除的返回0
from random import randint
nums = [randint(1, 100) for i in range(99)]
nums = sorted(nums)
print(nums)

def Searching_number(list,target_number):

    mid_idx = len(list) // 2 
    
    if target_number not in list:#判断对应的数字不在列表里
        print('The number is not in the list')
        return False

    elif list[mid_idx] == target_number:
        print('I found it')
        return True

    elif list[mid_idx] > target_number:
        #大了，截取左边的
        list = list[:mid_idx+1]
        print(list)
        # maximum recursion depth exceeded while getting the repr of an object 递归超过最大深度 为什么？
        Searching_number(list,target_number)
        
    elif list[mid_idx] < target_number:
        list = list[mid_idx:]
        print(list)
        Searching_number(list,target_number)


Searching_number (nums,101)


if 101 in nums:
    print('yes')
else: 
    print('no')