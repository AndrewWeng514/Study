# @Time    : 2022/8/26 9:11
# @Author  : Andrew
# 1.
# 定义无参函数，返回当前的系统时间格式，格式要求：YYYY - MM - DD
# HH: MM:SS
# 提醒：借助time包进行操作
def getSysTime():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S")


'''
def getSign ():  #获取分割符
    sign1 = input('请输入日期的分割符:')
    sign2 = input('请输入时间的分割符:')
    print(sign1,sign2)
    return [sign1,sign2]

def getSysTime():   #按格式格式分割时间
    import time
    list = getSign()
    a= list[0]
    b = list[1]
    return time.strftime(f'%Y{a}%m{a}%d %H{b}%M{b}%S')
'''

# 3.
# 执行如下代码，思考打印出来的data为什么是None
#
#
# def add():  # 函数定义def
#     data1 = 100
#     data2 = 200
#     print(data1 + data2)
#
#
# data = add()
# print('add函数运算的结果为:', data)
#

# 4.
# 执行如下代码，思考为什么代码会报错？
#
# def add():  # 函数定义def
#     data1 = 100
#     data2 = 200
#     result = data1 + data2
#     return result
#
#
# add()  # 函数调用
# print('add函数运算的结果为:', result)
#
# 5.
# 分别定义A，B，C三个无参函数，A函数调用B，B函数调用C，
# 运行A函数，要求打印出A，B，C三个函数运行的开始时间和结束时间
# 时间等待
'''  
import time
def A():
    print('A is begining at',getSysTime())
    time.sleep(2)
    B()
    time.sleep(2)
    print('A is end at',getSysTime())

def B():
    print('B is begining at', getSysTime())
    time.sleep(2)
    C()
    time.sleep(2)
    print('B is end at',getSysTime())
def C():
    print('C is begining at', getSysTime())
    time.sleep(2)
    print('C is end at',getSysTime())
A()
'''
6.
# 定义一个checkUser(UserID, password)
# 函数, 实现对用户账号在字典中的判断
# 判断如果UserID在字典中不存在，返回 - 1
# 判断如果UserID在字典中存在，但密码错误，返回 - 2
# 判断如果UserID在字典中存在，且密码正确，状态不是Active，返回 - 3
# 判断如果UserID在字典中存在，且密码正确，状态是Active，返回0
userInfo = {
    1001: {'password': 111111, 'status': 'Active'},
    1002: {'password': 222222, 'status': 'Active'},
    1003: {'password': 121212, 'status': 'inActive'}}


def checkUser(UserID, password):
    if UserID not in userInfo:
        result = -1
    else:
        if password != str(userInfo[UserID]['password']):
            result = -2
        else:
            if userInfo[UserID]['status'] == 'Active':
                result = 0
            else:
                result = -3
    return result


#
# 定义一个login函数，函数内通过input接收UserID和Password，login调用checkUser函数
# 如果checkUser返回 - 1，打印
# "账号不存在"
# 如果checkUser返回 - 2，打印
# "账号密码错误"
# 如果checkUser返回 - 3，打印
# "账号被禁用"
# 如果checkUser返回0，打印
# "账号正确，欢迎"
def login():
    UserID = int(input('请输入用户账号'))
    password = input('请输入密码')
    result = checkUser(UserID, password)
    if result == -1:
        print("账号不存在")
    elif result == -2:
        print('账号密码错误')
    elif result == -3:
        print("账号被禁用")
    else:
        print("账号正确，欢迎")


login()
