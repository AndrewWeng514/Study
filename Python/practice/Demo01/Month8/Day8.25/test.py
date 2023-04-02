# @Time    : 2022/8/25 9:21
# @Author  : Andrew
userAccount = {'1001': {'password': '123456', 'balance': '10000', 'currency': 'CNY', 'status': 'active'},
               '1002': {'password': '=111111', 'balance': '-200', 'currency': 'CNY', 'status': 'active'},
               '1003': {'password': '222222', 'balance': '2000000', 'currency': 'CNY', 'status': 'active'},
               '1004': {'password': '33333', 'balance': '8000000', 'currency': 'CNY', 'status': 'active'}
               }

# 3.1、【注册】
# 用户选择注册,提示输入用户账号
# 判断用户账号是否存在：
# 如果不存在，则提示输入密码，添加账户信息到字典中，账户的余额默认0,返回一级界面
#
#    如果存在，则提示用户"该账号已经存在，不能注册" ，返回一级界面
#
# # 3.2、【登录】
# # 用户选择登录,提示输入用户账号
# # 判断用户账号是否存在：
# # 如果账号存在，则提示输入密码，对密码进行判断：
# # 如果密码错误,提示”您的密码错误，请重新输入”,
# # 如果密码连续错误3次,提示”您的密码输入错误3次，请联系管理员”,返回一级界面。
# # 如果密码正确，进入二级界面
# # 如果账号不存在,则提示”您输入的账号不存在”，返回一级界面;
#


# 1、利用控制结构和数据类型，输入和输出编程
# 2、一级界面首页功能包含:【登录】、【注册】2个功能
flag = True
while flag:
    choice = input('======请选择您想进行的操作=====\n'
                   '=======输入[1]进行登录=======\n'
                   '=======输入[2]进行注册=======\n')
    if choice == '1':
        useraccount = input('请输入您的账号:')  # 接收登录的账
        if useraccount in userAccount:
            count = 1
            ##子功能5，返回上一级菜单的开关
            while count <= 3:  # 循环输错密码的次数
                password = input('请输入您的密码：')
                if password == userAccount[useraccount]['password']:  ##校验密码与输入的账号是否匹配
                    flag1 = True
                    while flag1:  ##匹配则进入二级菜单
                        choice1 = input('======请选择您想进行的操作=====\n'
                                        '=======输入[1]进行查询=======\n'
                                        '=======输入[2]进行存款=======\n'
                                        '=======输入[3]进行取款=======\n'
                                        '=======输入[4]进行转账=======\n'
                                        '=====输入[5]返回上级菜单======\n'
                                        )
                        if choice1 == '1':  ##查询账户余额
                            money1 = userAccount[useraccount]['balance']
                            print(f'您的账户余额为{money1}元')

                        elif choice1 == '2':  ##存款功能
                            money2 = input('请输入您想存入的金额：')
                            sumbalance = int(userAccount[useraccount]['balance']) + int(
                                money2)  ##存款后的账户余额=存款的金额+存款前账户的余额
                            userAccount[useraccount]['balance'] = str(sumbalance)  ##更新账户余额，并返回存款后的余额
                            print(f'当前您的账户余额一共为{sumbalance}元')

                        elif choice1 == '3':  ##取款功能
                            money3 = input('请输入您想取出的金额：')
                            money4 = userAccount[useraccount]['balance']  ##得到当前账户的余额：money4
                            if int(money3) > int(money4):  ##判断余额与所取的金额大小关系
                                print('您的余额不足')
                            else:
                                money5 = int(money4) - int(money3)  ##当前余额 = 取款前余额 — 所取出的金额
                                userAccount[useraccount]['balance'] = str(money5)  ##更新当前余额
                                print(f'取款成功，您当前的账户余额为{money5}元')

                        elif choice1 == '4':
                            account_other = input('请输入您想转账的账户账号：')
                            if account_other in userAccount:  ##校验转账账号是否已经存在
                                money5 = input('请输入您想转账的金额：')
                                money6 = userAccount[useraccount]['balance']
                                if int(money5) > int(money6):  ##校验转账金额money5与账户余额money6的大小关系
                                    print('您的余额不足')
                                else:
                                    money6 = int(money6) - int(money5)
                                    money7 = int(userAccount[account_other]['balance']) + int(money5)
                                    userAccount[useraccount]['balance'] = str(money6)  # 更新当前账户转账后的余额
                                    userAccount[account_other]['balance'] = str(money7)  # 更新被转帐户转账后的余额
                                    print(f'向{account_other}账户转账{money5}元成功,当前您的账户余额为{money6}元')
                            else:
                                print('对方账号不存在')

                        elif choice1 == '5':
                            break
                        else:
                            print('您输入的有误，请按要求进行输入')
                else:
                    print('您的密码错误，请重新输入')
                    count += 1
                break
            else:
                if count == 4:
                    print('您的密码输入错误3次，请联系管理员')

        else:
            print('您的账户不存在，请确认您的账号')



    elif choice == '2':  ##注册功能
        Account = input('请输入您的账号：')  # 接收输入的注册账号
        if Account in userAccount:
            print('该账户已经存在，不能注册')  ##如果存在，则输出提示语句
        elif Account not in userAccount:
            Password = input('请输入您的密码:')  ##如果不存在，则进行下一步：输入密码操作
            temp_dict = {'password': Password, 'balance': 0, 'currency': 'CNY', 'status': 'active'}
            userAccount.update({Account: temp_dict})  ##将注册的账号，密码以字典的形式存入账号字典中
            print('注册成功')
