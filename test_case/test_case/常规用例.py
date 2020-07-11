# conding: utf-8
# author: 隔壁老王

"""list排序"""
list = [1,210,11,5]
list.sort(reverse=True)
print(list)

"""for循环常规用法"""
elements=[]#列表为空
for i in range(1,6):
    print(f"一共数字有{i}")


"""随机整数型a，b,c排序"""
# list=[]
# for i in range(3):
#     x=input("please input:")
#     list.append(x)
#     list.sort()
# for i in range(3):
#     print(int(list[i]))


n = 0
while n < 20:
    n=n+1
    if n%2 == 0:
        break
    print(n)

# class newname:
    def nametest():
        list = ['唐三','沐白','小舞','宁荣荣','竹叶青']
        name={}
        newlist=[]

        while len(newlist) < len(list):
            for num in list:
                name = {"姓名":num}
                newlist.append(name)
        return newlist
