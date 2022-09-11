'''Author:chenzikai
time:2022年9月11日17点03分
匿名函数和文件操作的练习
文件路径：D:\My_code\Cxystc-Python_selfteaching-1\Python_practice\reviewing\data\匿名函数和文件操作练习文件
'''



keyname = ['name','gender','age','salary']
file_path = 'D:/My_code/Cxystc-Python_selfteaching-1/Python_practice/reviewing/data/匿名函数和文件操作练习文件'

def creating(keyname,file_path):
    final_res= []
    with open (file_path,'r') as f:
        for line in f.readlines():
            line = line.rstrip('\n')
            content = line.split(' ')
            res = dict(zip(keyname,content))
            final_res.append(res)
    return final_res

final_res = creating(keyname,file_path)
# sorted(iterable, cmp=None, key=None, reverse=False)
# max(iterable,key)

#最高工资
max_person_info = max(creating(keyname,file_path),key = lambda name: name['salary'])
print(f'Whose salary is highest?:{max_person_info}\n')

#最小年龄
min_age_person_info = min(creating(keyname,file_path),key = lambda name: name['age'])
print(f'Who is youngest?:{min_age_person_info}\n')


#首字母大写
def Title_name(final_res):
    for info in final_res:
        info['name'] = info['name'].title()
        print(info)
Title_name(final_res)

#删除以A开头的项
for item in final_res:
    if item['name'][0] == ('A' or 'a'):#记得加括号
        print(item)
        final_res.remove(item)
print(final_res)###

Title_name(final_res)