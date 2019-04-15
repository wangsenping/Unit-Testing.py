# -*- conding:utf-8 -*-
from django.test import client
import requests
payload = {'key1':'value1','key2':'value2'}
r = requests.post("	http://192.168.2.238:8205/web/supplier/applySupplier",data=payload)
print(r.text)