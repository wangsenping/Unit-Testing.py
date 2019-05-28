#!/usr/bin/env python
# conding:UTF-8
# author: 小猪佩奇

import requests
import pymysql

# url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
# cookies = {"PHPSESSID":"9bf6b19ddb09938cf73d55a094b36726"}
# res = requests.get(url=url, cookies=cookies) # 携带cookies发送请求
# print(res.text)


conn = pymysql.connect(host='192.168.2.238',
                     port= 3306,
                     user = 'root',
                     passwd = '123645',
                     db = 'ows-test',
                     charset='utf8')
#2.从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

#3.查询数据库
cur.execute("select * from t_user where name = '王五'")

#获取查询结果
result = cur.fetchall()
print(result)

#更改数据库
cur.execute("delete from t_user where name = '小猪佩奇'")

#提交更改
conn.commit()

#关闭游标及连接
cur.close()
conn.close()