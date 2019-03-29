#!usr/bin/env/python
# -*- conding:utf-8 -*-
# @time :2019/3/19
# 作者：王先生
import time
from unittest import *
import math
import requests
class TestMath(unittest.TestCase):  #unittest 所有类都可以从这个类继承下去
     def setUp(self):
payload = {'phone':'13271974882','pwd':'wsp12345'}
r = requests.get("http://10.10.100.2:8239/login", params=payload)
print(r.url)
payload = {'phone':'13271974882','pwd':'wsp12345'}
r = requests.post("http://10.10.100.2:8239/api/login/",payload)
print(r.text)

