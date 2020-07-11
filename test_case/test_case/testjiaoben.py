# conding : utf-8
# author : 三木

# """第一题"""
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if (x!=y)and (x!=z)and(y!=z):
#                 print(x,y,z)
#
# """第二题"""

# n=0
# def task1():
#     global n
#     for i in range(100):
#         n+=1
#     print(n)



n=0
for i in range(1,10):
    if (i%2==0):
        continue
    else:
        n+=i
print(n)