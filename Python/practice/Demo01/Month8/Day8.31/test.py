# @Time    : 2022/8/31 9:39
# @Author  : Andrew
# @Time    : 2022/8/31 17:05
# @Author  : Andrew
import time


def computer(data1, oper, data2):
    if oper == '-':
        ActuralResult = data1 - data2
    if oper == '+':
        ActuralResult = data1 + data2
    if oper == '*':
        ActuralResult = data1 * data2
    if oper == '/':
        ActuralResult = data1 / data2
    return ActuralResult


fb = open(r'testCase.txt', 'r', encoding='utf-8')
fb2 = open(r'testCase2.txt', 'w+', encoding='utf-8')
fb2.write('caseID,CaseName,Data1,Oper,Data2,ExpecteResult,ActuralResult,Status\n')
# num =len(fb.readlines())
fb.seek(0)
test_case = fb.readline()  # 读取标题行
# print(height_case,len(height_case),type(height_case) )
for i in range(len(fb.readlines()) - 1):
    test_case = fb.readline()  # 读取每行用例
    list = test_case.split(',')  # 分割列表
    # print(list,len(list),type(list))
    num1 = int(list[2])
    num2 = int(list[4])
    ActuralResult = computer(num1, list[3], num2)  # 执行运算
    if ActuralResult == int(list[5]):
        print(f'{list[0]}通过')

        list.append('pass')
    else:
        print(f'{list[0]}没有通过')
        list.append('block')
    test_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    list.insert(0, test_time1)
    list.insert(-1, str(ActuralResult))
    # print(list)
    case_list = ','.join(list)
    # print(case_list)
    case_list = case_list.replace('\n', '')
    # fb2 = open(r'./testCase2.txt', 'a+', encoding='utf-8')
    # print(fb3.tell())
    fb2.write(f'{case_list}\n')
