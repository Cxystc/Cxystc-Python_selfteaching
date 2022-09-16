#类与继承
from re import L


class Foo:
    def f1 (self):
        print("Foo.f1")
        self.f2()
    def f2 (self):
        print("Foo.f2")

class Too(Foo):
    def f1 (self):#修改了f1，Too中f1就是Too.f1
        print("Too.f1")
        self.f2()

obj = Too()
obj.f1()#打印“Too”，然后跳转到f2但是f2没有新的定义所以继承，故打印：Foo.f2

class SchoolPeople:
    def __init__(self,name ,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender
    
    def Birthday(self,Birthday):
        pass

class Schoolteacher(SchoolPeople):
    def __init__(self,name,age,gender,level):
        SchoolPeople.__init__(self,name,age,gender)#派生方法一:类调用
        self.level = level 

    def Scoring(self,Score):
        pass

class SchoolStudent(SchoolPeople):
    def __init__(self, name, age, gender,score):
        super().__init__(name, age, gender)
        # SchoolPeople._init(self,name,age,gender)#派生方法3二super
        self.score = score

#类的组合：在上述代码的基础上我们要给学生再选一门新课，但是并不是所有学生都有，所以不能在SchoolPeople上修改，我们就要用到类的组合
class Course:
    def __init__(self,price,period):
        self.price = price
        self.period = period

    def __info__(self):#不需要再输入price和period了,因为后面可以使用self.price,self.period
        print("The course is sold for %s $,and last for %s day. " %(self.price,self.period))


python = Course(200,365)
java = Course(400,200)
student1 = SchoolStudent('Tony',18,'male',100)
student1.course = python
student1.course.__info__()
print(student1.__dict__)
