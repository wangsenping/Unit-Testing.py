# -*- conding: utf-8 -*-
import requests
import json
url = ('http://10.10.100.2:8239/login')
data = {"phone":"13271974882","pwd":"wsp12345"}
result = requests.get(url,data),json
print(result)
