# -*- conding: utf-8 -*-
import requests
import json
url = ('http://10.10.100.2:8239/login')
data = {"phone":"13271974882","pwd":"wsp12345"}
result = requests.get(url,data),json
print(result)

import socket
 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 s.connect(('www.sina.com.cn',80))