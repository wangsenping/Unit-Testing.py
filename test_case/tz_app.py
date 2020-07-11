 # conding : utf-8
 # author = 王森平

import requests
import unittest
import json


class OneTest(unittest.TestCase):
    '''人像布控-查询设备列表'''
    def test_one(self):
        url = 'http://192.168.110.170:8006/api/ists/v1/base/map_collection/group'
        headers={
            'Content-Type':'application/json'
        }

        data = {"create_user_code":"admin",
                "name":"1",
                "group_id":"",
                "layer_type_code":1}
        }
        r = requests.request('post', url=url, headers=headers, data=json.dumps(data))
        print(r.status_code)
        self.assertEqual(r.status_code, 200)
        print(r.json())
        # print(r.text)
        # result = r.json()
        # self.assertEqual(result['code'],"0000")

    '''人像布控-查询列表'''
    def test_two(self):
        url = 'http://192.168.111.231:8080/disposition/face/list'
        headers = {'User': '1',
                   'Content-Type': 'application/json'
                   }
        data = {
            "disposition_status": 0,
            "disposition_target_type": 1,
            "page_num": 1,
            "page_size": 20,
            "subscribe_status": 0
        }
        data_1 = {
            "disposition_status": 2,
            "disposition_target_type": 2,
            "page_num": 1,
            "page_size": 20,
            "subscribe_status": 1
        }
        data_2 = {
            "disposition_status": 9,
            "disposition_target_type": 1,
            "page_num": 1,
            "page_size": 20,
            "subscribe_status": 0
        }
        data_3 = {
            "disposition_status": 1,
            "disposition_target_type": '',
            "page_num": 1,
            "page_size": 20,
            "subscribe_status": 0
        }
        r = requests.request('post', url=url, headers=headers, json=data)
        r1 = requests.request('post', url=url, headers=headers, json=data_1)
        r2 = requests.request('post', url=url, headers=headers, json=data_2)
        r3 = requests.request('post', url=url, headers=headers, json=data_3)
        print(r.status_code)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r1.status_code, 200)
        self.assertEqual(r2.status_code, 200)
        self.assertEqual(r3.status_code, 200)
        print(r.json())
        print(r1.json())
        print(r2.json())
        print(r3.json())
        result = r.json()
        result1 = r1.json
        # self.assertEqual(result['code'], "0000")
        # self.assertEqual(result1[data[data["page_num"]]],'1')


    '''人像布控-订阅/取消订阅'''
    def test_three(self):
        url = 'http://192.168.111.231:8080/disposition/subscribe'
        headers = {'User': '1',
                   'Content-Type': 'application/json'
                   }
        data={
            "action":0,
            "disposition_id":"1"
        }
        r= requests.request('post', url=url , headers= headers, data=json.dumps(data))
        print(r.json())
        self.assertEqual(r.status_code, 200)
        result = r.json()
        # self.assertEqual(result['message'],'')

        if __name__ == "__main__":
            unittest.main()
