# conding:utf-8
# 作者; 小猪佩奇
import requests
import json

url = "http://192.168.2.242:8135/pushRecord/userList"
params = "{\"msg_record_id\":10}"
headers = {
    'Content-Type': "application/json"
    }
response = requests.request("post", url, data=params, headers=headers)
print(response.json())


headers = {'Content-Type': "application/json"}
url = "http://192.168.2.242:8135/pushRecord/list"
payload = "\r\n{\r\n    \"channel_type\":1\r\n}"
response = requests.request("post",url, data=payload, headers=headers).text
print(response)


headers = {'Content-Type': "application/json"}
url="http://192.168.2.242:8135/pushRecord/detail"
payload = "\r\n{\r\n    \"msg_record_id\":10\r\n}"
response = requests.request("post",url, data=payload, headers=headers).text
print(response)