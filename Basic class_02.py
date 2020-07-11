# -*- conding: utf-8 -*-
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
elif age <5:
    print ('zhangsan')
else:
    print('kid')

#2
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}    #dict方法查询（牺牲空间换取时间）
print(d['Michael'])

s1 = set([1,2,3,4])
s2 = set([2,3,5,6])
print(s1&s2)       #取s1和s2的并集
print(s1|s2)       #取s1和s2的交集

#3
a = 'abc'
b = a.replace('b','d')      #替换函数
print(b)

n1=255
n2=100
print('n1转换后为：%s'%hex(n1))     #转换为16进制的函数
print('n2转换后为：%s'%hex(n2))


#4
def mylove(type): #自定义函数，def语句+函数名+括号，括号加参数，最后加冒号
    if type >=0:
        return type     #return 语法代表返回值
    else:
        return -type
print(mylove(-99))

#5
import math  #math 包里有sin，cos函数
def haha(x,y,step,hh=0):
    x = x + step * math.cos(hh)
    y = y + step * math.cos(hh)
    return x,y
