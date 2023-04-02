# @Time    : 2022/9/1 10:45
# @Author  : Andrew

import xlrd, xlwt


def computer(data1, oper, data2):
    if oper == "+":
        result = data1 + data2
    elif oper == "-":
        result = data1 - data2
    elif oper == "*":
        result = data1 * data2
    elif oper == "/":
        result = data1 / data2
    elif oper == "%":
        result = data1 % data2
    else:
        result = -1
    return result


def read_doc():
    pass


# # 1. 打开文件，返回文件对象
# fileObj=xlwt.Workbook(encoding = 'utf-8')       #创建一个新的Excel文件
# # 2. 新增一个sheet表单
# sheetObj = fileObj.add_sheet('My Worksheet')  #创建一个新的worksheet
# # 3. 写入表单单元格内容
# sheetObj.write(行号,列号, label = '内容')
# # 4. 保存表单
# fileObj.save(文件名称)
# fileObj.save(文件名称)
report_doc = xlwt.Workbook(encoding='utf-8')  # 新建一个表格文件
reporrt_sheet = report_doc.add_sheet('testReport')  # 新建一个表
# fileObj = xlrd.open_workbook('../computerCases.xls')
# sheetObj = fileObj.sheet_by_index(0)
# testCase = sheetObj.row_values(0)
# for i in range(0, len(testCase)):
#     reporrtSheet.write(0, i, label=f'{testCase[i]}')
# reportObj.save('./testReport.xls')

test_doc = xlrd.open_workbook('../computerCases.xls')  # 打开测试用例文件
test_sheet = test_doc.sheet_by_index(0)  # 打开表1
# testCase = sheetObj.row_values(0)#提取标题栏
# testCase.extend(["ActuralResult","Status"]) #标题栏增加实际值和状态
# for i in range(0, len(testCase)):
#     reporrtSheet.write(0, i, label=f'{testCase[i]}')


for i in range(0, test_sheet.nrows):  # 按文件总行数进行循环
    if i == 0:  # 当行数为0时,标题行  需要增加实际值和状态
        test_Case = test_sheet.row_values(i)  # 提取标题栏为列表
        test_Case.extend(["ActuralResult", "Status"])  # 标题栏增加实际值和状态
        for j in range(0, len(test_Case)):  # 遍历标题中每个元素
            reporrt_sheet.write(i, j, label=f'{test_Case[j]}')  # 在报告单中输入标题栏
    else:  # 当  遍历到其它行时为测试用例   需要进行操作
        test_Case = test_sheet.row_values(i)  # 提取测试用例
        # print(len(testCase),testCase,type(testCase))
        actualResult = computer(int(test_Case[2]), test_Case[3], int(test_Case[4]))  # 调用计算器  计算实际值
        if actualResult == int(test_Case[5]):  # 实际值和预期值进行比较
            test_Case.extend([f'{actualResult}', 'pass'])  # 相同时 则在用例后方添加实际值,状态
        else:
            test_Case.extend([f'{actualResult}', 'Fail'])  # 不同时 则在用例后方添加实际值,状态
        for j in range(0, len(test_Case)):  # 将新的用例表进行遍历
            reporrt_sheet.write(i, j, label=f'{test_Case[j]}')  # 将新的用例表插入到报告文件中
report_doc.save('./testReport.xls')

# for i in  range (0,sheetObj.nrows):
