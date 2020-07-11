# conding: utf-8
# author: 三木


# list = [1,2,3,1,1,2,5,67,44,2]
# print(set(list))
#
# def nonlocal_test():
#     count = 0
#
#     def test2():
#         nonlocal count  # 这里声明一下才能不报错
#         count += 1
#         return count
#
#     return test2
#
#
# val = nonlocal_test()
# print(val())
# print(val())
# print(val())

print(sum(range(1,101)))

x = 1
y = 0
while(x<101):
    y+=x
    x+=1
print(y)



















