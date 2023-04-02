# @Time    : 2022/8/31 19:46
# @Author  : Andrew
import time


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


fp = open(r'testCase.txt', 'r', encoding='utf-8')
fp1 = open(r'testCase2.txt', 'w', encoding='utf-8')
fp1.write('time,caseID,CaseName,Data1,Oper,Data2,ExpecteResult,ActuralResult,Status\n')
for i in range(4):
    result = fp.readline()
    if i > 0:
        caseID, CaseName, Data1, Oper, Data2, ExpecteResult = result.split(',')  # 1,add_正整数,100,+,200,300
        acturalResult = computer(int(Data1), Oper, int(Data2))
        if acturalResult == int(ExpecteResult):
            status = 'pass'
        else:
            status = 'block'
        systemTime = time.strftime('%Y-%m-%d %H-%M-%S')
        fp1.write(
            f'{systemTime},{caseID},{CaseName},{Data1},{Oper},{Data2},{int(ExpecteResult)},{acturalResult},{status}\n')
