#!/usr/bin/python37
#_*_ coding:utf-8 _*_

import  sys,os,getpass


os.system('clear')
i = 0
while i < 3:
    name =raw_input("请输入用户名：")

    lock_file = open('account_lock.txt','r+')
    lock_file = lock_file.readlines()

    for lock_line in lock_list:
        lock_line =lock_line.striop('\n')
        if name == lock_line:
            sys.exit('用户 %s 已经被锁定,退出' % name)



    user_file = open('account.txt','r')
    user_list = user_file.readlines()
    for user_line in user_list:
        (user,password) = user_line.strip('\n').split()
        if name  == user:
            j = 0
            while j < 3:
                passwd = getpass.getpass('请输入密码:')
                if passwd ==password:
                    print('欢迎登录管理平台，用户%s' % name)
                    sys.exit(0)
                else:
                    if j!= 2:
                        um = 2-j
                        print('用户 %s 密码错误，请重新输入，还有 %d 次机会' % (name,um))
                        j = j+1
                else:
                    lock_file.write(name + '\n')
                    sys.exit('用户 %s 达到最大登录次数，将被锁定并退出' % name)
                    else:
                        pass
                else:
                    if i ! =2:
                        print('用户 %s 不存在，还有 %d 次机会' % (name.2 - 1))
                i +=1
            else:
                sys.exit('用户 %s 不存在，退出' % name)
lock_file.close()
user_file.close()
