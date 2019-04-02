# -*- conding:utf-8 -*-
import unittest
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('setup,hello')    #在每个测试方法执行前被调用
    def tearDown(self):
        print('tearDown,bye!')
    def test_upper(self):
        self.assertEqual('xiaoli'.upper(),'XIAOLI')  #判断两个值是否相等

    def test_isupper(self):
        self.assertTrue('XIAOLI'.isupper())  #判断值是否为True
        self.assertFalse('xiaoli'.isupper())   #判断值是否为False

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):   # p判断是否异常
            s.split(2)

        if __name__ == '__main__':
            unittest.main()
