# @Time    : 2022/8/31 20:49
# @Author  : Andrew
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


#  读取所有的测试用例  input:txt file  output: list
def readTestCase(file):
    fp = open(file, 'r', encoding='utf-8')
    caseList = fp.readlines()
    fp.close()
    return caseList


#  改写测试标题标题
def writeReport(file, mode, str):  # file :文件地址  mode:模式(a,r,w) str:标题名
    fp = open(file, mode, encoding='utf-8')
    fp.write(str)
    fp.close()


caseList = readTestCase('./testCase.txt')  # 读取所有测试用例
Title = caseList.pop(0)  # 读取标题行   赋予Title
Title = Title.replace('\n', '')  # 将标题行中的换行符替换为空字符
mystr = Title + "," + "ActuralResult" + "," + "Status\n"  # 形成测试报告的标题
for case in caseList:
    caseID, caseName, data1, oper, data2, exResult = case.split(',')
    actualResult = computer(int(data1), oper, int(data2))
    case = case.replace('\n', '')
    if int(exResult) == actualResult:
        mystr = mystr + f"{case},{actualResult},{'Pass'}\n"
    else:
        mystr = mystr + f"{case},{actualResult},{'Pass'}\n"
fp2 = writeReport('./testReport.txt', 'a', mystr)
