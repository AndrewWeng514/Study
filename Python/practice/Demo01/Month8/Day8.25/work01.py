# @Time    : 2022/8/25 19:19
# @Author  : Andrew
# 题目内容
#
# 实现woniuATM取款机的操作，需求描述如下
userAccount = {'1001': {'password': '123456', 'balance': '10000', 'currency': 'CNY', 'status': 'active'},
               '1002': {'password': '111111', 'balance': '-200', 'currency': 'CNY', 'status': 'active'},
               '1003': {'password': '222222', 'balance': '2000000', 'currency': 'CNY', 'status': 'active'},
               '1004': {'password': '333333', 'balance': '8000000', 'currency': 'CNY', 'status': 'active'}
               }
# print(userAccount)
# print('1001'in userAccount)

# 1、利用控制结构和数据类型，输入和输出编程
# 2、一级界面首页功能包含:【登录】、【注册】2个功能
# 代码实现
'''
# print('1.[登录]','2.[注册]',sep='\n')
# choice = input('请输入您的选择:')
# if choice == '2':
'''
# 3.1、【注册】 要求
'''用户选择注册,提示输入用户账号
判断用户账号是否存在：
如果不存在，则提示输入密码，添加账户信息到字典中，账户的余额默认0,返回一级界面

   如果存在，则提示用户"该账号已经存在，不能注册" ，返回一级界面
 '''
# 注册代码实现
'''
  user_id = input('请输入用户账号:')
    if user_id in userAccount:
        print('该账号已经存在,不能注册')
    else:
        user_password = input("请输入密码:")
        newSet = {user_id: {'password': user_password, 'balance': '0', 'currency': 'CNY', 'status': 'active'}}
        userAccount.update(newSet)
    print(userAccount)
'''
# 3.2、【登录】要求
'''
用户选择登录,提示输入用户账号
判断用户账号是否存在：
如果账号存在，则提示输入密码，对密码进行判断：
如果密码错误,提示”您的密码错误，请重新输入”,
如果密码连续错误3次,提示”您的密码输入错误3次，请联系管理员”,返回一级界面。
如果密码正确，进入二级界面
如果账号不存在,则提示”您输入的账号不存在”，返回一级界面;
'''
# 登录  代码实现
'''
log_id = input('请输入')
if log_id not in userAccount:
    print('您输入的账号不存在')
else:
    for count in range(0,3):
        log_password = input("请输入密码:")
        if log_password != userAccount[log_id]['password']:
            print('您的密码错误,请重新输入')
            if count ==2:
                print('您的密码输入错误3次，请联系管理员')
        else:
            pass
'''

#  4、二级界面功能包含:【1. 查询】、【2. 存款】、【3. 取款】、【4. 转账】、【5. 返回】5个功能
#  print('【1. 查询】','【2. 存款】','【3. 取款】','【4. 转账】','【5. 返回】',sep='\n')
# choice2 = input('请输入您需要的功能:')
# 4.1、【1. 查询】
# # 用户选择查询,直接查出用户账户的余额
# 代码实现
'''
if choice2 == '1':
    print(userAccount[log_id]['balance'])
'''
# 4.2、【2. 存款】
# 用户选择存款,需要输入存入的金额,存款成功后,需要给用户进行提示,用户的余额对应增加
# 代码实现
'''
deposit = input('请输入存款金额:')
deposit = int(deposit)
user_balance =int(userAccount['1001']['balance'])
sum_balance = deposit +user_balance
userAccount['1001']['balance'] = str(sum_balance)
print('你的余额是:%s'%userAccount['1001']['balance'])
'''
# 4.3、【3. 取款】 要求
'''
用户选择取款，要求用户输入取款额，判断用户的余额是否充足,
如果余额不足则提示”您的余额不足”;
如果余额充足则取款成功,用户账户余额对应减少
'''
# 代码实现
'''
cash = int(input('请输入取款金额'))
user_balance = int(userAccount['1001']['balance'])
if cash > user_balance:
    print('您的余额不足')
else:
    print(f'本次取款:{cash}')
    new_balance = user_balance - cash
    userAccount['1001']['balance']=str(new_balance)
    print('你的余额是:%s'%userAccount['1001']['balance'])
'''
# 4.4、【4. 转账】要求
'''
用户选择转账,需要输入转账账号、金额,先判断转账的账号是否存在,
如果不存在则提示用户”对方账号不存在”;
如果存在，判断自己余额是否充足：
如果充足，进行转账,转出账号的余额减少,转入账号的余额增加
如果不充足，提醒余额不足
'''
# 代码实现
'''
other_id = input('请输入需要转账的账号')
if other_id not in userAccount:
    print('对方账号不存在')
else:
    other_cash =  int(input("请输入转账金额:"))
    user_balance = int(userAccount['1001']['balance'])
    other_balance =int(userAccount[other_id]['balance'])
    if other_cash > user_balance:
        print('您的余额不足')
    else:
        print(f'本次转账:{other_cash}')
        new_balance01 = user_balance - other_cash#我方余额
        userAccount['1001']['balance'] = str(new_balance01)
        print('你的余额是:%s' % userAccount['1001']['balance'])
        new_balance02 = other_balance + other_cash  # 敌方余额
        userAccount[other_id]['balance'] = str(new_balance02)
        print('你的余额是:%s' % userAccount[other_id]['balance'])

'''

# 4.5、【5. 返回】
# 用户选择返回,则退出二级界面，回到一级操作界面，提示用户进行登陆或者注册
# “””
#
# 测试用例：
#
# 选择注册，输入账号1001，系统应该提示账户存在，不允许
# 选择注册，输入账号1009，密码111111，看系统结果，应该创建成功
# 选择登录，输入账号1009，输入密码1，看系统提示，密码输错3次，系统应该提示练习管理员
# 选择登录，输入账号1009，输错2次，第3次输入正确，应该正常登录系统
# 4.1 选择【查询】，系统应该正确显示余额
# 4.2 选择【存款】，系统提醒输入金额，数据输入后，选择查询，余额应该显示正确的累加结果
# 4.3 选择【取款】，系统提醒输入金额，输入超过余额的取款数，系统应该提示余额不足
# 4.3 选择【取款】，系统提醒输入金额，输入不超过余额的取款数，系统应该正确扣除取款，余额显示正确
# 4.4 选择【转账】，系统提示输入对方账号，输入1010，系统应该提示对方账号不存在
# 4.5 选择【转账】，系统提示输入对方账号，输入1002，系统提示转账额度，输入大于自己余额的数据，系统应该提示余额不足
# 4.6 选择【转账】，系统提示输入对方账号，输入1002，系统提示转账额度，输入小于自己余额的数据，系统应该正常转账，自己账户和对方账户的余额都修改正确
# 4.7 选择【返回】，系统显示一级界面，提示用户进行登录或者注册
