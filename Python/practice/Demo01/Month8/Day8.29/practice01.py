# @Time    : 2022/8/29 16:26
# @Author  : Andrew
# 3.
# 定义一个函数, 对输入学生的信息进行判断打印：
# 场景1.
# 定义函数获取当前系统时间#
def getSystemTime():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S")


# # 将如下数据通过insertStudent函数存入stuList列表中,
stuList = []


def insertStudent(sid, stuName, *hobbies, stuBirth='', stuSex='', stuHeight='', **kwargs):
    stuList.append([sid, stuName, hobbies, stuBirth, stuSex, stuHeight, kwargs])
    return stuList


# 系统时间
# 实参如下：
# 1001, 'Kate', 'sing', 'dance', stuBirth = '2021-01-01', stuHeight = 160, recordTime = getSysTime()
# 1002, 'Mike', 'walk', 'run', 'swim', 'read', stuBirth = '1999-10-10', stuSex = 'M', recordTime = getSysTime()
# 1003, 'Jack', 'swim', stuSex = 'M', stuHeight = 178, recordTime = getSysTime()
# 1004, 'Linda', 'read', stuSex = 'F', recordTime = getSysTime()
# 1005, 'Rose', 'sing', 'read', 'swim', stuBirth = '2000-01-01', recordTime = getSysTime()
#
# 场景2.
# 定义checkStudent函数，对stuList中每个学生记录，检查Birth，Sex，Height是否为空字符串，
# 将这些信息不全的学生找出来, 具体哪个信息缺失
insertStudent(1001, 'Kate', 'sing', 'dance', stuBirth='2021-01-01', stuHeight='160', recordTime=getSystemTime()
              )
insertStudent(1002, 'Mike', 'walk', 'run', 'swim', 'read', stuBirth='1999-10-10', stuSex='M', recordTime=getSystemTime()
              )
insertStudent(1003, 'Jack', 'swim', stuSex='M', stuHeight='178', recordTime=getSystemTime())
insertStudent(1004, 'Linda', 'read', stuSex='F', recordTime=getSystemTime())
insertStudent(1005, 'Rose', 'sing', 'read', 'swim', stuBirth='2000-01-01', recordTime=getSystemTime())
print(stuList)


# 定义checkStudent函数，对stuList中每个学生记录，检查Birth，Sex，c是否为空字符串，
# 将这些信息不全的学生找出来, 具体哪个信息缺失
def checkStudent():
    list = []
    for stu in stuList:
        list = [stu[1]]
        # for noneInfo in stu[3:]:
        if stu[3] == '':
            list.append('Birth')
        if stu[4] == '':
            list.append('Sex')
        if stu[5] == '':
            list.append('Height')
        print(f'{list[0]}同学的 {list[1:]}信息缺失')


checkStudent()
