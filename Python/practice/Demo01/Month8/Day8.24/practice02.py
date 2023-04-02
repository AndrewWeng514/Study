# @Time    : 2022/8/24 15:53
# @Author  : Andrew
# 6.对下列列表进行处理：
stuInfo = [
    [1001, 'Kate', 185, 'Female', [70, 90, 98]],
    [1002, 'Mike', 165, 'Male', [75, 90, 100, 50, 98]],
    [1003, 'John', 170, 'Male', [100, 88, 98, 76]],
    [1003, 'John', 170, 'Male', []]
]
# 2、场景3：录入新的学生信息， 例如：将学生的学号：1005，姓名：Lucy, 身高：170,性别：Female
# #      #  分数：数学80分，语文90分，英语100分，录入系统中，可以循环录入不同的学生信息，
# #      #  已经存在的学号是不能录入的。


while True:
    # 设置菜单项
    print('=====功能1：按性别统计人数======\n'
          '=====功能2：统计平均分大于多少===\n'
          '=====功能3：添加学生信息=====\n'
          '=====功能4：删除没有成绩的学生====')

    choice = input('请进行选择：')
    if choice == '1':
        # 执行统计性别人数
        ssex = input('请输入性别Female,Male:')
        Fcount = 0
        Mcount = 0
        for info in stuInfo:
            # print(info)
            if info[3] == 'Female':
                Fcount = Fcount + 1
            elif info[3] == 'Male':
                Mcount = Mcount + 1
        if ssex == 'Female':
            print('女生的人：', Fcount)
        elif ssex == 'Male':
            print('男生的人数：', Mcount)
        else:
            print('请输入：Male ,Female')

    elif choice == '2':
        # 统计平均分数
        iavg = input("统计大于XXX平均分的人数：")
        count = 0
        for info in stuInfo:
            # print(info)
            # 计算每个学生平均分
            if len(info[-1]) == 0:
                avg = 0
            else:
                avg = sum(info[-1]) / len(info[-1])
            if avg > int(iavg):
                count = count + 1
            # print(info)
        print(count)
    elif choice == '3':
        stuNo = int(input('请录入学号：'))
        # 编号单独提取出来，放在列表中
        # 定义stuNos 空列表
        # 定义一个用户信息的空列表
        oneInfo = []
        stuNos = []
        for i in stuInfo:
            stuNos.append(i[0])
        # print(stuNos)
        if stuNo in stuNos:
            print("您输入的学号已经存在")
        else:
            sname = input("请录入姓名：")
            sheight = input("请录入身高：")
            ssex = input("请录入性别：")
            scorelist = input("请录入分数：").split(',')
            newScore = []  # 成绩的空列表，转换int 类型后，存在在该列表中
            print(scorelist)  # ['']
            if len(scorelist[0]) == 0:
                newScore = []  # 代表没有录入成绩
            else:
                for score in scorelist:  # 将socore成绩转换成int类型
                    news = int(score)
                    newScore.append(news)
            oneInfo.extend([stuNo, sname, sheight, ssex, newScore])
            stuInfo.append(oneInfo)
        print(stuInfo)
    elif choice == '4':
        # 删除没有成绩
        for info in stuInfo:
            if len(info[-1]) == 0:
                stuInfo.remove(info)  # 直接将该信息移除
        print(stuInfo)
    else:
        print("请按要求输入选项")
