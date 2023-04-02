# @Time    : 2022/8/31 17:05
# @Author  : Andrew
# 1. 练习文件的open(),close(),read(),readline(),readlines(),write(),tell(),seek()方法的用法
#
# 2. 把如下内容存放于txt文件中，将每行测试用例读取出来
'''
caseID,CaseName,Data1,Oper,Data2,ExpecteResult
1,add_正整数,100,+,200,300
2,add_正负数,-100,+,200,100
3,add_负数,-100,+,-100,-200
'''
import time

fb = open(r'./testCase3.txt', 'a+', encoding='utf-8')
fb.write('caseID,CaseName,Data1,Oper,Data2,ExpecteResult')
while True:
    words = input("请输入内容:")
    if words == 'q':
        break
    else:
        fb.write(f'\n{words}')
fb.close()


# txt = fb.readlines()
# print(txt,len(txt))

# 定义一个计算器acturalResult=computer(data1,oper,data2)函数实现计算器功能，从上述文本文件中读取数据，然后将
# 运算结果写入另外一个文本的报告文件中，报告文件除了记录用例相关信息外，还需要记录执行的时间和实际结果
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
fb2.write('caseID,CaseName,Data1,Oper,Data2,ExpecteResult,ActuralResult,Status')
height_case = fb.readlines()
# print(height_case,len(height_case),type(height_case) )
num = len(height_case)
fb.seek(0)
test_case = fb.readline()  # 读取标题行
# print(height_case,len(height_case),type(height_case) )
for i in range(num - 1):
    test_case = fb.readline()  # 读取每行用例
    list = test_case.split(',')  # 分割列表
    # print(list,len(list),type(list))
    # num1 = int(list[2])
    # num2 = int(list[4])
    ActuralResult = computer(int(list[2]), list[3], int(list[4]))  # 执行运算
    if ActuralResult == int(list[5]):
        print(f'{list[0]}通过')
        # test_time =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # list.insert(0,test_time)
        # list.append(str(ActuralResult))
        list.append('pass')
    else:
        print(f'{list[0]}没有通过')
        # test_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # list.insert(0, test_time1)
        # list.append(str(ActuralResult))
        list.append('block')
    test_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    list.insert(0, test_time)
    list.insert(-1, str(ActuralResult))
    # print(list)
    case_list = ','.join(list)
    # print(case_list)
    case_list = case_list.replace('\n', '')
    # fb2 = open(r'./testCase2.txt', 'a+', encoding='utf-8')
    # print(fb3.tell())
    fb2.write(f'\n{case_list}')
fb.close()
fb2.close()

#
# 测试报告内容样式：
# caseID,CaseName,Data1,Oper,Data2,ExpecteResult,ActuralResult,Status
# 1,add_正整数,100,+,200,300,300,Pass
# 2,add_正负数,-100,+,200,100,100,Pass
# 3,add_负数,-100,+,-100,-200,-200,Pass
