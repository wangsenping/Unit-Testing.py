# conding: utf-8
# author: 小猪佩奇

import requests
import json


url = 'http://192.168.2.235:5080/main/home'
data = {"mobilePhone":"13271974882",
        "password":"123321",
}
result = requests.post(url,data).json()
print (result)

def send_post(url=Mone,data=None):
    result = requests.post(url=url,data=data).json() #封装post方法
    res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
print (res)

if __name__ =='__main__':
    url = 'http://192.168.2.235:5080/main/login'
    data = {"mobilePhone": "13271974882",
            "password": "123321",
            }
    post = send_post(url = url,data = data)
