class Dog:
	kind = 'canine'
	def __init__(self,name):#__init__是一个方法（也就是在类里面的函数）
		self.name = name	
		self.tricks = []

	def add_trick(self,trick):
		self.tricks.append(trick)	

d = Dog ("fido")
e = Dog ('Buddy')
print (d.kind)
print (e.kind)
d.add_trick("run")
print (e.tricks)
print (d.tricks)
#注意缩进IndentationError: expected an indented block

