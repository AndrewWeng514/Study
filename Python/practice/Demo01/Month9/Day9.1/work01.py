# @Time    : 2022/9/1 10:14
# @Author  : Andrew
#  文本文件


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


# input: txt file   output: list
def readFile(file):
    fp = open(file, 'r', encoding='utf-8')
    caseList = fp.readlines()
    fp.close()
    return caseList


def writeFile(file, mode, str):
    fp = open(file, mode, encoding='utf-8')
    fp.write(str)
    fp.close()


caseList = readFile('./testCase.txt')  # 1.读取测试数据
Title = caseList.pop(0)
Title = Title.replace('\n', '')
mystr = Title + "," + "ActuralResult" + "," + "Status\n"
for case in caseList:
    caseID, caseName, data1, oper, data2, exResult = case.split(',')  # 2. 测试数据解析
    acResult = computer(int(data1), oper, int(data2))  # 3. 调用被测试对象computer，并且传参，得到实际结果
    case = case.replace('\n', '')
    if int(exResult) == acResult:  # 4. 比较实际结果和期望结果
        mystr = mystr + f"{case},{acResult},{'Pass'}\n"
    else:
        mystr = mystr + f"{case},{acResult},{'Fail'}\n"

fp2 = writeFile('./testReport.txt', 'a', mystr)
