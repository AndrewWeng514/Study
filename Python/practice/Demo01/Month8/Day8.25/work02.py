# @Time    : 2022/8/25 19:45
# @Author  : Andrew

# 注册
userAccount = {'1001': {'password': '123456', 'balance': '10000', 'currency': 'CNY', 'status': 'active'},
               '1002': {'password': '111111', 'balance': '-200', 'currency': 'CNY', 'status': 'active'},
               '1003': {'password': '222222', 'balance': '2000000', 'currency': 'CNY', 'status': 'active'},
               '1004': {'password': '333333', 'balance': '8000000', 'currency': 'CNY', 'status': 'active'}
               }
a = '2'
while True:
    print('1.[登录]', '2.[注册]', sep='\n')
    choice = input('请输入您的选择:')
    if choice == '2':
        user_id = input('请输入用户账号:')
        if user_id in userAccount:
            print('该账号已经存在,不能注册')
        else:
            user_password = input("请输入密码:")
            newSet = {user_id: {'password': user_password, 'balance': '0', 'currency': 'CNY', 'status': 'active'}}
            userAccount.update(newSet)
    elif choice == '1':
        log_id = input('请输入您的账号:')
        if log_id not in userAccount:
            print('您输入的账号不存在')
        else:
            for count in range(0, 3):
                log_password = input("请输入密码:")
                if log_password != userAccount[log_id]['password']:
                    print('您的密码错误,请重新输入')
                    if count == 2:
                        print('您的密码输入错误3次，请联系管理员')
                else:
                    while True:
                        print('【1. 查询】', '【2. 存款】', '【3. 取款】', '【4. 转账】', '【5. 返回】', sep='\n')
                        choice2 = input('请输入您需要的功能:')
                        if choice2 == '1':
                            print('您的余额是:%s' % userAccount[log_id]['balance'])

                        elif choice2 == '2':
                            deposit = input('请输入存款金额:')
                            deposit = int(deposit)
                            user_balance = int(userAccount[log_id]['balance'])
                            sum_balance = deposit + user_balance
                            userAccount[log_id]['balance'] = str(sum_balance)
                            print('您存入了%s' % deposit)
                            print('你的余额是:%s' % userAccount[log_id]['balance'])
                        elif choice2 == '3':
                            cash = int(input('请输入取款金额'))
                            user_balance = int(userAccount[log_id]['balance'])
                            if cash > user_balance:
                                print('您的余额不足')
                            else:
                                print(f'本次取款:{cash}')
                                new_balance = user_balance - cash
                                userAccount[log_id]['balance'] = str(new_balance)
                                print('你的余额是:%s' % userAccount[log_id]['balance'])
                        elif choice2 == '4':
                            other_id = input('请输入需要转账的账号')
                            if other_id not in userAccount:
                                print('对方账号不存在')
                            elif other_id == log_id:
                                print('不能对自己转账')
                            else:
                                other_cash = int(input("请输入转账金额:"))
                                user_balance = int(userAccount[log_id]['balance'])
                                other_balance = int(userAccount[other_id]['balance'])
                                if other_cash > user_balance:
                                    print('您的余额不足')
                                else:
                                    print(f'本次转账:{other_cash}')
                                    new_balance01 = user_balance - other_cash  # 我方余额
                                    userAccount[log_id]['balance'] = str(new_balance01)
                                    print('你的余额是:%s' % userAccount[log_id]['balance'])
                                    new_balance02 = other_balance + other_cash  # 对方余额
                                    userAccount[other_id]['balance'] = str(new_balance02)
                        elif choice2 == '5':
                            break
                        else:
                            print('没有该功能,请重新选择!')
                    break
