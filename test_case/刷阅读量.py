#  conding:utf-8
# __author__ = 'sanmu'

from bs4 import BeautifulSoup
import requests
import time  # 时间函数库,包含休眠函数sleep()
import urllib.request
import urllib.error

url = 'https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20200406&st=env'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
    "Content-Type": "application/json"}  # 构造GET方法中的Header

openner = urllib.request.build_opener()  # 创建openner对象
openner.addheaders = headers.items()  # 使用openner方法添加多个header

while 1:  # 一旦开刷就停不下来
    request = requests.get(url=url, headers=headers)  # 发送GET请求,获取博客文章页面资源
    count = count + 1  # 计数器加1
    print('这是第%s次访问' % count)  # 打印当前循环次数
    print(request.text)  # 这里用来验证是不是每次真的访问了,可以不要
    if count % 6:  # 每6次访问为1个循环,其中5次访问等待时间为31秒,另1次为61秒
        time.sleep(31)  # 为每次页面访问设置等待时间是必须的,过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数
    else:
        time.sleep(61)

# import urllib.request
# import time
#
# # 使用build_opener()是为了让python程序模仿浏览器进行访问
# opener = urllib.request.build_opener()
# # opener.addheaders = [('User-agent','Mozilla firefox/5.0.1')]
# opener.addheaders = [('User-agent','Google Chrome/74.0.3729.169')]
#
# # 专刷某个页面
# print('开始了哈...')
# tempUrl = 'https://48949420.wiz03.com/wapp/pages/view/share/s/18B9gw1L4N7G2YVUnW2d911E1Vnxwk3M2Q0a2dRIdQ01fbts'
# for x in range(200):
#     try:
#         opener.open(tempUrl)
#
#         print('%d %s' % (x, tempUrl))
#     except urllib.error.HTTPError:
#         print('urllib.error.Httperror')
#         time.sleep(1)
#     except urllib.error.URLError:
#         print('urllib.error.链接错误')
#         time.sleep(1)
#         time.sleep(0.1)
