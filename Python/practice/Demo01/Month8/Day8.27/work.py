# @Time    : 2022/8/27 14:44
# @Author  : Andrew
#   1. 对银行账号进行破解，
'''
1. 对银行账号进行破解，
   假定银行账号accID是4位数字,范围1000-9999，
   密码password是6位数字，范围100000-999999，
   先进行账号破解，
   如果命中一个账号后，开始破解该账号对应的密码：
      如果当前账号密码正确，打印账号及密码，停止后续密码尝试，开始破解下一个账号；
      如果当前账号密码不正确，继续尝试后续密码；
   如果账号没有命中，则继续生成下一个账号进行尝试
 userAccount =
 {
  '1001':{'password':'123456','banlance':'10000','currency':'CNY','status':'active'},
  '2002':{'password':'111111','banlance':'-200','currency':'CNY','status':'active'},
  '3003':{'password':'222222','banlance':'2000000','currency':'CNY','status':'active'},
  '4004':{'password':'333333','banlance':'8000000','currency':'CNY','status':'active'}
 }

'''
#  代码实现
userAccount = {
    '1001': {'password': '100000', 'banlance': '10000', 'currency': 'CNY', 'status': 'active'},
    '2002': {'password': '111111', 'banlance': '-200', 'currency': 'CNY', 'status': 'active'},
    '3003': {'password': '222222', 'banlance': '2000000', 'currency': 'CNY', 'status': 'active'},
    '4004': {'password': '333333', 'banlance': '8000000', 'currency': 'CNY', 'status': 'active'}
}
for userId in range(1000, 10000):
    userId = str(userId)
    if userId in userAccount:
        for userPassward in range(100000, 1000000):
            userPassward = str(userPassward)
            if userPassward == userAccount[userId]['password']:
                print(f'账号是:{userId}', f'密码是:{userPassward}')
                break
#   2.学生信息统计
'''
7. stuInfo=[
        [1001,'Kate',185,'Female',[70,90,91],"sing,dance,run"],
 		[1002,'Mike',165,'Male',[75,90,100,50,98],"dance,draw"],
		[1003,'John',170,'Male',[100,88,98,76],"walk,read,run"],
 		[1004,'Danny',165,'Male',[89,90,100,77,99],"sing,walk,swim"],
		[1005,'Rose',170,'FeMale',[98,82,99,79],"swim,read"],
        [1006,'Linda',165,'FeMale',[75,90,63,50,88],"dance,swim"],
		[1007,'Jane',170,'FeMale',[56,78,92,73],"sleep"]
        ]
   使用for循环实现如下操作
   1. 统计每个学生的平均成绩，将其打印出来
   2. 统计全班学生的平均成绩，将其打印出来
   3. 统计全班同学中，喜欢sing的有多少人
   4. 统计班级同学平均身高
   5. 统计班级同学最大身高，和最小身高

'''
# 代码实现
stuInfo = [
    [1001, 'Kate', 185, 'Female', [70, 90, 91], "sing,dance,run"],
    [1002, 'Mike', 165, 'Male', [75, 90, 100, 50, 98], "dance,draw"],
    [1003, 'John', 170, 'Male', [100, 88, 98, 76], "walk,read,run"],
    [1004, 'Danny', 165, 'Male', [89, 90, 100, 77, 99], "sing,walk,swim"],
    [1005, 'Rose', 170, 'FeMale', [98, 82, 99, 79], "swim,read"],
    [1006, 'Linda', 165, 'FeMale', [75, 90, 63, 50, 88], "dance,swim"],
    [1007, 'Jane', 170, 'FeMale', [56, 78, 92, 73], "sleep"]
]
while True:
    print('1. 统计每个学生的平均成绩，将其打印出来'
          , '2. 统计全班学生的平均成绩，将其打印出来'
          , '3. 统计全班同学中，喜欢sing的有多少人'
          , '4. 统计班级同学平均身高'
          , '5. 统计班级同学最大身高，和最小身高', sep='\n')
    choice = input('请输入你的选择:')
    if choice == '1':
        for stu in stuInfo:
            avgScore = sum(stu[4]) / len(stu[4])
            print(stu[1], '的平均成绩是%.1f' % avgScore)
    if choice == '2':
        sumAll = 0
        lenAll = 0
        for stu in stuInfo:
            sumAll += sum(stu[4])
            lenAll += len(stu[4])
        avgScore = sumAll / lenAll
        print('全班的平均成绩是%.1f' % avgScore)
    if choice == '3':
        count = 0
        for stu in stuInfo:
            #     count += stu[-1].count('sing')
            #     print('全班有%d人喜欢sing'%count)
            if 'sing' in stu[-1]:
                count += 1
        print('全班有%d人喜欢sing' % count)
    if choice == '4':
        sumAll = 0
        for stu in stuInfo:
            sumAll += stu[2]
            avgHeight = sumAll / len(stuInfo)
        print('全班的平均身高是%.1f' % avgHeight)
    if choice == '5':
        maxHeight = stuInfo[0][2]
        minHeight = stuInfo[0][2]
        for stu in stuInfo:
            if maxHeight <= stu[2]:
                mxHeight = stu[2]
            elif minHeight >= stu[2]:
                minHeight = stu[2]
        print('最大身高是%d' % maxHeight, '最小身高是%d' % minHeight)

#   3.猜数游戏
'''
   import random
   通过代码随机生成一个1-100之间的整数，random.randint(1,100)
   从键盘输入一个1-100之间的整数，系统判断：
   如果输入的数据小于随机数，系统提示"Too small";
   如果输入的数据大于随机数，系统提示"Too big";
   如果输入的数据=随机数，系统提示"Congratulations!!!"
   总共猜测6次机会，看你是否猜中系统的随机数把猜数的练习给改造成while循环的结构
'''
#   代码实现
import random

count = 1
while True:
    if count < 7:
        num1 = int(input('猜数游戏\n请输入你的数字:'))
        num2 = random.randint(1, 100)
        if num1 < num2:
            print('第%d次游戏结果:' % count)
            print('Too small !')
        elif num1 < num2:
            print('第%d次游戏结果:' % count)
            print('Too big !')
        else:
            print('第%d次游戏结果:' % count)
            print('Congratulations!!!')
        count += 1
    else:
        print('游戏结束')
        break

#   4.输入日期的合法性
'''
6. 输入一个年月日，判断年月日的合法性(需要嵌套分支) year,month,day=input().split('-')
   6.1 要求年份在1000-9999之间算合法，月份在1-12之间算合法
   6.2 针对日期，要求1,3,5,7,8,10,12月，日期在1-31之间算合法
       要求月份4,6,9,11，日期在1-30之间算合法
       要求月份2月份，闰年1-29算合法，非闰年，1-28算合法
   提示：
   1. 闰年的判断依据：
       能被4整除，但不能被100整除的为闰年 或者 能被400整除的年份为闰年
   2. 月份建议用列表存储 bigmonth=[1,3,5,7,8,10,12]  smallmonth=[4,6,9,11]
   3. 建议先判断年份的合法性，
    年份合法再判断月份的合法性，
    月份合法再判断天的合法性，判断天时，根据不同的月份做不同的判断，尤其是二月，需要考虑是否闰年
     
   4. 年份如果不合法直接打印年份错误，不需要去判断月份了
   5. 月份如果不合法直接打印月份错误，不需要去判断天了

'''
# 代码实现
while True:
    year, month, day = int(input('请输入年,月,日,并且以\'_\'分割\n')).split('-')
    print(type(year), year)
    year = int(year)
    month = int(month)
    day = int(day)
    if year not in range(1000, 10000):
        print('请输入1000-9999之间的年份')
    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day in range(1, 32):
                print(f'成功录入日期:{year}-{month}-{day}')
            else:
                print('这是个大月,请输入1-31的日期')
        elif month in [4, 6, 9, 11]:
            if day in range(1, 31):
                print(f'成功录入日期:{year}-{month}-{day}')
            else:
                print('这是个小月,请输入1-30的日期')
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day in range(1, 30):
                    print(f'成功录入日期:{year}-{month}-{day}')
                else:
                    print('今年是闰年,请输入1-29的日期')
            else:
                if day in range(1, 29):
                    print(f'成功录入日期:{year}-{month}-{day}')
                else:
                    print('今年是平年,请输入1-28的日期')
        else:
            print('请输入1-12的月份')
