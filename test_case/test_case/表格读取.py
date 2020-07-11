#  conding : utf-8
#  author : 隔壁老王

import xlrd
import random
# def excel():
#     wb = xlrd.open_workbook('E://python3//test.xls')
#     sheet = wb.sheet_by_name('sanmu')
#     print(sheet)
#
#     dat =[]
#     for a in range(sheet.nrows):
#         cells = sheet.row_values(a)
#         print(cells)
#         data = int(cells[0])
#         dat.append(data)
#
#         return dat
# a = excel()
# print(a)
#
# def test(a):
#     for b in a:
#         print(b)
#         test(a)

def one_test():

    book = xlrd.open_workbook('E://python3//test.xls')
    sheet = book.sheet_by_name('sanmu')
    # sheet = book.sheets()[0]
    list = []
    for i in range(3, sheet.nrows):
        row = sheet.row_values(i)
        dict = {"type":row[1], "chinese":row[2],"english":row[3], "shortname":row[4],"description":row[5]}
        list.append(dict)
    print(json.dumps(list, ensuer_ascii= False))





