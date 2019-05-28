# -*- conding:utf-8 -*-
import requests
url = "http://192.168.2.237:8118/gs_mall_channel_mk_admin/admin/channelCustomCategory/insertCategory"
querystring = {"channelId":"125"}
payload = "{\r\n\"channelId\":\"135\",\r\n "\
          "\"name\":\"test2\",\r\n " \
          "\"channelName\":\"ceshi\",\r\n " \
          "\"pid\":\"85\",\r\n  " \
          "\"type\":\"2\",\r\n  " \
          "\"display\":\"1\",\r\n " \
          "\"imgUrl\":\"http://www.baidu.com/\",\r\n " \
          "\"keywords\":\"test2\",\r\n " \
          "\"externalLinks\":\"www.bjson.com\",\r\n " \
          "\"suppilerCategorys\":{\r\n " \
          "\"suppilerCategoryLinks\":[{\r\n  " \
          "\"suppilerCategoryLink\":[\r\n  " \
          "{\"id\":2,\"code\":\"0002\",\"name\":\"shijian\"},\r\n"\
          "{\"id\":3,\"code\":\"0003\",\"name\":\"shijian2\"}\r\n  " \
          "]\r\n }]\r\n }\r\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    }
response = requests.request("GET",url,data=payload, headers=headers, params=querystring)
print(response.json())