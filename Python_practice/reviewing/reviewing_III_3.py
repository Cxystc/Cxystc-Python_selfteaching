#类与类型 List.append()方法的运行原理
# class  CLASS:
#     def __init__(self,name):
#         self.name = name 
#     def test (self):
#         print(self.name)

# class1 = CLASS("Mike")
# class1.test()#Mike

class  CLASS:
    def __init__(self):
        pass
    def test (self,name):
        print(name)#这里就可不用self.name

class1 = CLASS()#__init__() takes 1 positional argument but 2 were given
class1.test("Mike")#可以输出Mike
CLASS.test(class1,"Mike")#用未被实例化的CLASS也可以

#其实list也是一个类
list1 = [1,2,3,4,5]
print(type(list1))
list1.append(5)
print(list1)
list.append(list1,1)
print(list1)

#类的多态
class Mother:
    #预定俗成要执行的函数：第一种方法
    def Must_to_do (self):
        raise AttributeError("The function must be difined")
class son1(Mother):
    def Must_to_do(self):
        print('son1')
class son2(Mother):
    def Must_to_do(self):
        print("son2")
class son3(Mother):
    def Must_to_do(self):
        pass

One = son1()
One.Must_to_do()
two = son2()
two.Must_to_do()
Three = son3()
Three.Must_to_do()#AttributeError

import abc

class Mother2(metaclass=abc.ABCMeta) :
    @abc.abstractmethod
    def Must_to_do(self):
        pass

class duagther(Mother2):
    def NONE(self):
        pass

Four = duagther()
Four.Must_to_do()#Can't instantiate abstract class duagther with abstract method Must_to_do

