# conding: utf-8
# author: 小猪佩奇

import pymysql

class DB:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.2.238',
                     port= 3306,
                     user = 'root',
                     passwd = '123645',
                     db = 'ows-test',
                     charset='utf8')
        self.cur = self.conn.cursor() #从连接建立游标，才能操作数据库

    def __del__(self): #析构函数，实例删除时触发
        self.cur.close() #关闭游标
        self.conn.close()#关闭连接

    def query(self,sql):
        self.cur.execute(sql)  #更改数据库
        return self.cur.fetchall() #获取查询结果

    def exec(self,sql):
        try:
            self.cur.execute()
            self.conn.commit()  #提交数据库

        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self,name):
        result = self.query("select * from user where name'{}'".format(name))
        return True if result else False  #为空返false

    def del_user(self,name):
        self.exec("delete from user where name='{}'".format(name))

