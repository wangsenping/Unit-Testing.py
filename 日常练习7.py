# -*-conding:utf-8 -*-
import requests
import json

def send_post(url=None,data=None):
    result = requests.post(url=url, data=data), json()  # 参数必须按照url，data顺序传入
    res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
      return(res)

if__name__=='__main__'
url = 'http://10.10.100.2:8239/login'
data={"phone":"13271974882","pwd":"wsp12345"}

post = send_post(url=url,data=data)


