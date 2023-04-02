"""
 @Author: Andrew
 @FileName: xls.py
 @DateTime: 2022/10/17 16:18
 @Brief:DDT excel相关操作
"""
import xlrd, xlwt


#  读取测试用例并返回列表
def read_xls(self):
    testcases = []
    for i in range(1, self.sheet.nrows):
        testcases.append(self.sheet.row_values(i))
    return (testcases)


#  处理excel数据为['login-1', '用户名为空', '', 'woniu123', '0000', 'id', 'userNameMsg', '用户名不能为空.']
def read_xls_up(filead, sheetname):
    file = xlrd.open_workbook(filead)
    sheet = file.sheet_by_name(sheetname)
    testcases = []
    for i in range(1, sheet.nrows):
        if i:  # 如果有值才会执行添加元素的动作
            test_data = sheet.row_values(i)
            tem = test_data[0:2]
            # print(tem)
            for j in test_data[3].split('\n'):
                # print(j)
                tem.append(j.split('=')[-1])
            for j in test_data[4].split('\n'):
                # print(j)
                tem.append(j.split('=')[-1])
            testcases.append(tem)
    return (testcases)


if __name__ == '__main__':
    a = read_xls_up("../testdata/TestCase-up.xls", 'Sheet1')
    print(a)
