#conding:utf-8
#author:sanmu

import requests
import json
# def readfile():
#     pramas=[]
#     file = open('pramas.txt','r',enconding="gbk")
#     for line in file.readlines():
#         pramas.append(line.strip('\n').split(','))
#     return pramas
#     # print(pramas)

class RunMain:

    def send_get(self,header,url,data):
        res=requests.request(get, header = header ,url = url , json = data).json()
        return res
    def send_post(self,header,url,data):
        res=requests.request(post, header = header ,url = url, json = data).json()
        return res
    def send_put(self,header,url,data):
        res=requests.request(put, header = header ,url = url, json = data).json()
        return res
    def send_delete(self,header,url,data):
        res=requests.request(delete, header = header ,url = url, json = data).json()
        return res
    def run_main(self,header,url,method,data=None):
        res = None
        if method == 'get':
            res = self.send_get(header,url,data)
        elif method == 'post':
            res = self.send_post(header,url,data)
        elif method == 'put':
            res = self.send_put(header,url,data)
        else:
            res = self.send_delete(header,url,data)
        return res
if __name__ == '__main__':
    url = ''
    data = {}