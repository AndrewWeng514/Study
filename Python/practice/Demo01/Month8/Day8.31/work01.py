# @Time    : 2022/8/31 19:30
# @Author  : Andrew
# 2. 把如下内容存放于txt文件中，将每行测试用例读取出来
# caseID,CaseName,Data1,Oper,Data2,ExpecteResult
# 1,add_正整数,100,+,200,300
# 2,add_正负数,-100,+,200,100
# 3,add_负数,-100,+,-100,-200
#
# 定义一个计算器acturalResult=computer(data1,oper,data2)函数实现计算器功能，从上述文本文件中读取数据，然后将
# 运算结果写入另外一个文本的报告文件中，报告文件除了记录用例相关信息外，还需要记录执行的时间和实际结果
#
# 测试报告内容样式：
# caseID,CaseName,Data1,Oper,Data2,ExpecteResult,ActuralResult,Status
# 1,add_正整数,100,+,200,300,300,Pass
# 2,add_正负数,-100,+,200,100,100,Pass
# 3,add_负数,-100,+,-100,-200,-200,Pass

fp = open(r'case.txt', 'w+', encoding='utf-8')
fp.write('caseID,CaseName,Data1,Oper,Data2,ExpecteResult\n'
         '1,add_正整数,100,+,200,300\n'
         '2,add_正负数,-100,+,200,100\n'
         '3,add_负数,-100,+,-100,-200')
fp.seek(0)


# result = fp.read()
# print(result)

###调用计算器函数
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


###从case文档中传参
testCase = fp.readlines()
print(testCase, type(testCase), len(testCase))
list_Case = []
for i in range(len(testCase)):
    if i == 0:
        continue
    else:
        list_temp = testCase[i].split(',')  # 'list_temp=[ 1,add_正整数,100,+,200,300\n]
        a = list_temp[5].replace('\n', '')  # a=300
        list_temp.pop(5)  # list_temp=[ 1,add_正整数,100,+,200]
        list_temp.append(a)  # list_temp=[ 1,add_正整数,100,+,200,300]
        list_Case.append(list_temp)  # list_Case=[ 1,add_正整数,100,+,200,300]
fp.close()
fp = open(r'report.txt', 'w+', encoding='utf-8')
fp.write('caseID,CaseName,Data1,Oper,Data2,ExpecteResult,ActuralResult,Status\n')

for i in list_Case:
    if int(i[5]) == computer(int(i[2]), i[3], int(i[4])):
        Status = 'Pass'
    else:
        Status = 'Fault'
    a = computer(int(i[2]), i[3], int(i[4]))
    test_report = []
    test_report.extend(i)
    test_report.append(a)
    test_report.append(Status)
    result = f'{test_report[0]},{test_report[1]},{test_report[2]},{test_report[3]},{test_report[4]},' \
             f'{test_report[5]},{test_report[6]} ,{test_report[7]}\n'
    fp.write(result)
fp.seek(0)
fp.close()
