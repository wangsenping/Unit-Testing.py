#_*_ conding: utf-8 _*_
#1
s = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(s)
#2
def um():
    print('张三')
f = um
print(f())
#2
# import functools   此模块包含偏函数
# def log(func)
#     @functools.wraps(func)
#     def wrapper(*)

#3
import functools
print(int('1234',base=16))
print(int('520',base=0))

#4
import functools
max=functools.partial(max,10)
max=(5,6,7)
print(max)
#5
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