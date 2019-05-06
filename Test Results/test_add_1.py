#  conding: utf-8
#  author: 小猪佩奇

import xlrd

class Excel:
    def get_datas(self):
        xl = xlrd.open_workbook(r"data.xls")
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