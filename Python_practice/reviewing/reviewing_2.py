#占位符
#traditional

name = Erytos 
birthday = 123
# print (name+"`s birthday is",birthday)

print ("%s's birthday is %s"%(name,birthday))
print ("%s's birthday is %d"%(name,birthday))

print ("{}'s birthday is {} ".format(name,birthday))
print ('{0} {1} {0}'.format(name,birthday))

print(f"{name}'s birthday is {birthday}")

salary = 6.666
print(round(salary,2))
print(f'{salary:.2f}')