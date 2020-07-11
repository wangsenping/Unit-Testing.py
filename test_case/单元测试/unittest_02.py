# conding:utf-8
# author : sanmu

import xlrd,unittest,requests,json
import HtmlTestRunner

# xlrd.open_workbook()  #打卡文件路径
# shl= book.sheet_by_name('Sheetl') #读取表格第一页
#
# rows = shl.nrows  #多少行
# cols = shl.ncols  #多少列
#


class TestMethod(unittest,testcase):
    def setUp(self):
        self.run= RunMain()

    def test_01(self):
        header=
        url =
        data={}
        res = self.run.run_main(header,url,'POST',data)
        print(res)
        self.assertEqual(res['code'],200,"测试成功")
        print('第一个用例')



