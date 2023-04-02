"""
 @Author: Andrew
 @FileName: test.py
 @DateTime: 2022/10/19 17:02
 @Brief:脚本测试文件
"""
import xlrd

['http://101.34.13.184:8080/WoniuBoss4.0/assets/addAss',
 'post',
 "{'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}",
 '{\n                "ass.assets_name": "01",\n                "ass.assets_type": "01",\n                "ass.bar_code": "23123221231",\n                "ass.price": "250",\n                "purchase_employee": "李四",\n                "ass.purchase_employee_id": "4",\n                "ass.purchase_time": "2022-10-01",\n                "ass.note": "API",\n                "ass.assets_owner": "01"\n            }',
 'AlreayExistCode']

sheet = xlrd.open_workbook("../testdata/asset.xls").sheet_by_name("Sheet1")
testcase = []
for i in range(1, sheet.nrows):
    cases = sheet.row_values(i)
    # print(cases)
    tem = cases[0:2]
    a = eval(cases[2])
    tem.append(a)
    b = eval(cases[3])
    tem.append(b)
    tem.append(cases[4])
    print(tem)
    testcase.append(cases)
print(eval(testcase))
