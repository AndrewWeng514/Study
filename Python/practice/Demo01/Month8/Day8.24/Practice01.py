# @Time    : 2022/8/24 12:16
# @Author  : Andrew
# 1、石头剪刀布游戏：剪刀：0，石头：1，布： 2 ，利用随机数，和电脑玩石头剪刀布游戏。
from turtle import clear

#
# while True:
#     import random
#     print('石头剪刀布','剪刀:0 石头:1 布:2',sep='\n')
#     choice1 = input('请输入您的选择:')
#     choice2 = random.randint(0,2)
#     print("电脑的选择:",choice2)
#     if choice1 == 0:
#         if choice2 ==0:
#             print('平局')
#         elif choice2== 1:
#             print('你输了')
#         else:
#             print('你赢了')
#     elif choice1 == 1:
#         if choice2 ==0:
#             print('你输了')
#         elif choice2== 1:
#             print('平局')
#         else:
#             print('你输了')
#     else :
#         if choice2 ==0:
#             print('你赢了')
#         elif choice2== 1:
#             print('你输了')
#         else:
#             print('平局')

###  if涵盖所有的胜利条件
###    代表数字之间的差值是2的时候是

# 6.对下列列表进行处理：
stuInfo = [
    [1001, 'Kate', 185, 'Female', [70, 90, 98]],
    [1002, 'Mike', 165, 'Male', [75, 90, 100, 50, 98]],
    [1003, 'John', 170, 'Male', [100, 88, 98, 76]]
]

# # 场景3：录入新的学生信息， 例如：将学生的学号：1005，姓名：Lucy, 身高：170,性别：Female
#      #  分数：数学80分，语文90分，英语100分，录入系统中，可以循环录入不同的学生信息，
#      #  已经存在的学号是不能录入的。
print('1,录入学生信息', '2,录入学生成绩', sep='\n')
choice = input('请输入您的选择')
if choice == '1':
    listNew = [0, 0, 0, 0]
    sid = input('请输入学号')
    if sid in stuInfo:
        print('您输入的学号已存在,请重新输入')
    else:
        listNew[0] = (sid)
        sname = input('请输入姓名')
        listNew[1] = (sname)
        slen = input('请输入身高')
        listNew[2] = (slen)
        ssex = input('请输入性别')
        listNew[3] = (ssex)

# listScore =[0,0,0]
# Sch =  input('语文成绩')
# listScore[0]=Sch
# Smath = input('数学成绩')
# listScore[1]= Smath
# Senglish = input('英语成绩')
# listScore[2] = Senglish
# print(listScore)
# # 场景4： 将没有的成绩的学生，在strInfo中删除。
