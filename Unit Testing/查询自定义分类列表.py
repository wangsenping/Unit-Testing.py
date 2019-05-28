# -*- conding:utf-8 -*-
import requests

url = "http://192.168.2.237:8118/gs_mall_channel_mk_admin/admin/commodityInfo/getMixMallCategoryTree"
params = {"channelId":"101"}
payload = {'some':'data'}
headers = { 'cache-control': "no-cache",}
response = requests.request("GET", url, data=payload, headers=headers, params=params)
print(response.json())