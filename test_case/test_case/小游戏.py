# conding: utf-8
# author: 小猪佩奇
# 自动格式化代码 Ctrl+Shift+f
import requests,json
import unittest
import random

"""简单小游戏"""
username = 'admin'
password = '123456'
for i in range(3):
    username = input('请输入用户名')
    password = input('请输入密码')

    #验证用户名或密码是否正确
    if username == 'admin' and password == '123456':
        print('欢迎!用户:{}'.format(username))
        print('---期待已久唷---')
        break
    else:
        print('用户名或密码错误！请重新输入')
else:
    print('账户密码错误次数超过三次！账户被锁定')

"""修改列表内容"""
list=['lisa','tuoni','jniya','shanmu','隔壁老王','zt',]

for i in range(len(list)):
    if '老王' in list[i]:
        list[i] = 'houzi'
        break
print(list)


"""判断数据是否为列表、字典或元祖"""
a=('2','lisa','3','4',)
print(isinstance(a,tuple))

"""文件读写操作"""
stream = open(r' c:\路径','rb') #读
stream = open(r' c:\路径','w') #写

with open(r' c:\路径','rb') as stream:
    container = stream.read() #读取文件内容

    with open(r' c:\路径','wb') as stream1:
        stream1.write((container))
print('文件复制完成')



def func():
    try:
        pass  # 可能会出现异常的代码
    except Exception:
        pass  # 如果有异常就执行的代码
    finally:
        pass  # 无论是否存在异常都会被执行的代码