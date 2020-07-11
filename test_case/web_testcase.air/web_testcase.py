# -*- encoding=utf8 -*-
__author__ = "test"

from airtest.core.api import *

auto_setup(__file__)
# driver.get("http://192.168.111.143/sso/login?service=http%3A%2F%2F192.168.111.143%3A8006%2Fcas%2Fvalidate&sn=undefined")
driver.get("http://192.168.111.143:8006/fullAnalysis/analysis")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

