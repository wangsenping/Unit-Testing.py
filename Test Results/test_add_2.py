#  conding: utf-8
#  author: 小猪佩奇

import requests
import ddt,unittest,json
import HtmlTestRunner
# from read_data import Excel
import xlrd

class Excel:
    def get_datas(self):
        xl = xlrd.open_workbook(r'D:\zdh-csyl\data.xls')
        sheet = xl.sheet_by_name("修改")
        items = sheet,row_values(0)
        datas = []
        for nrow in range(1,sheeet.nrows):
            data = dict()
            values = sheet.row_values(nrow)
            for ncol in range(0,len(items)):
                data[items[ncol]] = values[ncol]
            data.append(data)
        return datas


excel = Excel()

@ddt.ddt
class wn(unittest.TestCase):
    @classmethod
    def setUPClass(cls):   #登录初始化
        params = {"userName": "user000", "userPass": "pass123", "checkcode": "0000"}
        url = "http://xxxx/xxx/log/userLogin"
        cls.session = requests.session()
        rsp = cls.session.get(url, params=params)
        print(rsp.text)

        # 修改测试用例执行

    @ddt.data(*excel.get_datas())
    def test_add(self, testCase):
        params = json.loads(testCase["params"])
        # print(params)
        rsp = self.session.get(url=testCase["url"], params=params)
        self.assertEqual(testCase["except_result"], rsp.text)
        self.debug()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromName("wnboss.WNBoss"))
    with open("testReport.html", "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=3, title="xxxx接口测试报告")
        runner.run(suite)