#!/usr/bin
#-*- congdig:utf-8 -*-
# xiaowang
import json
from multiprocessing import Pool
import requests
from bs4 import BeautifulSonp
import pandas as pd
import pymongo
# from views import *

def generate_allurl(user_in_nub,user_in_city): #生成url
    url = 'http://'+ user_in_city + '.lianjia.com/ershoufang/pg{}/'
    for url_next in range(1, int(user_in_nub)):
        yield url.format(url_next)
