# -*- conding:utf-8 -*-
import unittest
def division_funtion(x, y):
    return round(float(x)/y,6)
class TestDivision(unittest.TestCase):
    def test_int(self):
        self.assertEqual(division_funtion(9, 3), 3)  #  assertEqual(判断两个值是否相等)

    def test_int2(self):
        self.assertEqual(division_funtion(9, 4), 2.25)

    def test_float(self):
        self.assertEqual(division_funtion(4.2, 3), 1.4)
        print('你看，可以了吧')
if __name__ == '__main__':
    unittest.main()
