# -*- conding:utf-8 -*-
# 作者:三木亲了你一口

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81}
def print_score(std):
     print('s%: s%' %(std('name'),std('score'))) #方法1

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
        print('s%: s%' % (self.name,self.score))  #方法2
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
bart = Student('麦克',88)
print(bart.name)

def print_score(std):
    print('s%:s%' % (std.name,std.score))
    print(print_score(bart))

#继承多态
class Animal(object):
    def run(self):
        print('I LOVE Animal')
    def run_twice(animal):
        animal.run()
        print(run_twice(animal()))
class Dog(Animal):
    def run(self):
        print('l love dog')


