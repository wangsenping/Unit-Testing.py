# -*- conding:utf -8 -*-
import unittest
import requests

class Case(unittest.TestCase):
    def test_case01(self):
        response = requests.post(url='...',data={},headers={'Content-Tybe':'application/x-www-from-urlencoded'})
        self.assertEqual(response,status_code,200,'返回状态错误，不为200')
        print('测试通过')

    def test_case02(self):
        response = requests.get(url = '...')
        self.assertEqual(response,status_code,400,'返回状态错误，不为400')
        print('测试通过')

# if __name__=='__main__':
#    unittest.main()
