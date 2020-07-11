# conding =utf-8
import requests
import unittest
from requests import get
# print(help(get))
class OneTest(unittest.TestCase):

    def test_sanmu (self):
        headers = {"token":"d19f2192-86eb-425b-8f11-a53d4f157ddc"}
        url = "http://192.168.111.142:8908/ICEPIDEMICCONTROL/nation/info/getAllNation"
        r = requests.request('get', headers = headers, url=url)
        print(r.status_code)
        print(r.json())
        self.assertEqual(r.status_code, 200)
        result = r.json()
        self.assertEqual(result['message'],"操作成功")
        self.assertEqual(result['code'],"0103280000")

    def test_yonghujiaoyan (self):
        headers = {"token":"d19f2192-86eb-425b-8f11-a53d4f157ddc"}
        data = {'account':"王森平"}
        url = "http://192.168.111.142:8908/ICEPIDEMICCONTROL/user/checkAccount"
        r = requests.request('get',headers=headers,url=url,data=data)
        print(r.json())


        if __name__ == "__main__":
            unittest.main()