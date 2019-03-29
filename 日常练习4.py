#-*- coding:utf-8 -*-
#1
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grage(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return'c'
lisa = Student('lisa',99)
bart = Student('bart',50)
print(lisa.name,lisa.get_grage())
print(bart.name,bart.get_grage())

#2
a=list()
print(isinstance(a,list))   #isinstance()方法是判断变量是不是某个类型
print(isinstance(a,dict))
print(type(a))
#3
print(type(123))