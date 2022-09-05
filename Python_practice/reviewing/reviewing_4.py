
set1 = {1,2,3,4}
set2 = {2,4,6,8}
set3 = set1.intersection(set2)
print(set3)

s1 = {1,2,3,4,5}
s2 = {2,3,4,5,6}
s3 = s1.intersection(s2)
s4 = s1.union(s2)
s5 = s1.difference(s2)
s6 = s1.difference_update(s2)#None
print(s1,s2,s3,s4,s5,s6)

pythoners = {'jason', 'nick', 'tank', 'sean'}
linuxers = {'nick', 'egon', 'kevin'}
pythoners.difference_update(linuxers)
s7 = pythoners.difference_update(linuxers)
print(pythoners)
print(linuxers)
print(s7)
'''{'jason', 'tank', 'sean'}
{'egon', 'nick', 'kevin'}
None'''
