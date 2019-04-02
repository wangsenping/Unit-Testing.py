# -*-conding:utf-8 -*-
import requests
import json

def send_post(url=None,data=None):
    result = requests.post(url=url, data=data), json()  # 参数必须按照url，data顺序传入
    res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
    print（res）
