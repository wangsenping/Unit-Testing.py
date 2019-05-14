#  conding : utf-8
#  author : 小猪佩奇
import requests
import json
class webrequests:
    def post(self,url,para,headers):
        try:
            r = requests.post(url,params=para,headers=headers)
            print("获取返回状态码",r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型-0",json_r)
        except BaseException as e:
            print("请求失败",str(e))
    def get(self,url,para,headers):
        try:
            r = requests.get(url,params=para,headers=headers)
            print("获取返回状态码",r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型-1",json_r)
        except BaseException as e:
            print("请求失败",str(e))
    def post_json(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data) #将json数据类型转化为python数据类型
            r = requests.post(url,data=data,headers=headers)
            json_r = r.json()
            print("json类型转化成python数据类型-2", json_r)
        except BaseException as e:
            print("请求失败",str(e))

url = "http://192.168.2.245:8135/global/push/diff"
para = {"source": "ppmd",
    "data": [
        {
            "name": "王森平",
            "number": 2,
            "user_id": 72242
        }
    ],
    "push_id": 1,
    "template_id": 14,
    "channel_type": 1}
headers = {'Content-Type': "application/json"}

q = webrequests()
q.post(url,para,headers)
q.get(url,para,headers)
q.post_json(url,para,headers)


