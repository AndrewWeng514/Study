# @Time    : 2022/8/24 15:58
# @Author  : Andrew
stuInfo = [
    [1001, 'Kate', 185, 'Female', [70, 90, 98]],
    [1002, 'Mike', 165, 'Male', [75, 90, 100, 50, 98]],
    [1003, 'John', 170, 'Male', [100, 88, 98, 76]],
    [1003, 'John', 170, 'Male', []]
]
print("1.按性别统计人数", '2.统计平均分大于多少', '3.添加学生信息', '4.删除没有成绩的学生信息', sep='\n')
choice = input('请输入您的选择')
if choice.isdigit():
    if choice not in ['1', '2', '3', '4']:
        print('没有该功能')
    else:
        if choice == '1':
            print('按性别统计人数')
            str = input("请输入性别 male-男 female-女:")
            if str not in ['male', 'female']:
                print('请输入正确的性别')
            else:
                m = 0
                count = 0
                while m < len(stuInfo):
                    i = stuInfo[m][3]
                    if i == str:
                        count += 1
                        m += 1
                    else:
                        m += 1
                print(count)
        elif choice == '2':
            print('统计平均分大于多少的人数')
            num = input('请输入平均数:')
            if num.isdigit() == False:
                print('请输入数字!')
            else:
                if int(num) not in range(101):
                    print('请输入0-100的数字')
                else:
                    count = 0
                    for info in stuInfo:
                        if len(info[-1]) == 0:
                            avg = 0
                        else:
                            avg = sum(info[-1]) / len(info[-1])
                        if avg > int(num):
                            count = count + 1



        elif choice == '3':
            pass
        else:
            pass
else:
    print('请输入1,2,3,4数字')
