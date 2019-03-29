# -*- conding: utf-8 -*-
calc = (1,2,3)
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#2
def fact(n):  #fact 是递归函数
    if n==1:
      return 1
    return n*(n-1)
print(fact(10000000000))

#3
d = {'a':1, 'b':2, 'c':3,}
for key in d:
    print(key)
#4

def  longmaxt(L):        #判断一个输出最大最小值
    if L == []:
        return (None,None)
    else:
        max = L(0)
        min = L(0)
        for x in L:
            if max <x:
                max = x
            if min >x:
                min = x
        return(max,min)
#5x
print([x * x for x in range(1,20)])

#6
list1 = ['hello','wolrd','8','apple','None']
list2 = [x.lower() for x in list1 if isinstance(x,str)]  #lower()是一种方法，isinstance（x,str）是判断变量是不是字符串的函数
print(list2)


#7
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))

#8
def f(haha):
    return haha *haha
hh = map(f,[1,2,3,4,5,6,7])
print(list(hh))

#9
list=sorted([36, 5, -12, 9, -21])
print(list)


#10
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return t[0].lower
print(by_score)

# #11
# n = list(map(lambda as: as * as , [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(n)
