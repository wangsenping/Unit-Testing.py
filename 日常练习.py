# -*- conding = utf-8 -*-
a = 85
b = 72
c = (1-b/a) * 100
c = round(c,1)
print ('小明成绩提升了%s %%' %c)



aj=['鳄鱼','皇子','yasuo']
len(aj)
print (aj[0])


sum = 0
for x in range(101):
    sum = sum + x
print(sum)


sum = 0
n = 10
while n > 0:
    sum = sum + n
    n = n-2
print(sum)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1

print('都结束了，还搞毛呀')