# conding:UTF-8
import requests
import sys
import json
url = "http://192.168.2.245:8135/global/push/diff"
payload = "{\r\n\"source\":\"ppmd\",\r\n"\
          "\"data\": [\r\n{\r\n"\
          "\"user_id\":72242,\r\n"\
          "\"user_name\":\"haha\",\r\n"\
          "\"owing_months\": 3,\r\n"\
          "\"last_pay_month\": \"2019.3\",\r\n"\
          "\"start_overdue_month\": \"2019.4\",\r\n"\
          "\"org_name\": \"jiguandangjian\",\r\n" \
          "\"first_title\": \"chashouduanxin\",\r\n"\
          "\"details_link\": \"http://localhost/test/{{openId}}\",\r\n"\
          "\"details_link_txt\": \"yingxiangzhengxin" \
          "zixun400-001-0711\"\r\n}\r\n],\r\n"\
          "\"push_id\": 1,\r\n"\
          "\"template_id\": 13,\r\n"\
          "\"channel_type\": 1\r\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "192.168.2.245:8135",
    'accept-encoding': "gzip, deflate",
    'content-length': "772",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)



url = "http://192.168.2.245:8135/global/push/diff"
payload = "\r\n{\r\n\"source\":"\
          "\"ppmd\",\r\n"\
          "\"data\": [\r\n{\r\n"\
          "\"name\": \"\",\r\n"\
          "\"number\": 2,\r\n"\
          "\"user_id\": 72242\r\n}\r\n],\r\n"\
          "\"push_id\": 1,\r\n"\
          "\"template_id\":14 ,\r\n"\
          "\"channel_type\": 1\r\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "192.168.2.245:8135",
    'accept-encoding': "gzip, deflate",
    'content-length': "230",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)

